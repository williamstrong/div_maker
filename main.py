import os
direc = input("Directory to check? ")

# Get directory to pull images from
f = []

for subdir, dirs, files in os.walk(direc):
    for file in files:
        f.append(os.path.join(subdir, file))

# print(f)

# Get size and create list of name and sizes
from PIL import Image

files_and_size = []

for i in f:
    if i.endswith('.PNG'):
        with Image.open(i) as img:
            width, height = img.size
            # print(width, height)
        # Create list of name and sizes
        files_and_size.append([i, [width, height]])
    else:
        f.remove(i)

# print(files_and_size)

divs = []
css = []

# Create div tag and styles
for i in files_and_size:
    fn = os.path.split(i[0])[1]
    div = '<div id="%s"></div>\n' % fn
    style = '#%s {\n\theight: %dpx;\n\twidth: %dpx;\n}\n' % (fn, i[1][0], i[1][1])

    divs.append(div)
    css.append(style)

# print(divs)
# print(css)

# Write to files
with open('/Users/williamstrong/test.txt', 'w') as file:
    for i in divs:
        file.write(i)
        print(i)
        print('wrote')

with open('/Users/williamstrong/test.css', 'w') as file:
    for i in css:
        file.write(i)
# for i in divs:
