def draw_rectangle(width, height):
    rectangle = ""
    j = 0
    while j != height:
        i = 0
        while i < width:
            if i == 0 or i == width - 1:
                rectangle += "|"
            elif j == 0 or j == height - 1:
                rectangle += "-"
            else:
                rectangle += " "
            i += 1
        j += 1
        rectangle += "\n"
    return rectangle


# Test
print(draw_rectangle(10, 3))
