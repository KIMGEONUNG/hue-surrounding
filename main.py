from PIL import Image

# Basic parameters
interval=10
step=50
images = []
path = "./images/sample3.jpg"

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
    added = i * interval
    new_data = []
    for d in data:
        new_rgb = ((d[0] + added)%255, (d[1] + added)%255, (d[2] + added)%255)
        new_data.append(new_rgb)

    im = Image.new('RGB', (width, height))
    im.putdata(new_data)

    images.append(im)

# Save to gif
images[0].save('./output_animation.gif',
        save_all=True, append_images=images[1:], optimize=False, duration=80, loop=0)

print("# Program finished")
