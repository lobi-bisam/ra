import os
yourpath = "C:\\tasks\\lobi"

"""
Program tworzy dodatkowy folder Other opisany w zadaniu.
Została też uwzglęgniona sytuacja, w której sprzątamy katalog z istniejącymi już folderami.
oraz sytuacja w której zrobiliśmy sprzątanie, część plików wylądowała w Other, a w kolejnej rundzie, 
po dodaniu kilku plików o tym samym rozszerzeniu, ich suma (z Other + nowe) przekracza ustaloną liczbę 
(3?) i tworzy nowy Folder. 
"""

def giveAllDirs(path, list):
    list_folders = list
    path = path
    dirs = os.listdir(path)
    for file in dirs:
        pathDic = os.path.join(path, file)
        if os.path.isdir(pathDic):
            list_folders.append(file)
    return list_folders


def toolittle(path):
    path = path
    dirs = os.listdir(path)
    name = "other"
    other_path = os.path.join(path, name)
    if not os.path.isdir(other_path):
        os.makedirs(other_path)

    for file in dirs:
        path2 = os.path.join(path, file)
        dirpath2 = os.listdir(path2)
        if (len(dirpath2)) < 4:
            for item in dirpath2:
                old_path = os.path.join(path2, item)
                new_path = os.path.join(other_path, item)
                os.replace(old_path, new_path)
            #if len(dirpath2) == 0:
            #    os.rmdir(path2)


def clearRemoveOther(name, path):
    other_path = os.path.join(path, name)
    for item in os.listdir(other_path):
        old_path = os.path.join(other_path, item)
        new_path = os.path.join(path, item)
        os.replace(old_path, new_path)
    os.rmdir(other_path)


def deleteEmptyDirectories(path):
    for item in os.listdir(path):
        path_item = os.path.join(path, item)
        if len(os.listdir(path_item)) == 0:
            os.rmdir(path_item)



def ogarniacz(yourpath):
    path = yourpath
    # take all files from dic "other" to order them again
    name = "other"
    other_path = os.path.join(path, name)
    if os.path.isdir(other_path):
        clearRemoveOther(name, path)

    list_folders = []
    list_folders = giveAllDirs(yourpath, list_folders)
    dirs = os.listdir(path)
    dirs = list(set(dirs) - set(list_folders))  # delete all dics from my list to check
    if len(dirs) == 0:
        return "No files without directories"
    first = dirs[0]
    print(first)
    end = first.split(".")[1]  # first folder from this directory

    if len(list_folders) == 0:
        old_path = os.path.join(path, first)
        folder_path = os.path.join(path, end)  # define path to folder
        os.makedirs(folder_path)  # create new folder
        print(folder_path)
        new_path = os.path.join(folder_path, first)
        #os.replace(old_path, new_path)  CHECK ITTT!!!
        list_folders = [end]  # lista folderów
    # print(list_folders)

    for file in dirs:
        old_path = os.path.join(path, file)  # path to file /file.xyz
        # print(old_path)
        end = file.split(".")[1]
        i = 0
        for folder in list_folders:
            #print("jestem też tu")
            n = len(list_folders)
            i += 1
            if end == folder:
                folder_path = os.path.join(path, end)  # path to folder /xyz
                new_path = os.path.join(folder_path, file)  # path to file in folder /xyz/file.xyz
                os.replace(old_path, new_path)
                break
        if i == n and end != folder:
            folder_path = os.path.join(path, end)  # path to folder /xyz
            #print("jestem tu")
            os.makedirs(folder_path)  # create new path
            new_path = os.path.join(folder_path, file)
            os.replace(old_path, new_path)
            list_folders.append(end)


def main():
    print("blabla")


if __name__ == '__main__':
    ogarniacz(yourpath)
    toolittle(yourpath)
    deleteEmptyDirectories(yourpath)
