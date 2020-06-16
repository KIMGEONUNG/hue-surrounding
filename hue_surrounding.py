from PIL import Image
from enum import Enum
import colorsys
import sys
import getopt

args = sys.argv[1:]
opts, args = getopt.getopt(args, 'f:i:o:h')

# Basic parameters
interval=0.05
frame=20
images = []
path = "./sample_images/sample.png"
output = './output.gif'

for opt, arg in opts:
    if opt == "-i":
        path = arg
    elif opt == "-s":
        frame = int(arg) 
        interval = 1 / frame 
    elif opt == "-o":
        output = arg
    elif opt == "-h":
        print("-f : The number of frames ")
        print("-i : Input image file path. Default path is \"%s\"" % path)
        print("-o : output image file path. Default path is \"%s\"" % output)
        sys.exit(1)

print("### Program Started ###")
print("# Parameters")
print("interval : " + str(interval))
print("frame : " + str(frame))
print("image path : " + str(path))

# Read original image file
im = Image.open(path)
data = im.getdata()
width, height = im.size

print("# Original image pixel datas")
print("width : " + str(width))
print("height : " + str(height))

# Create new image frame
for i in range(0,frame):

    val = i * interval
    
    new_data = []
    for d in data:
        hsl = colorsys.rgb_to_hls(d[0]/255,d[1]/255,d[2]/255)

        new_h = (hsl[0] + val)
        new_rgb = colorsys.hls_to_rgb(new_h, hsl[1], hsl[2])
        new_rgb_int = (int(new_rgb[0] * 255), int(new_rgb[1] * 255), int(new_rgb[2] * 255))
        new_data.append(new_rgb_int)

    im = Image.new('RGB', (width, height))
    im.putdata(new_data)

    images.append(im)

# Save to gif
images[0].save(output,
        save_all=True, append_images=images[1:], optimize=False, duration=80, loop=0)

print("### Program Finished ###")
