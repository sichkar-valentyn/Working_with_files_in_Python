
# Possible modes to open file with:
# r (read) - open for reading (by default)
# w (write) - open to write, all information in the file will be deleted
# a (append) - open to write, writing will be done at the end
# b (binary) - open in a binary mode
# t (text) - open in the text mode (by default)
# r+ - open for reading and writing
# w+ - open for reading and writing, all information will be deleted

# Opening file for reading
f = open('test.txt', 'r')
# Reading first 5 symbols from the file
x = f.read(5)
print(x)
# Reading file till the end
y = f.read()
print(y)
# Showing the y as the representation of line type
print(repr(y))
# Method to split the information from the file to the different lines
y = y.splitlines()
print(y)
# Closing the file
f.close()


# Opening file for reading
f = open('test.txt', 'r')
# Reading just one line from the file
z = f.readline()
z = z.rstrip()  # Deleting the right symbol to move for the next line
print(repr(z))
# Reading the second line
z = f.readline().strip()  # Another way how to delete symbol to move for the next line
print(repr(z))
# Closing the file
f.close()


# Opening file for reading
f = open('test.txt', 'r')
# Reading lines one by one using loop
for line in f:
    line = line.rstrip()
    print(repr(line))

# When everything is read already from the file
# The last try will give the empty string
x = f.read()
print(repr(x))

# Closing the file
f.close()


# Opening file for writing
# If the file doesn't exist, it will be created
f = open('test_w.txt', 'w')
# Writing the line into the file
f.write('Hello!\n')  # We use here the \n to move to the next line
f.write('World!\n\n')

# Another way to write lines in the file in separate rows
lines = ['Line1', 'Line2', 'Line3']
content = '\n'.join(lines)  # We use .join and say that symbol \n has to be places between lines
f.write(content)

# Closing the file
f.close()


# Opening file for appending
# If the file doesn't exist, it will be created
f = open('test_a.txt', 'a')
f.write('Hello!\n')  # Each time we will run this code it will append new info in the file

# Closing the file
f.close()


# Another and recommended way to open file and close it automatically
with open('test.txt') as f:
    for line in f:
        line = line.rstrip()
        print(line)

# Here file will be already closed

# It is possible to open several files at the same time
with open('test.txt') as f, open('test_copy.txt', 'w') as w:
    for line in f:
        w.write(line)  # Copying all info from file f to w


# Implementing the task
# there is a file with some amount of lines
# It is needed to create the copy of this file but with opposite order of the lines in it
with open('test.txt') as f, open('test_copy.txt', 'w') as w:
    lst = []
    # Reading all the lines and putting them into the list
    for line in f:
        lst += [line.rstrip()]

    # Reordering the elements of the list in reverse direction
    lst = lst[::-1]

    # Joining all the elements from the list with the symbol \n
    content = '\n'.join(lst)
    # Writing the information into the copy file
    w.write(content)


# Using os and os.path while working with files
import os
import os.path

# Showing all files and directories in the current folder
print(os.listdir())

# Getting the current directory
print(os.getcwd())
# Changing the current directory
os.chdir('tensorflow')
print(os.getcwd())
# Changing back the directory in one level upper
os.chdir('..')
print(os.getcwd())

# Showing the files in the specific directory
print(os.listdir('tensorflow'))

# Checking if the file exists
print(os.path.exists('test.txt'))
print(os.path.exists('tensorflow'))

# Checking if the path is the file
print(os.path.isfile('test.txt'))
print(os.path.isfile('tensorflow'))

# Checking if the file is the directory
print(os.path.isdir('test.txt'))
print(os.path.isdir('tensorflow'))

# Getting the absolute path to the file
print(os.path.abspath('test.txt'))


# Using os.walk for going through all directories and files in them from thr current directory
for current_dir, dirs, files in os.walk('.'):  # Fullstop here means the current directory
    print(current_dir, dirs, files)


# Using shutil for copying the files and directories
import shutil

# Copying the file
shutil.copy('test.txt', 'test_test.txt')

# Copying the directory
#shutil.copytree('tensorflow', 'tensorflow_copy')


# Implementing the task
# Reading the directory and all sub-directories
# And showing only that directories which contain the .py files
# Also, sorting the results in lexicographical order
lst = []
for current_dir, dirs, files in os.walk('main'):
    for x in files:
        if '.py' in x:
            lst += [current_dir]
            break

# Sorting the resulted list
lst.sort()

# Preparing data for writing
content = '\n'.join(lst)

# Writing in the file
f = open('results.txt', 'w')
f.write(content)
f.close()

