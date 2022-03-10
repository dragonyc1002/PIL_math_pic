import PIL #匯入PIL
from PIL import Image #匯入PIL.Image
from PIL import ImageDraw #匯入PIL.ImageDraw

import PIL.Image
import PIL.ImageDraw
import math #匯入math

#定義r,g,b三個function
def r(x,y):
    return int(math.tan(x*y)*10)

def g(x,y):
    return r(x,y)

def b(x,y):
    return r(x,y)

print(r,g,b)


img = Image.new("RGB", (1024,1024), "black") #定義img為新增一個1024*1024,且為黑背景的圖

pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i,j] = (r(i,j), g(i,j), b(i,j))

img.save("main.jpg", "JPEG") #儲存jpg檔案
