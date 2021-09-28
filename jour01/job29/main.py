def draw_triangle(height):
    triangle = ""
    width = height * 2
    i = 0
    j = i + 1
    while i < height:
        for it in range(0, width):
            if it == width / 2 - j:
                triangle += "/"
            elif it == width / 2 + i:
                triangle += "\\"
            if i == height - 1 and width / 2 - j < it < width / 2 + i:  # last line
                triangle += "_"
            else:
                triangle += " "
        i += 1
        j += 1
        triangle += "\n"
    return triangle


# Test
height = int(input("Entrez un nombre"))
print(draw_triangle(height))