#照片變黑白
from PIL import Image

image_file = Image.open('monty-truth.png')
image_file = image_file.convert('L')#1是指轉黑白，L也可以，但它畫質較好
image_file.save('result.png')