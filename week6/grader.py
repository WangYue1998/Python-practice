def open_scores_file():
    """
    prompts for an input file name; returns an opened input file object
    """
    file=input("Enter the file name:")
    while True:
        try:
            file = open(file)  
        except:
            print("Error message")
            file = input("Enter the file name")
        
        return file
     # Replace with code

def total_score(line):
    """
    the total of the scores in scores_str
    """
       # Replace with code  
    one=(line[9:12])
    two= (line[14:17])
    three= (line[19:22])
    print(one)
    print(two)
    print(three)
    total_score= int(one)+int(two)+int(three)
    return total_score  
    
    
def grade(points_scored, points_possible):
    """
    the grade for a score of points_scored out of a total of points_possible
    """
    pass      # Replace with code


# main code

file_object=open_scores_file() 
header = file_object.readline()
total_pts = file_object.readline().strip()
#print(header)
#print(total_pts)
for line in file_object:
   #print(line, end="")
   
   total_score(line)
   
file_object.close
