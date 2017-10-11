
# Backpedal

It's like `os.walk`, but backwards... and on a bicycle.

## Motivation?

The primary use case for Backpedal is finding files from within your current directory, and/or parent(s).  For example, both Vagrant and Fabric support running from nested sub-directories within a project while loading their associated `Vagrantfile` of `fabfile.py` from the root (parent) project directory by searching from the current directory and upward.

## Contributors

The `walk up` logic was initially garnered from a quick search on Google that produced the following Gist:

- Zach Davis (zdavkeos) - https://gist.github.com/zdavkeos/1098474


Thanks Zach!


## Usage

```python
import backpedal

### find a file from current dir, up through all the parents
res = backpedal.find('Vagrantfile')

### use like os.walk
for curdir,dirs,files in backpedal.up('/path/to/starting/point'):
    pass

for curdir,dirs,files in backpedal.down('/path/to/starting/point'):
    pass
```

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
