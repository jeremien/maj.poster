import pathlib
import drawbot_skia.drawbot as db
import datetime, random, math

# date
dt = datetime.datetime.today()
name = 'shape_' + dt.strftime("%d%m%Y")

pw = 802.2
ph = 983.6
u = 5
m = u*4

randomPhases = [(2 * math.pi * db.random(), db.choice([-1, 1])) for i in range(3)]
nBlobs = 30

db.size(pw, ph)

def varyPoint(pt, radius, phase):
  x, y = pt
  dx = radius * db.cos(phase)
  dy = radius * db.sin(phase)
  return x + dx, y + dy

def drawShape(radius):
  points = []
  for i in range(3):
    a = 2 * math.pi * i / 3
    x = radius * db.cos(a)
    y = radius * db.sin(a)
    rPhase, rSign = randomPhases[i]
    print(rPhase, rSign)
    points.append(varyPoint((x, y), 0.2 * radius, rPhase + rSign * 2 * math.pi))

  points.append(None)
  bezPath = db.BezierPath()
  bezPath.qCurveTo(*points)
  bezPath.closePath()
  db.drawPath(bezPath)

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

# cross
cross(m, m)
cross((pw - m*2), m)
cross(m, (ph - m*2))
cross((pw - m*2), (ph - m*2))

# text
db.stroke(None)
db.fill(0)
db.font("Plantin MT Pro", 11)
db.text("Une forme molle rouge dessinée à partir de trois points", (m*2, m*3))


db.translate(pw/2, ph/2)
db.stroke(None)
db.fill(1,0,0)

# draw a unique shape
drawShape(pw * 0.5)

# central cross
cross(m, m)

db.saveImage(str(name) + '.jpg')
db.saveImage(str(name) + '.pdf')
