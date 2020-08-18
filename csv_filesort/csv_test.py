import csv
import os

ROOT_PATH = "/home/dbuzzell/test_dir"


def getFiles(root_name, list_files, indent):
    indent_str = [""] * indent
    if os.path.isfile(root_name):
        return [indent_str + [root_name]]
    else:
        file_sort = sorted(sorted(os.listdir(root_name), key=lambda s: s.casefold()),
                           key=lambda s: os.path.isfile(root_name + "/" + s))
        for f in file_sort:
            new_entry = indent_str + [f + "/"] if os.path.isdir(root_name + "/" + f) else indent_str + [f]
            list_files.append(new_entry)
            getFiles("{}/{}".format(root_name, f), list_files, indent + 1)
        return list_files

  
listofFiles = getFiles(ROOT_PATH, [[ROOT_PATH + "/"]], 1)
with open("testing.csv", "w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(listofFiles)
