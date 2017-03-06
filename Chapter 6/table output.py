def printTable(stringLists):
    #find the largest length of a word
    maxLength = 0
    for i in range(len(stringLists)):
        for j in range(len(stringLists[i])):
            if len(stringLists[i][j]) > maxLength:
                maxLength = len(stringLists[i][j])

    for i in range(len(stringLists[0])):
        for j in range(len(stringLists)):
            print(stringLists[j][i].rjust(maxLength), end = ' ')
        print('')



tableData = [["apples", "oranges", "cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose", "goose"]]


printTable(tableData)
