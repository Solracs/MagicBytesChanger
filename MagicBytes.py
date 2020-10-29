#!/usr/bin/python3


# This is an easy script that helps you adding the numbers that
# identify the files.
# Now jpg and png are available
# More extensions will be added if requested


#IMPORTANT
# running this will remove all the data which was stored on the file

numbers = {'jpg' : [255, 216, 255, 224], 'png' : [137,80,78,71]}

filename = input("Name of the file: ")

try:
    file = open(filename, 'wb')
    fileExtension = input("Extension: ")
    byteNumbers = bytearray(numbers[fileExtension])

    file.write(byteNumbers)
    file.close()
except:
    print("Error. Not such file")
