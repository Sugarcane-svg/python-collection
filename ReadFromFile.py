# given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen.

with open('namelist.txt', 'r') as file:
    name_dict = {}
    a = file.readline().replace('\n', '')
    while a:
        
        if  a not in name_dict.keys():
            name_dict[a] = 1
        else:
            name_dict[a] += 1
        
        a = file.readline().replace('\n', '')

    for pair in name_dict.items():
        print(pair)
