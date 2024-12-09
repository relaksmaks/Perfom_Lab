from sys import argv

circle_file_path, dot_file_path = argv[1], argv[2]

with open(circle_file_path, encoding='utf-8') as circle_file:
    circle_coords, rad = [line.strip() for line in circle_file.readlines()]
    circle_coords, rad = [float(i) for i in circle_coords.split()], float(rad)

with open(dot_file_path, encoding='utf-8') as dot_file:
    dots = [[float(i) for i in line.strip().split(" ")] for line in dot_file.readlines()]
    dots = [[x - circle_coords[0], y - circle_coords[1]] for x, y in dots]

for dot in dots:
    hyp = (dot[0] ** 2 + dot[1] ** 2) ** 0.5
    print(1 if hyp < rad else 0 if hyp == rad else 2)
