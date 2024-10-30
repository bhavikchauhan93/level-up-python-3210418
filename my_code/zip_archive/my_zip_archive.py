from zipfile import ZipFile
import os

def zip_archive(path, extension_list, output_zip):
  with ZipFile(output_zip, 'w') as outfile:
    for dirpath, dirnames, filenames in os.walk(path):
      #os.walk yields a 3-tuple (dirpath, dirnames, filenames).
      #dirpath is a string, the path to the directory. 
      #dirnames is a list of the names of the subdirectories in dirpath
      #filenames is a list of the names of the non-directory files in dirpath
      rel_path = os.path.relpath(dirpath, path)
      for file in filenames:
        for type in extension_list:
          if file.lower().endswith(type):
            outfile.write(os.path.join(dirpath, file), arcname=os.path.join(rel_path, file))
      
if __name__ == '__main__':
  zip_archive('my_stuff',['.jpg','.txt'],'my_stuff_modified.zip')