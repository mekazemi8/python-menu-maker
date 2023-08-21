import os
import glob


def getListOfSortedPythonFiles(path):
    files = list(filter(os.path.isfile, glob.glob(os.getcwd() + "\*.py")))
    files.sort(key=os.path.getctime)
    return files


def parseFiles(files_list):
    global menu, counter, list_of_file_names, list_of_file_descs
    menu = 'List of your programs ->\n'
    counter = 1
    list_of_file_names = []
    list_of_file_descs = []
    for any_file in files_list:
        if not os.path.isdir(any_file):
            with open(any_file, 'r') as f:
                pr_name = f.readline().strip()
                pr_desc = f.readline().strip()
                if len(pr_name) > 1 and pr_name[0] == '#':
                    name = pr_name[1:].strip()
                else:
                    name = getFileNameFromFileAddress(any_file)
                if name == 'main': continue
                menu += f'\t{counter}\t{name}\n'
                list_of_file_names.append(any_file)
                list_of_file_descs.append(pr_desc[1:].strip() if len(pr_desc) > 1 and pr_desc[0] == '#' else '')
                counter += 1


def getFileNameFromFileAddress(address, includeMimeType=False):
    file_name = address.split('\\')[-1]
    if not includeMimeType:
        file_name = file_name.split('.')
        file_name = '.'.join(file_name[:-1])
    return file_name


def getSelect():
    try:
        select = int(input("Enter Number of program to RUN (quit => 0): "))
        if select > counter - 1:
            raise Exception
        elif select == 0:
            print('Thanks For Using This Program\n>>>> Good Bye :) <<<<')
            exit()
    except Exception as e:
        print('OOOOps! Please Enter a valid number :(')
        select = getSelect()
    return select


def main():
    print(menu)
    select = getSelect() - 1
    try:
        print('File Address =>', list_of_file_names[select])
        print('\n', list_of_file_descs[select])
    except Exception:
        pass

    print(f'\n<<<{"-" * 35}>>>\n<<<------ Start Program Running ------>>>\n<<<{"-" * 35}>>>')
    __import__(getFileNameFromFileAddress(list_of_file_names[select]))
    print(f'<<<{"-" * 35}>>>\n<<<------- Done! (End Program) ------->>>\n<<<{"-" * 35}>>>\n')
    main()


header = """
             =======================
                Welcome to Python
             =======================
This program will make a menu from your programs
           >>> mekazemi8@gmail.com <<<
<<<<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>>>>"""
if __name__ == '__main__':
    print(header)
    path = os.getcwd()
    files = getListOfSortedPythonFiles(path)
    parseFiles(files)
    main()
