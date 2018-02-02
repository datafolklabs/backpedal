
import os
import re
from pytest import raises
from backpedal import log, abspath, up, down, find, BackpedalArgumentError


def test_log(tmp):
    global DEBUG
    DEBUG = True
    os.environ['BACKPEDAL_DEBUG'] = '1'
    log('this is a test message')


def test_up(tmp):
    for curdir, dirs, files in up('tests/data/sub1'):
        print("CURDIR: %s" % curdir)
        assert os.path.isdir(curdir)

        for d in dirs:
            full_path = os.path.join(curdir, d)
            assert os.path.isdir(full_path)
        for f in files:
            full_path = os.path.join(curdir, f)
            assert os.path.isfile(full_path)

        # lets avoid issues with going up out of our source dir
        if re.match('^(.*)tests$', curdir):
            break

    # if path is None, then it defaults to curdir so lets test that
    for curdir, dirs, files in up():
        assert abspath(curdir) == abspath(os.curdir)
        break


def test_down(tmp):
    for curdir, dirs, files in down('tests/data/sub1'):
        assert os.path.isdir(curdir)

        for d in dirs:
            full_path = os.path.join(curdir, d)
            assert os.path.isdir(full_path)
        for f in files:
            full_path = os.path.join(curdir, f)
            assert os.path.isfile(full_path)

    # if path is None, then it defaults to curdir so lets test that
    for curdir, dirs, files in down():
        assert abspath(curdir) == abspath(os.curdir)
        break


def test_find(tmp):
    res = find('README.md')
    assert re.match('(.*)README.md', res)


def test_find_direction(tmp):
    # direction up
    res = find('README.md', direction='up', path='tests/data/sub1/a')
    assert re.match('(.*)data/sub1/a/README.md', res)

    # direction down
    res = find('README.md', direction='down', path='tests/data')
    assert re.match('(.*)data/sub1/a/README.md', res)

    # direction both
    res = find('README.md', direction='both', path='tests/data')
    assert re.match('(.*)README.md', res)

    # direction bogus (raises error)
    msg = "Argument 'direction' must be one of"
    with raises(BackpedalArgumentError, match=msg):
        res = find('README.md', direction='bogus')


def test_find_first_only(tmp):
    # first_only True
    res = find('README.md', first_only=True, path='tests/data/sub1/a')
    assert re.match('(.*)data/sub1/a/README.md', res)

    # first_only False
    res = find('README.md', first_only=False, path='tests/data/sub1/a')
    assert isinstance(res, list)
    for path in res:
        assert re.match('(.*)README.md', path)

    # first_only bogus
    msg = "Argument 'first_only' must be one of"
    with raises(BackpedalArgumentError, match=msg):
        res = find('README.md', first_only='bogus')


def test_find_item_type(tmp):
    # item_type file
    res = find('data', item_type='file', direction='both', path='tests/')
    assert os.path.isfile(res)

    # item_type directory
    res = find('data', item_type='directory', direction='both', path='tests')
    assert os.path.isdir(res)

    # item_type both
    res = find('data', item_type='both', first_only=False, direction='both',
               path='tests')

    found_a_file = False
    found_a_dir = False
    for item in res:
        if os.path.isfile(item):
            found_a_file = True
        elif os.path.isdir(item):
            found_a_dir = True

    assert found_a_file
    assert found_a_dir

    # same thing with first_only true (coverage)
    res = find('data', item_type='both', first_only=True, direction='down',
               path='tests/')

    # direction bogus (raises error)
    msg = "Argument 'item_type' must be one of"
    with raises(BackpedalArgumentError, match=msg):
        res = find('data', item_type='bogus')


def test_find_none(tmp):
    res = find('bogus_file_does_not_exist')
    assert res is None
