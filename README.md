# photo2html
Make an album without using any external service. Creates a static page with flexbox.

## Requirements

- Python 3 or 2.7
- ImageMagick
    - `brew install imagemagick`
    - `apt-get install ghostscript imagemagick`

## Install

Put `run.py` in the folder containing your photos, then:

    python run.py

It will create an `index.html` page, and a `thumb` folder containing all thumbnails.

*Note.* The current version of the code assumes your photos have `.jpg` extension (not uppercase). If not, please change the `glob` filter.

## Useful links

- [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- Two useful Stack Overflow posts:
    - [iOS Image Orientation has Strange Behavior](https://stackoverflow.com/questions/10600613/ios-image-orientation-has-strange-behavior)
    - [](https://stackoverflow.com/questions/12026441/is-there-a-way-to-tell-browsers-to-honor-the-jpeg-exif-orientation)

Long story short: sometimes, images are displayed in landscape instead of portrait in browsers. It is because some phones (ex. iPhone) use the Orientation EXIF metadata, which is [ignored by browsers](https://stackoverflow.com/questions/12026441/is-there-a-way-to-tell-browsers-to-honor-the-jpeg-exif-orientation) unless you have `image-orientation: from-image` which is [only recognized by Firefox so far](https://developer.mozilla.org/en-US/docs/Web/CSS/image-orientation#Browser_compatibility).  
ImageMagick saved us, by using the flag `-auto-orient` for creating the thumbnails.

## Next steps (please open PRs!)

- Get valid HTML5 code 😇
- Provide a better default flexbox configuration (= tweak the magic numbers so that any phone has at least two columns of pictures)
- Use [fancybox](http://fancyapps.com/fancybox/3/). Vanilla JS responsive alternatives are welcome.

## Authors

[Jill-Jênn Vie](https://jilljenn.github.io) & [Sam Vie](http://sakiut.fr)
