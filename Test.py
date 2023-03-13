import glob
import os
import shutil

src_folder = r"E:\pynative\reports"
dst_folder = r"E:\pynative\account\\"

# move file whose name starts with string 'emp'
pattern = src_folder + "\emp*"
for file in glob.iglob(pattern, recursive=True):
    # extract file name form file path
    file_name = os.path.basename(file)
    shutil.move(file, dst_folder + file_name)
    print('Moved:', file)