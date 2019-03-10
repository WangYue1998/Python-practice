
class Box(object):
    
    def __init__(self, x_coord=0, y_coord=0, length=100, height=100):
        '''box at (x_coord,y_coord) with given length and height'''
        # requires: all arguments are numeric, length > 0, height > 0
        # assumes: measurements are in pixels 
        if type(x_coord)== int or type(x_coord)==float:
            self.x = x_coord    # x coordinate of lower left corner
        else:
            raise ValueError
        if type(y_coord) == int or float:
            self.y = y_coord    # y coordinate of lower left corner
        else:
            raise ValueError
        if length >0 and type(length)== int:
            self.l = length# length of the line
        else:
            raise ValueError
        if type(height)== int:
            self.h = height     # height of the box 
        else:
            raise ValueError
    def __add__ (self, other):  
        """sum of self and other"""
        new_x = min(self.x, other.x)
        new_y = min(self.y, other.y)
        new_l = max(self.x + self.l, other.x + other.l) - new_x
        new_h = max(self.y + self.h, other.y + other.h) - new_y
        return Box(new_x, new_y, new_l, new_h)
        
    def __mul__(self, scalar=1):
        """product of self and scalar (a positive numeric value)"""
        new_l = self.l * scalar
        new_h = self.h * scalar
        return Box(self.x, self.y, new_l, new_h)
           
    def move (self, amt_x=0, amt_y=0): 
        """move self by amt_x horizontally and amt_y vertically"""
        self.x += amt_x
        self.y += amt_y
        
    def __str__ (self):
        """string representation of self"""
        templ = 'box@({:.1f}, {:.1f}), {:.1f} pxl X {:.1f} pxl'
        return templ.format(self.x, self.y, self.l, self.h)
    
    def __repr__(self):
        new_str= self.__str__()
        return new_str
    
    def __rmul__(self, scalar=1 ):
        s = self.__mul__(scalar)
        return s 
    
    def __eq__(self, other):
        if type(other)== Box:
            if self.x == other.x and self.y == other.y and self.h == other.h and \
                self.l == other.l:
                    return True
            else:
                return False
        else:
            return False
        

b1 = Box()
print('str(b1):', b1)
print('b1:', b1)

b2 = Box(-10, 50, 75, 75)
print('str(b2):', b2)
print('b2:', b2)

b3 = b1 + b2
print('b3:', b3)

b2.move(-150, -100)
print('b2:', b2)

b4 = b2*1.5
print('b4:', b4)

# For use in Step 6 of Part (a) 
b5 = 1.5 * b2
print('b5:', b5)

# For use in Step 7 of Part (a)
b6 = b4
print('b6:', b6)
print('b4 == b5:', b4 == b5)
print('b4 == b6:', b4 == b6)

try:
    b7 = Box('hi')
except ValueError:
    print()