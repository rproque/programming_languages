#!/usr/local/bin/python3
import os
import make_pretty


def dir_os_walk(path):
    for root, directories, files in os.walk(path):
        print("root:", root)
        for directory in directories:
            print("directory: ", directory)
        for file in files:
            print("file: ", file)

def dir_recursion(path_to_check):

    def dir_list(path):
        contents = os.listdir(path)
        for file in contents:
            full_path = os.path.join(path, file)
            if os.path.isdir(full_path):
                print("Directory: ", full_path)
                dir_list(full_path)
            else:
                if os.path.isfile(full_path):
                    print("     File: ", full_path)

    if os.path.exists(path_to_check):
        print("Directory is: ", path_to_check)
        dir_list(path_to_check)
    else:
        print("Directory does not exist.")



if __name__ == "__main__":
    path_to_check = '/Users/reroque/Desktop/git_code/rproque_git/reference_guide'
    # print(make_pretty.header("DIR: OS.WALK"))
    # dir_os_walk(path_to_check)
    print(make_pretty.header("DIR: RECURSION"))
    dir_recursion(path_to_check)
