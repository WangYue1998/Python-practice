# Game to answer the question:
#   'What animal were you in your prior lifetime?'

#NOT_DONE = "Not done"                                                  

print("This game answers the question:\n")                            
print("\t'What animal were you in your prior lifetime?'\n")           
print("Please answer each question ('Y' for 'yes' and 'N' for 'no').")
print()                                                                

reply = input("Do you like the outdoors?  ")                          
if reply == 'y' or reply == 'Y':                                     
    
    reply = input("Do you like to run?  ")                          
    if reply == 'y' or reply == 'Y':                                 
        print("You were a horse!")                                    

    else:                                                             
        print("You were a turtle!")                                   
        
else: 
    reply = input("Do you like to cheese?  ") 
    if reply == 'y' or reply == 'Y':                                 
        print("You were a mouse!")
    else:
        reply = input("Do you like to swim?  ") 
        if reply == 'y' or reply == 'Y':
            print("You were a fish!")
        else:
            print("You were a cat!")
        


print("\nThanks for playing!")        