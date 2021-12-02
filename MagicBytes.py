#!/usr/bin/python3


# This is an easy script that helps you adding the numbers that
# identify the files.
# Now jpg, png and gif are available
# More extensions will be added if requested


import sys

if len(sys.argv) == 1:
    print("How to use: \n->python3 MagicBytes.py <yourfile> <wantedextension>")
    print("->python3 MagicBytes.py help")
elif len(sys.argv) == 2 and sys.argv[1] == "help":
    print("How to use: \npython3 MagicBytes.py <yourfile> <wantedextension>")
    print("Only jpg, png and gif are available")
elif len(sys.argv) == 3:
    numbers = {'jpg' : [255, 216, 255, 224, 0, 16, 74, 70, 73, 70, 0, 1], 'png' : [137,80,78,71], 'gif' : [71, 73, 70, 56, 55, 97]}

    filename = sys.argv[1]

    try:
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
    except:
        print("Not such file")
    try:
        file = open(filename, 'wb')
        fileExtension = sys.argv[2]
        byteNumbers = bytearray(numbers[fileExtension])

        file.write(byteNumbers)
        file.close()

        file = open(filename, "a")
        file.write("\n\n\n")
        for line in lines:
            file.write(line)
        file.close()
        print("Succes")
    except:
        print("Error. Not such file")
else:
    print("ERROR. Wrong number of arguments\n\n")
