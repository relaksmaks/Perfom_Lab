from sys import argv

circle_file_path, dot_file_path = argv[1], argv[2]

with open(circle_file_path, encoding='utf-8') as circle_file:
    data = circle_file.read()
    crdnts, radius = data.split('\n') 
    x = int(crdnts[0])
    y = int(crdnts[2])
    r = int(radius)

with open(dot_file_path, encoding='utf-8') as dot_file:
    data = dot_file.read()
    dots = data.split('\n')

for dot in dots:
    x1 = int(dot[0])
    y1 = int(dot[2])
    if (x - x1) * (x - x1) + (y - y1) * (y - y1) == r * r:
        print(0)
    elif (x - x1) * (x - x1) + (y - y1) * (y - y1) < r * r:
        print(1)
    else:
        print(2)

