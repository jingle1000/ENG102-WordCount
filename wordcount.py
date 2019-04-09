with open('input.txt', 'r') as f:
    inQuotes = False
    counter = 0
    for line in f:
        for character in line:
            if character == "\"" or character == "(" and not inQuotes:
                inQuotes == True
            if inQuotes and character == "\"" or character == ")":
                inQuotes = False
            if character == " " and not inQuotes:
                counter += 1
print("Word Count: " + str(counter))