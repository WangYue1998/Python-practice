# Program to process data from files using dictionaries

"""
Each line of the file passed into function make(...) contains a player name,
followed by one or more point values (integers), each separated from the next
by a comma (e.g., similar to initData.txt)
   
Each line of the file passed into function update(...) starts with a '+' or
a '-', followed by a player name and then by one or more point values (ints),
each separated from the next by a comma (e.g., similar to updataData.txt).

The program calls function update(...) to update the points lists of players
in an existing points dictionary, where the update file specifies the updates
to be peformed. A lines that starts with a '+' specifies one or more points
that are to be added to a player's point list.  A line that starts with a '-'
specifies one or more points that are to be deleted from a players's points
list.  The update(...) function will display an informative message and ignore
a line if the player is not already in the points dictionary; it will display
an informative message and ignore a point value if the player's point list does 
not contain the point value to be removed.  
"""

def make(filename):
    """
    Creates a players dictionary from the data in filename and returns it
    """
    # the players dictionary associates each player in filename with the
    # list of points (ints) in filename for that player 

    # initialize the result to be returned to be an empty dict
    result_dic = {}
    
    # open the file for reading
    fd = open(filename, 'r')
     
    # read and process each line in the file
    for line in fd:
        # split the line into a list of strings
        line_lst = line.strip().split(',')
        # check that the line is not empty
        if line_lst[0]:
            # save the player name
            player = line_lst[0]
            # convert the point strings to ints
            point_lst = [int(n) for n in line_lst[1:]]
        
            # a player not already in the dictionary has no points yet
            if player not in result_dic:
                result_dic[player] = []
            
            # extend the player's points list with the points in this line
            result_dic[player] += point_lst
        
    fd.close()
    return result_dic
    
def update(data_dict, up_filename):
    """
    Updates data_dict according to the specification in the file up_filename
    """

    pass       # replace with code 
    
        
def print_stats(data_dict):
    """
    Displays players, their total points, and their averages from data_dict
    """
    # Display a header row
    # Display in descending order by total points  
    # Truncate names to 10 characters; line players and points in columns
    # Display average with one-digit of accuracy
    
    pass       # replace with code
        
        
# main code section

points_dict = make('initData.txt')
print('After initialization:\n')
print_stats(points_dict)

update(points_dict, 'updateData.txt')
print('\nAfter update:\n')
print_stats(points_dict)

    
