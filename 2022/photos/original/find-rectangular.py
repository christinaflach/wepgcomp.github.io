# Prints the names of all photos that
# have a rectangular aspect ratio
from pathlib import Path
from PIL import Image

for path in Path('.').glob('*'):
    try:
        im = Image.open(path)
        width, height = im.size
        if width != height:
            print(path, end=' ')
    except:
        pass
print()