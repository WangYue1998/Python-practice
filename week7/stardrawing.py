def draw_line(line_spec):
    result = ''
    star_turn = False      
    for num in line_spec:
        if star_turn:
            result = result + num * '*'
        else:
            result = result + num * ' '
        star_turn = not star_turn
    print(result)

def test_draw_line():
    print("draw_line([0, 3, 2, 3]) prints:")
    draw_line([0, 3, 2, 3])
    print(8*'-')
    print()
    print("draw_line([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) prints:")
    draw_line([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    print(10*'-')
    print()
    print("draw_line([0, 1, 1, 2, 1, 3, 1, 2, 1, 1]) prints:")
    draw_line([0, 1, 1, 2, 1, 3, 1, 2, 1, 1])
    print(13*'-')

test_draw_line()    