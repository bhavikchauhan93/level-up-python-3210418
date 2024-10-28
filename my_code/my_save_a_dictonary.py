import json

def save_dictionary_to_file(dict, path):
  with open(path, "w") as outfile:
    json.dump(dict, outfile)

def read_dictionary_from_file(path):
  with open(path, "r") as file:
    data = json.load(file)
  return data

if __name__ == '__main__':
  dict = {"a":"1", "b":"2", "c":"3"}
  path = "./dictionary.json"
  #Save dictionary to file
  save_dictionary_to_file(dict, path)

  #Read dictionary from file
  print(read_dictionary_from_file(path))