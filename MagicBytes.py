#!/usr/bin/python3


# This is a simple script that helps you adding the numbers that
# identify the files.
# Formats jpg, png and gif are currently available
# More extensions will be added if requested


#IMPORTANT
# running this will remove all the data previously stored in the file

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
        file = open(filename, 'wb')
        fileExtension = sys.argv[2]
        byteNumbers = bytearray(numbers[fileExtension])

        file.write(byteNumbers)
        file.close()
        print("Succes")
    except:
        print("Error. Not such file")
else:
    print("ERROR. Wrong number of arguments\n\n")
