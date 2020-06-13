from PIL import Image
from enum import Enum
import colorsys
import sys
import getopt

args = sys.argv[1:]
opts, args = getopt.getopt(args, 'r:g:b:p:o:h')

class value_rule(Enum):
    ZERO = 0
    PLUS = 1
    MINUS = 2

# Basic parameters
interval=0.005
step=20
images = []
path = "./images/sample1.jpg"
output = './output.gif'

ruleR = value_rule.PLUS
ruleG = value_rule.PLUS
ruleB = value_rule.PLUS

for opt, arg in opts:
    if opt == "-r":
        if arg == "0":
            ruleR = value_rule.ZERO
        elif arg == "1":
            ruleR = value_rule.PLUS
        elif arg == "2":
            ruleR = value_rule.MINUS
        else:
            raise ValueError("")
    elif opt == "-g":
        if arg == "0":
            ruleG = value_rule.ZERO
        elif arg == "1":
            ruleG = value_rule.PLUS
        elif arg == "2":
            ruleG = value_rule.MINUS
        else:
            raise ValueError("")
    elif opt == "-b":
        if arg == "0":
            ruleB = value_rule.ZERO
        elif arg == "1":
            ruleB = value_rule.PLUS
        elif arg == "2":
            ruleB = value_rule.MINUS
        else:
            raise ValueError("")
    elif opt == "-p":
        path = arg
    elif opt == "-o":
        output = arg
    elif opt == "-h":
        print("-r : R of RGB value sign. 0 is no change, 1 is plus, 2 is minus. Default value is 1")
        print("-g : G of RGB value sign. 0 is no change, 1 is plus, 2 is minus. Default value is 1")
        print("-b : B of RGB value sign. 0 is no change, 1 is plus, 2 is minus. Default value is 1")
        print("-p : Input image file path. Default path is \"%s\"" % path)
        print("-o : output image file path. Default path is \"%s\"" % output)
        sys.exit(1)

print("# Parameters")
print("interval : " + str(interval))
print("step : " + str(step))
print("image path : " + str(path))

# Read original image file
im = Image.open(path)
data = im.getdata()
width, height = im.size

print("# Original image pixel datas")
print("width : " + str(width))
print("height : " + str(height))

# Create new image frame
for i in range(0,step):

    val = i * interval
    
    new_data = []
    for d in data:
        try:
            hsl = colorsys.rgb_to_hls(d[0],d[1],d[2])
        except:
            pass
        finally:
            hsl = [0,0,0]

        new_h = hsl[0] + val
        new_rgb = colorsys.hls_to_rgb(new_h, d[1], d[2])
        new_rgb_int = (int(new_rgb[0]), int(new_rgb[1]), int(new_rgb[2]))
        new_data.append(new_rgb_int)

    im = Image.new('RGB', (width, height))
    im.putdata(new_data)

    images.append(im)

# Save to gif
images[0].save(output,
        save_all=True, append_images=images[1:], optimize=False, duration=80, loop=0)

print("# Program finished")
