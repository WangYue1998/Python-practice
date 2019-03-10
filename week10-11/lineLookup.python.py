import string


"""
Program that uses dictionaries and sets to manipute data read from a file

Prompts for a file name and reads the text to create a 'word dictionary':
Each key is a word from the text, in lower case. The value associated with a 
word is the set of line numbers that the word appears in. 

Then prompts for a series of words to search for.

Prints the line numbers of all lines that contain all the words entered. 
"""



def get_input_file():
    """
    Prompts the user for a file to read (repeadly, if necessary).
    Returns an open file object attached to the file.
    """
    while True:
        try:
            file_name = input("Enter the input file name: ")
            open_file = open(file_name)
            break
        except FileNotFoundError:
            print("File {} could not be opened.".format(file_name))
    return open_file     

 
  

def read_text( text_file ):
    """
    Creates and returns a word dictionary from the text in text_file
    """
    # Requires: text_file references a file that has been opened in read mode
    
    # initialize an empty result dictionay and the line number
    result = {}
    num = 0
    for line in text_file:
        # increment the line number           
        num += 1
        # create normalized list of words (without punction, all lower case)
        # which appear on this line
        line_lst = line.split()
        word_lst = [w.strip(string.punctuation) for  w in line_lst]
        word_lst = [w.lower() for w in word_lst]
        
        # update the result dictionary
        for w in word_lst:
            try:
                # add this line to the lines that w maps to
                result[w] = result[w] | {num}
            except KeyError:
                # first appearance of w; make it map to set with just this line
                result[w] = {num}
    
    return result


 
   
def print_nums(word, num_iterable):
    """
    Prints word and the numbers in num_iterable formatted for an index listing
    """
    # Requires: num_iterable is a collection containing the line numbers (ints)
    #   of the lines that word appears in; num_iterable is empty if word is
    #   does not appear in any line
    INDENT = 3*' '
    if num_iterable:
        num_lst = sorted(num_iterable)
        num_str_lst = [str(num_int) for num_int in num_lst]
        num_str = ', '.join(num_str_lst)
    else:
        num_str = 'Not found'
    print('{}:\n{}{}'.format(word, INDENT, num_str)) 


            
def contains_all ( word_iterable, word_dict ):
    """returns a list containing the numbers of all lines that contain 
    all of the words in word_iterable, in ascending order"""
    # Requires: 
    #  - word_iterable is a collection of words (strings)
    #  - word_dict maps each (normalized) word to the set of line numbers of  
    #      lines in which word appears
    
    return []  # stub, replace with code            

        
        
# read the input file into index        
file = get_input_file()
index_dict = read_text(file)
file.close()

# get the words to be looked up
phrase = input('Enter one or more words to search on:\n') 
phrase_lst = [w.strip(string.punctuation).lower() for w in phrase.split()] 
      
# look them up
num_lst = contains_all(phrase_lst, index_dict)

# print the words and the lines they appear on
print() 
print_nums(phrase, num_lst)               