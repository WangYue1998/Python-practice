"""
Create a star drawing from an input file.

Each line of the input file provides a line specification as a sequence
of non-negative integers (which could be empty): 
  - the first integer, if any, indicates the number of spaces to print at the 
        start of the line,
  - the second integer, if any, indicates the number of stars to print next, 
  - the third integer, if any, indicates the number spaces to print next, 
  - etc.

An empty sequence specifies a blank line

For example:

    1 4
    5 1
    1 5
    0 1 4 1
    0 1 4 1
    1 5
    
Specifies:

 ****
     *
 *****
*    *
*    *
 *****
     
"""


def draw_line(line_spec):
    """draws a line of alternating sequences of spaces and stars"""
    # Requires: line_spec, a list of non-neg ints, gives the numbers of spaces,
    #   then stars, then spaces, etc.
    result = ''  
    star_turn = False      
    for num in line_spec:
        if star_turn:
            result = result + num * '*'
        else:
            result = result + num * ' '
        star_turn = not star_turn
    print(result)
    
def get_input_file():
    """Returns a file object in read mode. Prompts the user for the file
       name (repeatedly, if user enters a bad file name).
    """
    
    filename= input("Please enter the name:") 
    while True:
        try: 
            file=open(filename,'r')
            break
        except FileNotFoundError:
            filename= input("Please enter the name again:")
            
    return file
        
     # replace this line with code
    
    
def get_line_spec(line_str):
    """Returns the list of ints in line_str"""
    # Requires: line_str is a string of space-separated ints (or empty)
    line_spec= line_str.strip()
    line_spec= line_spec.split() 
    for i in range(len(line_spec)):
        line_spec[i]= int(line_spec[i])
   
    return line_spec
    '''result=[]
    for ch in line_spec:
        result.append(int(ch))
    return result'''

    
    # replace this line with code
     

def main():
    file= get_input_file()
    # get the opened input file (use get_input_file) 
    for line in file:
        line_spec= get_line_spec(line)
        draw_line(line_spec)
        
        
    # for each line of the input file, 
    #    get the line spec (use get_line_spec) and 
    
    #    print the line (use draw_line)
    file.close
    # close the input file
     
main()




        
    
        


    
        
        

