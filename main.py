from PIL import Image

im = Image.open('./images/sample1.jpg')
data = im.getdata()
data_len = len(list(data))
data_ls = list(data)

print(data_ls)

