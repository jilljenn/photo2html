from string import Template
import glob
import os

if not os.path.isdir('thumb'):
    os.makedirs('thumb')

photos = '<div>\n'
for photo in sorted(glob.glob('*.jpg')):
    os.system('convert {:s} -auto-orient -resize 150 thumb/{:s}'.format(photo, photo))
    photos += '<a href="{:s}"><img src="thumb/{:s}" /></a>\n'.format(photo, photo)
photos += '</div>'

with open('index.tpl.html') as f:
    t = Template(f.read())
with open('index.html', 'w') as f:
    f.write(t.substitute(photos=photos))
