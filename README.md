
# Backpeddle

It's like `os.walk`, but backwards... and on a bicycle.

## Motivation?

The primary use case for Backpeddle is finding files from within your current directory, and/or parent(s).  For example, both Vagrant and Fabric support running from nested sub-directories within a project while loading their associated `Vagrantfile` of `fabfile.py` from the root (parent) project directory by searching from the current directory and upward.

## Contributors

The `walk up` logic was initially garnered from a quick search on Google that produced the following Gist:

- Zach Davis (zdavkeos) - https://gist.github.com/zdavkeos/1098474


Thanks Zach!


## Usage

```python
import backpeddle

### find a file from current dir, up through all the parents
res = backpeddle.find('Vagrantfile')

### use like os.walk
for curdir,dirs,files in backpeddle.up('/path/to/starting/point'):
    pass

for curdir,dirs,files in backpeddle.down('/path/to/starting/point'):
    pass
```

From the `example` directory:

```
$ cd example/

$ python example.py

------------------------------------------------------------------------------
Find the first matching file starting from `.`
------------------------------------------------------------------------------
+++ BACKPEDDLE // looking for file README.md
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks/Development/backpeddle/example
RES > /Users/derks/Development/backpeddle/example/README.md

------------------------------------------------------------------------------
Find all matching files starting from sub1/a/b/c:
------------------------------------------------------------------------------
+++ BACKPEDDLE // looking for file README.md
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks/Development/backpeddle/example/sub1/a/b/c
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks/Development/backpeddle/example/sub1/a/b
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks/Development/backpeddle/example/sub1/a
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks/Development/backpeddle/example/sub1
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks/Development/backpeddle/example
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks/Development/backpeddle
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks/Development
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks
+++ BACKPEDDLE // backpeddling upward from path: /Users
+++ BACKPEDDLE // backpeddling upward from path: /
RES > ['/Users/derks/Development/backpeddle/example/sub1/a/README.md', '/Users/derks/Development/backpeddle/example/README.md', '/Users/derks/Development/backpeddle/README.md']

------------------------------------------------------------------------------
Look for directory but peddle down instead of up
------------------------------------------------------------------------------
+++ BACKPEDDLE // looking for directory data
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub1
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub1/a
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub1/a/b
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub1/a/b/c
RES > /Users/derks/Development/backpeddle/example/sub1/a/b/c/data

------------------------------------------------------------------------------
Look for files and directories in both directions
------------------------------------------------------------------------------
+++ BACKPEDDLE // looking for files/directories data
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks/Development/backpeddle/example
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks/Development/backpeddle
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks/Development
+++ BACKPEDDLE // backpeddling upward from path: /Users/derks
+++ BACKPEDDLE // backpeddling upward from path: /Users
+++ BACKPEDDLE // backpeddling upward from path: /
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub1
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub1/a
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub1/a/b
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub1/a/b/c
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub1/a/b/c/data
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub2
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub2/a
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub2/a/b
+++ BACKPEDDLE // backpeddling downward from path: /Users/derks/Development/backpeddle/example/sub2/a/b/c
RES > ['/Users/derks/Development/backpeddle/example/sub1/a/b/c/data', '/Users/derks/Development/backpeddle/example/sub2/data', '/Users/derks/Development/backpeddle/example/sub2/a/b/data']
```
