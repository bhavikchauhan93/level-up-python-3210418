import requests
import re
import os

def download_files(url, download_loc):
  file_path = ''
  #create a directory
  if not os.path.isdir(download_loc):
    os.mkdir(download_loc)
  #Change directory to download_loc
  os.chdir(download_loc)
  #Get file name from url
  filename = (url.rsplit('/', 1)[1]).split('.')[0]
  #pattern to be deleted from file name. i.e. word 'image'
  regexPattern = '^[a-z]+'
  #remove 'image' from file name. That leaves with file number.
  #Convert to integer so that we can increment number
  number = int(re.sub(regexPattern, '', filename))
  #Assumption: file names will have number less than 100
  #Craft the file name
  #Run loop until filename not found
  while True:
    if number < 10:
      file_path = f'image00{number}.jpg'
    else:
      file_path = f'image0{number}.jpg'
    
    #Download file from URL
    url = f'http://699340.youcanlearnit.net/{file_path}'
    r = requests.get(url, allow_redirects=False)
    if r.status_code == 200:
      with open(file_path, 'wb') as file:
          file.write(r.content)
      print(f'{file_path} File downloaded successfully')
      #Increment file number
      number += 1
    else:
      print(f'{file_path} Failed to download file')
      #Stop loop url not found
      break

if __name__ == '__main__':
  download_files('http://699340.youcanlearnit.net/image001.jpg', './images')