import os
import subprocess
import sys


def init_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', '-help', '-?']:
        print('''
        python compile.py [ tex_file_name ]
        
        Starting this program without any arguments will search for the .tex file with the same name as the parent folder.
        If a parameter is given, the program will search for the .tex file with the name [parameter].tex.
        ''')
        exit(0)

    file_name = os.path.split(os.getcwd())[1]
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

    if not os.path.isfile(f"{file_name}.tex"):
        print(f"There is no file with name '{file_name}.tex'")
        exit(1)

    auxiliary_dir = 'auxiliary'
    init_folder(auxiliary_dir)

    commands = [
        ['pdflatex', f'-aux-directory={auxiliary_dir}', f'{file_name}.tex'],
        ['bibtex', f'{auxiliary_dir}/{file_name}.aux'],
        ['pdflatex', f'-aux-directory={auxiliary_dir}', f'{file_name}.tex'],
        ['pdflatex', f'-aux-directory={auxiliary_dir}', f'{file_name}.tex'],
    ]

    for c in commands:
        subprocess.call(c)
