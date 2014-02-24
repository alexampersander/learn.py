i = 5
print (i)
i = i + 1
print (i)

s = '''This is a multi-line string.
This is the second line.'''
print (s)

'''
Multi line strings can be used as multi line comments, apparently.

I don't know if this is recommended or not, but it kind of annoys me
because Sublime Text still highlights it as a string (as it should).

Semicolons can be used, but it's not recommended to do so.
One physical line per logical line seems to be easily readable, too.
'''

print (s); print (i);
# Or just
print (s); print (i)
#Or the recommented
print (s)
print (i)

s = 'This is a string. \
This continues the string. \
All on the same line.'
print (s)