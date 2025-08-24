#this program uses clipboard wich is not build in module in python so you need to install it using:
#pip install clipboard

import json
import clipboard
from pathlib import Path

#constants
FILE_NAME = "clipboards.json"
MODES = ["save","load","delete","list","quit"]

#saving some content to specific path
def save_items(path,contents):
    with open(path,"w") as jf:
        json.dump(contents,jf)

#loading some content from a specific path
def load_items(path):
    with open(path,"r") as jf:
        data = json.load(jf)
        return data

#loading the data and creating the file if it doesn't exist:
if Path(FILE_NAME).exists():
    data = load_items(FILE_NAME)
else:
    with open(FILE_NAME,"w") as jf:
        jf.write("{}")
    data = load_items(FILE_NAME)

#defining the mode and key
while True:

    #asking the user for the mode
    mode = input(f"Hello user, choose one mode {MODES}: ").strip().lower()

    #save mode
    if mode == "save":

        # asking for the key.
        key = input("Select a key to save on it: ").strip()

        #saving the clipboard on the key
        data[key] = clipboard.paste()
        save_items(FILE_NAME,data)
        print(f"The contents in clipboard saved successfully in \"{key}\"")


    #load mode
    elif mode == "load":

        # asking for an existing key to load:
        while True:
            if len(data.keys()) != 0:
                key = input("Select a key to load it: ").strip()
                if key not in data.keys():
                    print(f"the key: \"{key}\" doesn't exist in the file.")
                    print("this is the list of keys:",list(data.keys()))
                else:
                    # saving the contents of the key in the clipboard
                    clipboard.copy(data[key])
                    print(f"The contents copied to clipboard successfully from \"{key}\"")
                    break
            else:
                print("Their is not items to load!")
                break

    #delete mode
    elif mode == "delete":

        # asking for an existing key to load:
        while True:
            if len(data.keys()) != 0:
                key = input("Select a key to delete it: ").strip()
                if key not in data.keys():
                    print(f"the key: \"{key}\" doesn't exist in the file.")
                    print("this is the list of keys:",list(data.keys()))
                else:
                    # deleting the key and it's contents
                    data.pop(key)
                    save_items(FILE_NAME,data)
                    print(f"The key \"{key}\" and it's content removed successfully!")
                    break
            else:
                print("Their is no items to delete!")
                break

    #showing the list
    elif mode == "list":
        print(list(data.keys()))

    #quit the program
    elif mode == "quit":
        break

    #wrong mode
    else:
        print(f"The mode \"{mode}\" doesn't exist in this program.")
