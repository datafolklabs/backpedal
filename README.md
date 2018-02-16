
# Backpedal

It's like `os.walk()`, but backwards... and on a bicycle.

[![Build Status](https://travis-ci.org/datafolklabs/backpedal.svg?branch=master)](https://travis-ci.org/datafolklabs/backpedal)

**Core Features**

- Walk directories up, down, or both directions
- Search for files, directories, or both item types
- Return first item found immediately, or list of all matching items
- 100% Test Coverage (pytest) on Python 2.7, 3.4, 3.5, 3.6
- 100% PEP8 Compliant (pep8, autopep8)

**Motivation**

The primary use case for backpedal is finding files from within your current directory, and/or parent(s).  For example, both Vagrant and Fabric support running from nested sub-directories within a project while loading their associated `Vagrantfile` or `fabfile.py` from the root (parent) project directory by searching from the current directory and upward.

The `walk up` logic was initially garnered from a quick search on Google that produced the following Gist:

- Zach Davis (zdavkeos) - https://gist.github.com/zdavkeos/1098474

Thanks Zach!


## Installation

Stable versions can be installed from [PyPi](https://pypi.python.org/pypi/backpedal):

```
$ pip install backpedal
```


## Documentation

As this is currently a very basic library, all documentation is here in this README. In the feature, as the project grows, more advanced/proper documentation will be added.


### `up(path)`

Walk up from a directory `path`.  If no `path` is given, default to `os.curdir`.  Similar to `os.walk` but in the oposite direction.

**Arguments**

- **path** *(str)*: The starting path to walk up from.

**Usage**

```
import backpedal

for curdir,dirs,files in backpedal.up('/path/to/starting/dir'):
    # do something with results
    pass
```

### `down(path)`

Walk down from a directory `path`.  If no `path` is given, default to `os.curdir`.  This is synonymous with using `os.walk`.

**Arguments**

- **path** *(str)*: The starting path to walk up from.

**Usage**

```
import backpedal

for curdir,dirs,files in backpedal.down('/path/to/starting/dir'):
    # do something with results
    pass
```

### `find(item, ...):`

Search for `files`, `directories`, or `both` item types from the given `path`, in either `up`, `down`, or `both` directions.

**Arguments**:

- **item** *(str)*: A string identifier of the directory or file name to search for.

**Keyword Arguments**:

- **path** *(str)*: The starting path to walk up from.  Defaults to `os.curdir()` if no path is given.
- **direction** *(str)*: The direction to walk (`up`, `down`, or `both`).  Default: `up`.
- **first_only** *(bool)*: Return the first item found (immediately) as a `str`, or return a `list` of all items found.  Default: `True`.
- **item_type** *(str)*: Type of item to search for (`file`, `directory`, or `both`).  Default: `file`
- **regex** *(bool)*: Whether to treat `item` as a regular expression.  Default: `false`
- **ignore** *(list)*: List of regular expressions to filter out matching results.  Note that this is not affected by the `regex` keyword argument...  the `ignore` list is already treated as regex.  Default: `None`.


**Usage**

```
import backpedal

### find a file from current dir, up through all the parents
res = backpedal.find('Vagrantfile')

### find a file or directory, and filter with ignore
res = backpedal.find('README', item_type='both', ignore=['(.*)\.git(.*)'])
```

## Example

From the `example` directory:

```
$ cd example/

$ python example.py

------------------------------------------------------------------------------
Find the first matching file starting from `.`
------------------------------------------------------------------------------
+++ BACKPEDAL // looking for file README.md
+++ BACKPEDAL // backpedaling upward from path: /Users/derks/Development/backpedal/example
RES > /Users/derks/Development/backpedal/example/README.md

------------------------------------------------------------------------------
Find all matching files starting from sub1/a/b/c:
------------------------------------------------------------------------------
+++ BACKPEDAL // looking for file README.md
+++ BACKPEDAL // backpedaling upward from path: /Users/derks/Development/backpedal/example/sub1/a/b/c
+++ BACKPEDAL // backpedaling upward from path: /Users/derks/Development/backpedal/example/sub1/a/b
+++ BACKPEDAL // backpedaling upward from path: /Users/derks/Development/backpedal/example/sub1/a
+++ BACKPEDAL // backpedaling upward from path: /Users/derks/Development/backpedal/example/sub1
+++ BACKPEDAL // backpedaling upward from path: /Users/derks/Development/backpedal/example
+++ BACKPEDAL // backpedaling upward from path: /Users/derks/Development/backpedal
+++ BACKPEDAL // backpedaling upward from path: /Users/derks/Development
+++ BACKPEDAL // backpedaling upward from path: /Users/derks
+++ BACKPEDAL // backpedaling upward from path: /Users
+++ BACKPEDAL // backpedaling upward from path: /
RES > ['/Users/derks/Development/backpedal/example/sub1/a/README.md', '/Users/derks/Development/backpedal/example/README.md', '/Users/derks/Development/backpedal/README.md']

------------------------------------------------------------------------------
Look for directory but peddle down instead of up
------------------------------------------------------------------------------
+++ BACKPEDAL // looking for directory data
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub1
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub1/a
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub1/a/b
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub1/a/b/c
RES > /Users/derks/Development/backpedal/example/sub1/a/b/c/data

------------------------------------------------------------------------------
Look for files and directories in both directions
------------------------------------------------------------------------------
+++ BACKPEDAL // looking for files/directories data
+++ BACKPEDAL // backpedaling upward from path: /Users/derks/Development/backpedal/example
+++ BACKPEDAL // backpedaling upward from path: /Users/derks/Development/backpedal
+++ BACKPEDAL // backpedaling upward from path: /Users/derks/Development
+++ BACKPEDAL // backpedaling upward from path: /Users/derks
+++ BACKPEDAL // backpedaling upward from path: /Users
+++ BACKPEDAL // backpedaling upward from path: /
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub1
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub1/a
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub1/a/b
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub1/a/b/c
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub1/a/b/c/data
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub2
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub2/a
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub2/a/b
+++ BACKPEDAL // backpedaling downward from path: /Users/derks/Development/backpedal/example/sub2/a/b/c
RES > ['/Users/derks/Development/backpedal/example/sub1/a/b/c/data', '/Users/derks/Development/backpedal/example/sub2/data', '/Users/derks/Development/backpedal/example/sub2/a/b/data']
```

## Development and Contributing

### Docker Compose

This project includes a basic Docker Compose setup to make development quick and easy, and is the recommended means of working with the source locally:

```
$ docker-compose up -d

$ docker-compose exec backpedal /bin/ash

app/
```

From within the Docker container, all development requirements are already installed and ready to go.

### VirtualEnv

An alternative setup would be to use VirtualEnv:

```
$ make virtualenv

$ source env/bin/activate

|> backpedal <| $
```

### Run Tests

```
$ make test
```


### Check PEP8 Compliance

```
$ make comply
```

And, fix PEP8 issues:

```
$ make comply-fix
```
