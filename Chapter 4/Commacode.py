#Write a function that takes a list and returns a string

def listToString(listWithString):
    string = ""

    for i in range(len(listWithString)-1):
        string += listWithString[i]

        if i == len(listWithString)-2: #last one
            string += " and "
            string += listWithString[i+1]
        else:
            string += ", "

    return string

    
    
