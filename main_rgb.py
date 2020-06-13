from PIL import Image
from enum import Enum
import sys
import getopt

args = sys.argv[1:]
opts, args = getopt.getopt(args, 'r:g:b:p:o:h')

class value_rule(Enum):
    ZERO = 0
    PLUS = 1
    MINUS = 2

# Basic parameters
interval=5
step=51
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
    
    if ruleR == value_rule.ZERO:
        valR = 0 
    elif ruleR == value_rule.PLUS:
        valR = val 
    elif ruleR == value_rule.MINUS:
        valR = val * (-1) 

    if ruleG == value_rule.ZERO:
        valG = 0 
    elif ruleG == value_rule.PLUS:
        valG = val 
    elif ruleG == value_rule.MINUS:
        valG = val * (-1) 

    if ruleB == value_rule.ZERO:
        valB = 0 
    elif ruleB == value_rule.PLUS:
        valB = val 
    elif ruleB == value_rule.MINUS:
        valB = val * (-1) 

    new_data = []
    for d in data:
        new_rgb = ((d[0] + valR + 255)%255, (d[1] + valG + 255)%255, (d[2] + valB + 255)%255)
        new_data.append(new_rgb)

    im = Image.new('RGB', (width, height))
    im.putdata(new_data)

    images.append(im)

# Save to gif
images[0].save(output,
        save_all=True, append_images=images[1:], optimize=False, duration=80, loop=0)

print("# Program finished")
