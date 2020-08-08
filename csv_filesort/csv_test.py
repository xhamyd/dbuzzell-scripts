import os, sys
import csv

ROOT_PATH = "/home/dbuzzell/test_dir"


def getFiles(root_name, listFiles, indent):
  indentStr = [""] * indent
  if os.path.isfile(root_name):
    return [indentStr + [root_name]]
  else:
    file_sort = sorted(sorted(os.listdir(root_name), key=lambda s: s.casefold()), key=lambda s: os.path.isfile(root_name + "/" + s))
    for f in file_sort:
      new_entry = indentStr + [f + "/"] if os.path.isdir(root_name + "/" + f) else indentStr + [f]
      listFiles.append(new_entry)
      getFiles("{}/{}".format(root_name, f), listFiles, indent + 1)
    return listFiles

  
listofFiles = getFiles(ROOT_PATH, [[ROOT_PATH + "/"]], 1)
with open("testing.csv", "w") as csvFile:
  writer = csv.writer(csvFile)
  writer.writerows(listofFiles)
  
