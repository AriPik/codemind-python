def count_special_character(string): 
    special_char= 0
    for i in range(0, len(string)):  
        ch = string[i]
        if (string[i].isalpha()):  
            continue
        elif (string[i].isdigit()):
            continue
        
        elif (string[i]==" "):
            continue
            
        else: 
            special_char += 1
    print(special_char)  
    
string = input()
count_special_character(string)