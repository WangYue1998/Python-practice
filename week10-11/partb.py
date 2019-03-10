import string

def get_input_file():
    while True:
        try:
            file_name = input("Enter the input file name: ")
            open_file = open(file_name)
            break
        except FileNotFoundError:
            print("File {} could not be opened.".format(file_name))
    return open_file        

def read_text( text_file ):
    result = {}
    num = 0
    for line in text_file:           
        num += 1
        line_lst = line.strip().split()
        word_lst = [w.strip(string.punctuation) for  w in line_lst]
        word_lst = [w.lower() for w in word_lst]
        
        for w in word_lst:
            try:
                result[w] = result[w] | {num}
            except KeyError:
                result[w] = {num}
    
    return result

def print_nums(word, num_iterable):
    INDENT = 3*' '
    if num_iterable:
        num_lst = sorted(num_iterable)
        num_str_lst = [str(num_int) for num_int in num_lst]
        num_str = ', '.join(num_str_lst)
    else:
        num_str = 'Not found'
    print('{}:\n{}{}'.format(word, INDENT, num_str)) 
        
file = get_input_file()
index = read_text(file)
file.close()
word_lst = ['Fissure', 'Who', 'They']
for w in word_lst:
    w_lc = w.lower()
    if w_lc in index:
        print_nums(w, index[w_lc])
    else:
        print_nums(w, set())