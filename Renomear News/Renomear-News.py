import re 
import os 
import shutil

main_folder = r'/home/e-thinkers/Downloads'

def rename_file(file): 
    file_name, file_extension = os.path.splitext(file)
    file_name_html = re.sub(r'\s','_', file_name)

    file_name_html = file_name_html
    return f'{file_name_html}{file_extension}'

def file_loop(root, dirs, files):
    for file in files: 
        if not re.search(r'\.html$', file): 
            continue

        new_file_name = rename_file(file)
        old_file_full_path = os.path.join(root, file)
        new_file_full_path = os.path.join(root, new_file_name)
        
        
        print(f'Renomeando arquivo {file} para {new_file_name}')
        shutil.move(old_file_full_path, new_file_full_path)


def main_loop():
    for root, dirs, files in os.walk(main_folder):
        file_loop(root, dirs, files)


if __name__ == '__main__': 
    main_loop()