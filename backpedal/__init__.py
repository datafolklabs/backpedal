
import os


class BackpedalArgumentError(Exception): pass

DEBUG = False
if 'BACKPEDAL_DEBUG' in os.environ.keys():
    if int(os.environ['BACKPEDAL_DEBUG']) == 1:
        DEBUG = True


def log(msg):
    if DEBUG is True:
        print('+++ BACKPEDAL // %s' % msg)


def abspath(path):
    """
    Return an absolute path, while also expanding the '~' user directory
    shortcut.

    :param path: The original path to expand.
    :rtype: str

    """
    return os.path.abspath(os.path.expanduser(path))


def down(path=None):
    if path is None:
        path = os.curdir

    path = abspath(path)

    log('backpeddling downward from path: %s' % path)

    ### directories and files in this path
    items = os.listdir(path)
    dirs, files = [], []

    for item in items:
    	if os.path.isdir(os.path.join(path, item)):
    		dirs.append(item)
    	else:
    		files.append(item)

    yield path, dirs, files

    if len(dirs) > 0:
        for sub_dir in dirs:
            next_path = abspath(os.path.join(path, sub_dir))
            for x in down(next_path):
                yield x
    else:
        return


def up(path=None):
    if path is None:
        path = os.curdir

    path = abspath(path)

    log('backpeddling upward from path: %s' % path)

    ### directories and files in this path
    items = os.listdir(path)
    dirs, files = [], []

    for item in items:
    	if os.path.isdir(os.path.join(path, item)):
    		dirs.append(item)
    	else:
    		files.append(item)

    yield path, dirs, files

    next_path = abspath(os.path.dirname(path))

    ### stop when we hit the top
    if next_path == path:
    	return

    ### iterate
    for x in up(next_path):
        yield x


def find(item, path=None, direction='up', first_only=True, item_type='file'):
    try:
        assert direction in ['up', 'down', 'both'], \
            "Argument 'direction' must be one of ['up', 'down', 'both']."
        assert first_only in [True, False], \
            "Argument 'first_only' must be one of [True, False]."
        assert item_type in ['file', 'directory', 'both'], \
            "Argument 'item_type' must be one of ['file', 'directory', 'both']"
    except AssertionError as e:
        raise BackpedalArgumentError(e.args[0])

    if item_type == 'both':
        type_log = 'files/directories'
    else:
        type_log = item_type

    log('looking for %s %s' % (type_log, item))
    found = []

    if path is None:
        path = os.curdir

    if direction in ['up', 'both']:
        for cur,dirs,files in up(path):
            if item_type in ['file', 'both'] and item in files:
                    if first_only is True:
                        return os.path.join(cur, item)
                    else:
                        found.append(os.path.join(cur, item))
            elif item_type in ['directory', 'both'] and item in dirs:
                    if first_only is True:
                        return os.path.join(cur, item)
                    else:
                        found.append(os.path.join(cur, item))

    if direction in ['down', 'both']:
        for cur,dirs,files in down(path):
            if item_type in ['file', 'both'] and item in files:
                if first_only is True:
                    return os.path.join(cur, item)
                else:
                    found.append(os.path.join(cur, item))
            if item_type in ['directory', 'both'] and item in dirs:
                if first_only is True:
                    return os.path.join(cur, item)
                else:
                    found.append(os.path.join(cur, item))

    if first_only is True or len(found) == 0:
        return None
    else:
        return [abspath(x) for x in found]
