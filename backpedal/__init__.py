
import os
import re


class BackpedalArgumentError(Exception):
    pass


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

    log('backpedaling downward from path: %s' % path)

    # directories and files in this path
    items = os.listdir(path)
    dirs, files = [], []

    for item in items:
        if os.path.isdir(os.path.join(path, item)):
            if item not in dirs:
                dirs.append(item)
        else:
            if item not in files:
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

    log('backpedaling upward from path: %s' % path)

    # directories and files in this path
    items = os.listdir(path)
    dirs, files = [], []

    for item in items:
        if os.path.isdir(os.path.join(path, item)):
            if item not in dirs:
                dirs.append(item)
        else:
            if item not in files:
                files.append(item)

    yield path, dirs, files

    next_path = abspath(os.path.dirname(path))

    # stop when we hit the top
    if next_path == path:
        return

    # iterate
    for x in up(next_path):
        yield x


def _ignored(path, ignore):
    # we do this here because we want regex to match
    # the full path
    if ignore is None or len(ignore) == 0:
        return False

    else:
        for ignore_regex in ignore:
            if re.match(ignore_regex, path):
                return True

    return False


def find(item, path=None, **kwargs):
    direction = kwargs.get('direction', 'up')
    first_only = kwargs.get('first_only', True)
    item_type = kwargs.get('item_type', 'file')
    ignore = kwargs.get('ignore', None)
    regex = kwargs.get('regex', False)
    found = []
    if path is None:
        path = os.curdir

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

    if direction == 'both':
        d_funcs = [up, down]
    elif direction == 'up':
        d_funcs = [up]
    elif direction == 'down':
        d_funcs = [down]

    # iterate over our direction functions (same logic, different direction)
    for d_func in d_funcs:
        for cur, dirs, files in d_func(path):
            # determine which lists to search in based on item_type
            if item_type == 'file':
                search_in = [files]
            elif item_type == 'directory':
                search_in = [dirs]
            elif item_type == 'both':
                search_in = [files, dirs]

            # iterate over each list we need to search in
            for search_list in search_in:

                # if regex then iterate over each item in the search_list
                # and match (expensive!)
                if regex is True:
                    for x in search_list:
                        full_path = os.path.join(cur, x)

                        if _ignored(full_path, ignore):
                            pass

                        elif re.match(item, x) and first_only is True:
                            return full_path

                        elif re.match(item, x):
                            if full_path not in found:
                                found.append(full_path)

                # if no regex then just test that the item is in the list
                # note that regex is always used for ignore list
                else:
                    full_path = os.path.join(cur, item)

                    if _ignored(full_path, ignore):
                        pass
                    elif item in search_list and first_only is True:
                        return full_path
                    elif item in search_list:
                        full_path = os.path.join(cur, item)
                        if full_path not in found:
                            found.append(full_path)

    if first_only is True or len(found) == 0:
        return None
    else:
        return [abspath(x) for x in found]
