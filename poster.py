import drawbot_skia.drawbot as db


doc_width = 1604.5
doc_height = 1967.2

db.size(doc_width, doc_height)

colors = db.image('colors/30012021.jpg', (0, 0))
trame = db.image('trames/30012021.jpg', (0, doc_height/2))
blob = db.image('shapes/30012021.jpg', (doc_width/2, 0))
image = db.image('images/30012021.jpg', (doc_width/2, doc_height/2))

db.saveImage('poster.jpg')
