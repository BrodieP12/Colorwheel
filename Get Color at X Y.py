import math
import os
from PIL import Image
import sys

bg_color = 0x888888
img_size = 500
img_half = img_size / 2
inner_radius = 100
outer_radius = 240

#Base: 1, adj: 0, ratio: 0.043987087836378946, shade: 0.8716060268720883

"""base = 1
adj = 0
ratio = 0.043987087836378946
shade = 0.8716060268720883
"""



def get_adj(x,y):
    if x - img_half == 0:
        angle = angle = -90
        if y > img_half:
            angle = 90
    else:
        angle = math.atan2((y - img_half), (x - img_half)) * 180 / math.pi
    angle = (angle + 30) % 360
    idx = angle / 60
    if idx < 0:
        idx = 6 + idx
    base = int(round(idx))
    adj = (6 + base + (-1 if base > idx else 1)) % 6
    return adj

#adj = get_adj(x,y)



def get_base(x,y):
    if x - img_half == 0:
        angle = angle = -90
        if y > img_half:
            angle = 90
    else:
        angle = math.atan2((y - img_half), (x - img_half)) * 180 / math.pi

    angle = (angle + 30) % 360
    idx = angle / 60
    if idx < 0:
        idx = 6 + idx
    base = int(round(idx))
    return base
#base = get_base(x,y)



def get_ratio(x,y):
    if x - img_half == 0:
        angle = angle = -90
        if y > img_half:
            angle = 90
    else:
        angle = math.atan2((y - img_half), (x - img_half)) * 180 / math.pi

    angle = (angle + 30) % 360
    idx = angle / 60
    if idx < 0:
        idx = 6 + idx
    base = int(round(idx))
    ratio = max(idx, base) - min(idx, base)
    return ratio

#ratio = get_ratio(x,y)

def get_shade(x,y):
    dist = abs(math.sqrt((x - img_half) ** 2 + (y - img_half) ** 2));
    boolVal = False
    if dist < inner_radius or dist > outer_radius:
        boolVal = True
    shade = 2 * (dist - inner_radius) / (outer_radius - inner_radius)
    return boolVal, shade

#shade = get_shade(x,y)




def make_color(x, y):
    output = 0x0
    bit = 0
    rgb = ()
    base = get_base(x,y)
    adj = get_adj(x,y)
    ratio = get_ratio(x,y)
    boolVal, shade = get_shade(x,y)
    if boolVal:
        print("Out of bounds")
        sys.exit()
    #Go through each bit of the colors adjusting blue with blue, red with red,
    #green with green, etc.
    for pos in range(3):
        base_chan = color_wheel[base][pos]
        adj_chan = color_wheel[adj][pos]
        new_chan = int(round(base_chan * (1 - ratio) + adj_chan * ratio))

        # now alter the channel by the shade
        if shade < 1:
            new_chan = new_chan * shade
        elif shade > 1:
            shade_ratio = shade - 1
            new_chan = (0xff * shade_ratio) + (new_chan * (1 - shade_ratio))
        output = int(new_chan) >> bit
        rgb = rgb + (output,)
    return rgb

color_wheel = [
    [0xff, 0x00, 0xff],
    [0xff, 0x00, 0x00],
    [0xff, 0xff, 0x00],
    [0x00, 0xff, 0x00],
    [0x00, 0xff, 0xff],
    [0x00, 0x00, 0xff],
    [0xff, 0x00, 0xff]]

valX = int(input("Value X :"))
valY = int(input("Value Y: "))
rgb = make_color(valX, valY)
print(rgb)


