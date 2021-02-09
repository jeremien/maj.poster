from PIL import Image
import os, random, uuid, pprint

base_path = 'src/'

def read_img(img_path: str, mode: str) -> tuple:
  """
  Read file image and return a tupple with each channels

  Args:
      img_path (str): path to the image

  Returns:
      tupple : each CMYK channels
  """
  img = Image.open(img_path).convert(mode)
  return img.split()


def removeDuplicates(lst:list) -> list: 
  """
  Remove duplicate tuple in list

  Args:
      lst (list): list of duplicate tuple

  Returns:
      [list]: list of unique tuple
  """
  data = list(set([i for i in lst]))
  return data 

def save_img(img: object) -> None:
  """ 
  Generate new unique id and save file on disk 

  Args:
      img (object): pillow obj
  """
  unique_id = uuid.uuid1() 
  img.save('img/' + str(unique_id) + '.jpg')

def gen_new_images(data: list, mode: str) -> None:
  """
  Generate new image from a  mix of RBG or CMYK channels

  Args:
      data (list): list of pillow object from images on disk
  """

  if mode == 'CMYK':
    cyan = [x[0] for x in data]
    magenta = [x[1] for x in data]
    yellow = [x[2] for x in data]
    black = [x[3] for x in data]
    
    l = len(data) - 1

    for i in range(l):
      c = random.randint(0, l)
      m = random.randint(0, l)
      y = random.randint(0, l)
      b = random.randint(0, l)
      print(c, m, y, b)
      try:
        new_img = Image.merge(mode, (cyan[c], magenta[m], yellow[y], black[b]))
      except IndexError:
        print('out of range')
        continue
      save_img(new_img)

  if mode == 'RGB':
    red = [x[0] for x in data]
    green = [x[1] for x in data]
    blue = [x[2] for x in data]
    
    l = len(data) - 1

    for i in range(l):
      r = random.randint(0, l)
      g = random.randint(0, l)
      b = random.randint(0, l)
      print(r, g, b)
      try:
        new_img = Image.merge(mode, (red[r], green[g], blue[b]))
      except IndexError:
        print('out of range')
        continue
      save_img(new_img)
 
if __name__ == "__main__":
  

  # data_1 = []
  # data_2 = []
  # data_3 = []
  # data_4 = []
  # data_5 = []
  # data_6 = []
  # data_7 = []
  
  data = []
  sizes = []
  
  with os.scandir(base_path) as entries:

    for entry in entries:
      try:
        if entry.is_file():
          channels = read_img(base_path + entry.name, 'RGB')
          sizes.append(channels[0].size)
          data.append(channels)

          # for s in all_sizes:
          #   if channels[0].size == s:
              # pprint.pprint(s)
             

              # print(s, data, channels)
              # gen_new_images(data=data, mode='RGB')
          # if channels[0].size == (4032, 3024):
          #   data_1.append(channels)
          # if channels[0].size == (4896, 2752):
          #   data_2.append(channels)
          # if channels[0].size == (1600, 1200):
          #   data_3.append(channels)
          # if channels[0].size == (3872, 2592):
          #   data_4.append(channels)
          # if channels[0].size == (4896, 2752):
          #   data_5.append(channels)
          # if channels[0].size == (4288, 2848):
          #   data_6.append(channels)
          # if channels[0].size == (1000, 667):
          #   data_7.append(channels)
      except FileNotFoundError:
        continue

  all_sizes = removeDuplicates(sizes)

  for d in data:
    all_data = [d for s in all_sizes if s == d[0].size]
    print(all_data)

  # for d in data:
  #   x = []
  #   for s in all_sizes:
  #     if d[0].size == s:
  #       x.append(d)
  #   all_data.append(x)
    
    # all_data.append(data)
  # pprint.pprint(all_data)
  # pprint.pprint(all_data)
  # sizes = removeDuplicates(sizes)
  # print('sizes of the images', sizes, 'number of sizes:', len(sizes))

  # gen_new_images(data=data_7, mode='RGB')
