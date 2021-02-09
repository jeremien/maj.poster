import drawbot_skia.drawbot as db


doc_width = 1604.5
doc_height = 1967.2

db.size(doc_width, doc_height)

colors = db.image('colors_01022021.jpg', (0, 0))
trame = db.image('trame_01022021.jpg', (0, doc_height/2))
blob = db.image('shape_01022021.jpg', (doc_width/2, 0))
image = db.image('image_01022021.jpg', (doc_width/2, doc_height/2))

db.saveImage('poster.jpg')
