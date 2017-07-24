
import backpeddle
backpeddle.DEBUG = True

def log(msg):
    print()
    print('-' * 78)
    print(msg)
    print('-' * 78)

log('Find the first matching file starting from `.`')
res = backpeddle.find('README.md')
print('RES > %s' % res)

log('Find all matching files starting from sub1/a/b/c:')
res = backpeddle.find('README.md', path='sub1/a/b/c', first_only=False)
print('RES > %s' % res)

log('Look for directory but peddle down instead of up')
res = backpeddle.find('data', direction='down', item_type='directory')
print('RES > %s' % res)

log('Look for files and directories in both directions')
res = backpeddle.find('data', direction='both', item_type='both', first_only=False)
print('RES > %s' % res)
