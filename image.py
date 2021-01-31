import pathlib
import drawbot_skia.drawbot as db
import datetime
from PIL import Image

# date
dt = datetime.datetime.today()
name = 'image_' + dt.strftime("%d%m%Y")

p = pathlib.Path(__file__).parent.absolute()

pw = 802.2
ph = 983.6
u = 5
m = u*4
wdt = 120

h = ph/5
w = pw/2

path = '9ad1c366-6224-11eb-896c-e46f13f48499.jpg'

db.size(pw, ph)

def cross(x, y):
  with db.savedState():
    db.fill(None)
    db.stroke(0)
    db.strokeWidth(1)
    db.translate(x, y)
    # line vertical
    db.line((u*2,0), (u*2,u*4))
    # line horizontale
    db .line((0,u*2), (u*4,u*2))


im = Image.open(path)
w,h = im.size
print(w, h)
im = im.resize((int(w/8), int(h/8)))
w,h = im.size
print(w, h)
im.save('image.jpg')
fw = (pw - w)/2
fh = (ph - h)/2
print(fw, fh)
db.image('image.jpg', (fw, fh))

# text
db.stroke(None)
db.fill(0)
db.font("Plantin MT Pro", 11)
db.text("Une image composée des canaux RVB issus de trois images différentes", (m*2, m*3))

# croix
cross(m, m)
cross((pw - m*2), m)
cross(m, (ph - m*2))
cross((pw - m*2), (ph - m*2))

db.saveImage(str(name) + '.jpg')
#db.saveImage(str(name) + '.svg')
db.saveImage(str(name) + '.pdf')