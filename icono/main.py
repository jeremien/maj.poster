from flat import document, image, shape, font, strike
import os

base_path = 'src/'

doc_width = 802.2
doc_height = 983.6
doc_marge_w = 40
doc_marge_h = 40
doc_gout = 15

layout_width = (doc_width - (doc_marge_w * 2))
layout_height = (doc_height - (doc_marge_h * 2))

sepX = 3
sepY = 6
cell_width = layout_width/sepX
cell_height = layout_height/sepY
img_width = cell_width - doc_gout

eli_heuer_txt = "Figures 1 à 2. Captures d'écran du compte twitter d'Eli Heuer du 01 avril au 26 juin 2020 (twitter.com/eliheuer)."
typeface_as_program_txt = "Figures 3 à 4. Impression de la première version du caractère Programme sur une presse typographique en 2009, par David Keshavjee et Julien Tavelli."
osp_txt = "Figures 5 à 6. Création typographique chez OSP sur FontForge pour la communcation 2020-2021 du théatre Balsamine (osp.kitchen/work/balsamine.2020-2021)."
catalogtree_txt = "Figures 7 à 8. Dispositif et prototypage pour la réalistion du projet Structured Light en 2010 (www.catalogtree.net/projects/structured_light)."
jurg_lehni_txt = "Figures 9 à 10. Le dispositif de dessin paramétrique Hektor en 2003 et 2008 (juerglehni.com/works/hektor)"

explication_txt = "hello"

regular = font.open('font/PlantinMTProRg.TTF')
body = strike(regular).size(11)

d = document(doc_width, doc_height, 'pt')
p = d.addpage()
s = shape()

def setImages(folder: str) -> list:
  images = []
  path = base_path + folder + '/'
  with os.scandir(path) as entries:
    for entry in entries:
      try:
        if entry.is_file():
          im = image.open(path + entry.name)
          images.append(im)
      except FileNotFoundError:
          continue
  return images

def grid() -> list:

  data = []
  posX = cell_width + doc_marge_w
  posY = cell_height + doc_marge_h

  x_data = []
  y_data = []

  for x in range(sepX):
    x_data.append((posX, posY))
    posX += cell_width

  for y in range(sepY):
    y_data.append((posX, posY))
    posY += cell_height

  data.append(x_data)
  data.append(y_data)

  return data

eli_heuer_img = setImages('eli_heuer')
typeface_as_program_img = setImages('typeface_as_program')
osp_img = setImages('osp')
catalogtree_img = setImages('catalogtree')
jurg_lehni_img = setImages('jurg_lehni')

g = grid()

for j in range(sepY):
  if j == 0:
    for i in range(sepX):
      if i == 0:
        p.place(eli_heuer_img[i]).position(doc_marge_w, doc_marge_h).fitwidth(img_width)
      elif i < 2:
        p.place(eli_heuer_img[i]).position(g[0][i-1][0], doc_marge_h).fitwidth(img_width)
      else:
        p.place(body.text(eli_heuer_txt)).frame(g[0][i-1][0],doc_marge_h,cell_width,cell_height)
  
  elif j == 1:
    for i in range(sepX):
      if i == 0:
        p.place(typeface_as_program_img[i]).position(doc_marge_w, g[1][j-1][1]).fitwidth(img_width)
      elif i < 2:
        p.place(typeface_as_program_img[i]).position(g[0][i-1][0], g[1][j-1][1]).fitwidth(img_width)
      else:
        p.place(body.text(typeface_as_program_txt)).frame(g[0][i-1][0],g[1][j-1][1],cell_width,cell_height)

  elif j == 2:
    for i in range(sepX):
      if i == 0:
        p.place(osp_img[i]).position(doc_marge_w, g[1][j-1][1]+doc_gout).fitwidth(img_width)
      elif i < 2:
        p.place(osp_img[i]).position(g[0][i-1][0], g[1][j-1][1]+doc_gout).fitwidth(img_width)
      else:
        p.place(body.text(osp_txt)).frame(g[0][i-1][0],g[1][j-1][1]+doc_gout,cell_width,cell_height)

  elif j == 3:
    for i in range(sepX):
      if i == 0:
        p.place(catalogtree_img[i]).position(doc_marge_w, g[1][j-1][1]).fitwidth(img_width)
      elif i < 2:
        p.place(catalogtree_img[i]).position(g[0][i-1][0], g[1][j-1][1]).fitwidth(img_width)
      else:
        p.place(body.text(catalogtree_txt)).frame(g[0][i-1][0],g[1][j-1][1],cell_width,cell_height)

  elif j == 4:
    for i in range(sepX):
      if i == 0:
        p.place(jurg_lehni_img[i]).position(doc_marge_w, g[1][j-1][1]+doc_gout).fitwidth(img_width)
      elif i < 2:
        p.place(jurg_lehni_img[i]).position(g[0][i-1][0], g[1][j-1][1]+doc_gout).fitwidth(img_width)
      else:
        p.place(body.text(jurg_lehni_txt)).frame(g[0][i-1][0],g[1][j-1][1]+doc_gout,cell_width,cell_height)


p.place(body.text(explication_txt)).frame(doc_marge_w,doc_height-cell_height,cell_width,cell_height)

unique_id = 'poster'
d.meta(unique_id).pdf('pdf/' + unique_id + '.pdf', compress=False, bleed=False, cropmarks=False)