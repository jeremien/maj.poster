from flat import document, image, shape, font, strike
import os
from PIL import Image


base_path = 'src/'

doc_width = 802.2
doc_height = 983.6
doc_marge_w = 60
doc_marge_h = 40
doc_gout = 15

layout_width = (doc_width - (doc_marge_w * 2))
layout_height = (doc_height - (doc_marge_h * 2))

sepX = 3
sepY = 6
cell_width = layout_width/sepX
cell_height = layout_height/sepY
img_width = cell_width - doc_gout

eli_heuer_txt = "Captures d'écran du compte Twitter \nd'Eli Heuer du 1er avril au 26 juin 2020 (Twitter.com/eliheuer)\n© Eli Heuer/Twitter."
typeface_as_program_txt = "Impression de la première version du caractère Programme sur une presse typographique, par David Keshavjee \net Julien Tavelli, 2009 (Optimo.ch/typefaces/programme)\n© David Keshavjee et Julien Tavelli."
osp_txt = "Création typographique sur FontForge par Open Source Publishing pour la communication 2020-2021 \ndu théâtre Balsamine, 2020 (Osp.kitchen/work/balsamine.2020-2021)\n© OSP/Free Art License version 1.3/Attribution ShareAlike Creative Commons BY-SA."
catalogtree_txt = "Dispositif et prototypage pour la réalisation du projet *Structured Light* par Catalogtree, 2010 (Catalogtree.net/projects/structured_light)\n© Catalogtree."
jurg_lehni_txt = "*Hektor Draws a Landscape* & *Hektor Titles a Show*, « Lee 3 Tau Ceti Central Armory Show », Villa Arson, Nice, Villa Arson, Nice, 2003 et « Design and the Elastic Mind », MoMA New York, Jürg Lehni, 2008. (Juerglehni.com/works/hektor)\n© Jürg Lehni & Uli Franke, 2002/Jürg Lehni & Alex Rich, 2003."

explication_txt = "La mise en page de ce poster a été réalisée selon les principes exposés dans l'article au recto, \
en utilisant trois bibliothèques du langage Python pour la typographie et le traitement des images : \
\nLa première bibliothèque est une version alpha de Drawbot, adaptée à la librairie graphique Skia \
pour une utilisation sur différents systèmes d'exploitation par Just Van Rossum (pypi.org/project/drawbot-skia). \
\nLa deuxième bibliothèque, Flat (xxyxyz.org) de Juraj Sukop, ne semble toutefois plus maintenue depuis 2018. \
\nLa troisième bibliothèque, Pillow, est très utilisée (pillow.readthedocs.io) dans le domaine du traitement d'image. \
\nLe code qui a permis la réalisation de ce poster est disponible à l'adresse : github.com/jeremien/maj.poster."

regular = font.open('font/PlantinMTProRg.TTF')
bold = font.open('font/Erbarre-Bold.otf')
body = strike(regular).size(10)
titre = strike(bold).size(13)

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
          name = path + entry.name
          try:
            im = Image.open(name).convert('CMYK')
            print(im.mode)
            im.save(
              name,
              resolution=300.0,
              quality=100
            )
          except IOError:
            print('error pillow')
            continue

          try:
            im = image.open(name)
            images.append(im)
          except ValueError:
            print('error flat')
            continue
      except FileNotFoundError:
          continue
  print(images)
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
        p.place(titre.text('Figures 1 et 2.')).frame(g[0][i-1][0],doc_marge_h + doc_gout,cell_width,cell_height)
        p.place(body.text(eli_heuer_txt)).frame(g[0][i-1][0] + 70,doc_marge_h + doc_gout,cell_width-doc_marge_w,cell_height)
  
  elif j == 1:
    for i in range(sepX):
      if i == 0:
        p.place(typeface_as_program_img[i]).position(doc_marge_w, g[1][j-1][1] - doc_gout).fitwidth(img_width)
      elif i < 2:
        p.place(typeface_as_program_img[i]).position(g[0][i-1][0], g[1][j-1][1] - doc_gout).fitwidth(img_width)
      else:
        p.place(titre.text('Figures 3 et 4.')).frame(g[0][i-1][0], g[1][j-1][1],cell_width,cell_height)
        p.place(body.text(typeface_as_program_txt)).frame(g[0][i-1][0] + 70, g[1][j-1][1],cell_width - 40,cell_height)

  elif j == 2:
    for i in range(sepX):
      if i == 0:
        p.place(osp_img[i]).position(doc_marge_w, g[1][j-1][1] + doc_gout).fitwidth(img_width)
      elif i < 2:
        p.place(osp_img[i]).position(g[0][i-1][0], g[1][j-1][1] + doc_gout).fitwidth(img_width)
      else:
        p.place(titre.text('Figures 5 et 6.')).frame(g[0][i-1][0], g[1][j-1][1] + doc_gout * 2,cell_width,cell_height)
        p.place(body.text(osp_txt)).frame(g[0][i-1][0] + 70,g[1][j-1][1] + doc_gout * 2,cell_width - 50,cell_height)

  elif j == 3:
    for i in range(sepX):
      if i == 0:
        p.place(catalogtree_img[i]).position(doc_marge_w, g[1][j-1][1] + doc_gout).fitwidth(img_width)
      elif i < 2:
        p.place(catalogtree_img[i]).position(g[0][i-1][0], g[1][j-1][1] + doc_gout).fitwidth(img_width)
      else:
        p.place(titre.text('Figures 7 et 8.')).frame(g[0][i-1][0], g[1][j-1][1] + doc_gout * 2,cell_width,cell_height)
        p.place(body.text(catalogtree_txt)).frame(g[0][i-1][0] + 70,g[1][j-1][1] + doc_gout * 2,cell_width - 40,cell_height)

  elif j == 4:
    for i in range(sepX):
      if i == 0:
        p.place(jurg_lehni_img[i]).position(doc_marge_w, g[1][j-1][1] + doc_gout * 3).fitwidth(img_width)
      elif i < 2:
        p.place(jurg_lehni_img[i]).position(g[0][i-1][0], g[1][j-1][1] + doc_gout * 3).fitwidth(img_width)
      else:
        p.place(titre.text('Figures 9 et 10.')).frame(g[0][i-1][0], g[1][j-1][1] + doc_gout * 4,cell_width,cell_height)
        p.place(body.text(jurg_lehni_txt)).frame(g[0][i-1][0] + 70,g[1][j-1][1] + doc_gout * 4,cell_width - 40,cell_height)

p.place(s.width(0.5).line(doc_marge_w - 20, doc_marge_h , doc_marge_w - 20, doc_height - doc_marge_h))
p.place(body.text(explication_txt)).frame(doc_marge_w, doc_height - (cell_height - doc_gout * 2),cell_width*2.5,cell_height)

unique_id = 'icono'
d.meta(unique_id).pdf('pdf/' + unique_id + '.pdf', compress=False, bleed=False, cropmarks=False)