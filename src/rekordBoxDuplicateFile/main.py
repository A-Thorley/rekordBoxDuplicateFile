import os
import shutil

originalFolder = "C:\\Users\\leoca\\Music\\320kbps\\"

destinationFolder = "C:\\Users\\leoca\\Music\\MovedFiles\\"

print(originalFolder)

if os.path.exists(originalFolder):
    print("That location exists")
    if os.path.isfile(originalFolder):
        print("That is a file")
    elif os.path.isdir(originalFolder):
        print("That is a folder")
    else:
        print("Not a file or folder")
else:
    print("That location doesn't exist")

print("")

for i, file in enumerate(os.listdir(originalFolder)):

    file_truncated = file[:35].lower()

    for j, file2 in enumerate(os.listdir(originalFolder)):

        file_truncated2 = file2[:35].lower()

        if i != j and file_truncated == file_truncated2:
                #if "remix" in file and "remix" not in file2:
                    #print(end="")
                #elif "remix" in file2 and "remix" not in file:
                    #print(end="")
                #else:
            print(f"'{file}' is a duplicate")
            filePath = "C:\\Users\\leoca\\Music\\320kbps\\" + file
            print(filePath)
            shutil.move(filePath, destinationFolder)
            print(f"'{file}' Transferred")
        else:
            print(end="")











'''
songName = 0
songFinder = 0

def songFinder(name):
    print("looking for matching track...")
    for i in len(folder)

if songName = songFinder(name):'''