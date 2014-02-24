age = 14
name = 'Alex'

print ('{0} was {1} years old when he first started reading this book.'.format(name, age))
print ('Why is {0} playing with that python?'.format(name))

# Custom end parameter (blank instead of the default "\n")
print ('a', end='')
print ('b', end='')

print ('') # this is just to add a newline

# Escape sequences
print ('What\'s your name?')
print ("C:\\Program Files (x86)\\Steam\\") # You have to escape backslashes if not using raw string

print ("Hello, this is Line #1.\nAnd this is Line #2.")

print (r"Newlines start with \n. This is not a new line.") # Raw string