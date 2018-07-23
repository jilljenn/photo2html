import glob
import os

html = '''
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
div {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
}
img {
    margin: 1em;
}
</style>
'''

if not os.path.isdir('thumb'):
    os.makedirs('thumb')

html += '<div>\n'
for photo in sorted(glob.glob('*.jpg')):
    os.system('convert {:s} -auto-orient -resize 150 thumb/{:s}'.format(photo, photo))
    html += '<a href="{:s}"><img src="thumb/{:s}" /></a>\n'.format(photo, photo)
html += '</div>'

with open('index.html', 'w') as f:
    f.write(html)
