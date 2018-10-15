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

all_photos = sorted(glob.glob('*.jpg'))
not_in_thumb = []

if not os.path.isdir('thumb'):
    os.makedirs('thumb')
else:
	thumb = os.popen("ls thumb/").read().splitlines()
	not_in_thumb = [photo for photo in all_photos if not photo in thumb]

html += '<div>\n'

for photo in not_in_thumb:
	os.system('convert {:s} -auto-orient -resize 150 thumb/{:s}'.format(photo, photo))

for photo in all_photos:
    html += '<a href="{:s}"><img src="thumb/{:s}" /></a>\n'.format(photo, photo)
html += '</div>'

with open('index.html', 'w') as f:
    f.write(html)
