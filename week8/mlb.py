"""
Manages information about baseball players.

Represents each player by a 'player-info' tuple containing:
    player’s name (of type str)
    team identifier (of type str)
    games played (of type int)
    at bats (of type int)
    runs scored (of type int)
    hits (of type int)
    homeruns (of type int)
    batting average (of type float)
    
The first seven items are read from a file and the last is calculated.
All are of the type indicated.

Represents the data on all players in a file as a list of player-info tuples.

Input files:
A comment line begins with '#'.  A legal non-comment line contains the first
seven items one player; a semi-colon separates items. (See mlb.test.txt,
mlb.2013.txt)
"""

# index in player-info tuples containing player information 
PN_X = 0    # player name
TI_X = 1    # team ID
GP_X = 2    # games played
AB_X = 3    # at bats
RS_X = 4    # runs scored
HI_X = 5    # hits
HR_X = 6    # home runs
BA_X = 7    # batting average

MENU = """
Enter one of the following commands:
   QUIT - quit the program
   HELP - display this message
   INPUT filename - load a new player data set 
   TEAM id - display statistics for a team; supported team id's are:
             ARI, ATL, BAL, BOS, CHC, CIN, CLE, COL, CWS, DET, 
             HOU,  KC, LAA, LAD, MIA, MIL, MIN, NYM, NYY, OAK,  
             PHI, PIT,  SD, SEA,  SF,  TB, TEX, TOR, WAS
   HOMERS n - display statistics for the top n homerun hitters (n > 0)
"""


def read_file(file_name):
    """Returns the data set (list) created from reading file_name"""   
    # if a line is incorrectly formatted, prints an error message and ignores it
    # ignores comments lines (lines starting with '#')
    # if file_name is bad, prints an error message and returns an empty list
    file_name= input("Enter an file name:")
    lne=[]
    try:
        file= open(file_name, 'r')
        file.readline()
        for line in file:
            lne.append(line.strip())
            lne_list= lne
            Battingaver=float(line[HI_X])/float(line[AB_X])
            lne_list.append(Battingaver)
        return tuple(lne_list)
            
    except FileNotFoundError:
        print("Errormessage")
        return lne
    
 


def print_roster(roster):
    """Prints formatted table from roster, in the order listed in roster."""
    # Requires: roster is a non-empty list of player-info tuples
    TEMPL = \
    "Replace with a template to use in printing player information"
    
    # print a blank line and then the header
    pass         #  delete and replace with code 
    
    # print the player statistics (use TEMPL.format(...) to line things up)
    pass         #  delete and replace with code 

       
def get_team(roster, team_id):
    """Returns the list of player-info tuples in roster on team team_id."""
    # Requires: roster is a list of player-info tuples.
    
    pass         #  delete and replace with code 


def get_top_hitters(roster, num):
    """Returns the list of num player-info tuples in roster with the highest 
    number of home runs"""
    # Requires: roster is a list of player-info tuples; n > 0 is an int.
    # Return list is sorted by number of home runs (high to low) and then
    #   alphabetically (low to high) by player name
    pass  # delete and replace with code 
 

# Main processing, start by printing the menu of commands
print(MENU)    

# initialize the dataset of player information to be empty
player_ds = []

# prompt for commands and execute them
#TEAM_id= [ARI, ATL, BAL, BOS, CHC, CIN, CLE, COL, CWS, DET, 
             #HOU,  KC, LAA, LAD, MIA, MIL, MIN, NYM, NYY, OAK,  
             #PHI, PIT,  SD, SEA,  SF,  TB, TEX, TOR, WAS]
while True:

    command = input('Enter a command: ').strip()
    
    if command.lower() == 'quit':
        print("Terminating.")
        break 
    
    elif command.lower() == 'help':
        print(MENU)
        
    elif command[:5].lower() == 'input':
        print('INPUT command')
        
    elif command.lower in TEAM_id:
        get_team(roster, command.lower)
        print()
    elif command =='HOMERS n':
        print()
    else: 
        command = input('Enter a command: ').strip()

     
