import turtle       # box.py - Part b

class Box(object):
    
    def __init__(self, x_coord=0, y_coord=0, width=100, height=100):
        '''box at (x_coord,y_coord) with given width and height'''
        # requires: all arguments are numeric, width > 0, height > 0
        # assumes: measurements are in pixels  
        self.x = x_coord    # x coordinate of lower left corner
        self.y = y_coord    # y coordinate of lower left corner
        self.w = width      # width of the box
        self.h = height     # height of the box        
     
    def add (self, other):  
        """sum of self and other"""
        new_x = min(self.x, other.x)
        new_y = min(self.y, other.y)
        new_w = max(self.x + self.w, other.x + other.w) - new_x
        new_h = max(self.y + self.h, other.y + other.h) - new_y
        return Box(new_x, new_y, new_w, new_h)
           
    def move (self, amt_x=0, amt_y=0): 
        """move self by amt_x horizontally and amt_y vertically"""
        self.x += amt_x
        self.y += amt_y
        
    def getStr (self):
        """string representation of self"""
        templ = 'box@({:.1f}, {:.1f}), {:.1f} pxl X {:.1f} pxl'
        return templ.format(self.x, self.y, self.w, self.h)
        
    def draw (self, color='black', turtle=turtle):
        """draw the box"""
        turtle.pensize(2)
        turtle.color(color) 
        turtle.setheading(0)
        turtle.up()
        # move the turtle into position (lower left corner)            
        turtle.goto(self.x, self.y)
        # draw the box
        turtle.down()
        turtle.showturtle()        
        turtle.forward(self.w)
        turtle.left(90)
        turtle.forward(self.h)
        turtle.left(90)
        turtle.forward(self.w)
        turtle.left(90)
        turtle.forward(self.h)
        turtle.hideturtle()

def test_draw( shape_lst, turtle=turtle):
    """test driver - draw the boxes in box_lst using turtle"""
    # requires: shape_lst is a list of objects with 'conforming' draw methods
    # draws the shapes in different colors on the screen associated with turtle
    # clears the screen before terminating
    
    COLORS = ['red', 'green', 'purple', 'blue', 'orange', 'black', 'turquoise']
    
    for i in range(len(shape_lst)):
        next_color = COLORS[ i%len(COLORS) ]
        next_shape = shape_lst[i]
        next_shape.draw(next_color)
        
    input('Press any key to continue...\n')
    turtle.clear()       


b1 = Box()
print('b1:', b1.getStr())

b2 = Box(-10, 50, 75, 75)
print('b2:', b2.getStr())

b3 = b1.add(b2)
print('b3:', b3.getStr())

test_draw([b1, b2, b3])

b2.move(-150, -100)
print('b2:', b2.getStr())

test_draw([b1, b2, b3]) 

blst = [Box(50*i, 50*i) for i in range(-5, 5)]
test_draw( blst )

turtle.bye()