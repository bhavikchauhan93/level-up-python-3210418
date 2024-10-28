#Ideally random function should not be used for cryptographic uses. However, this code was written for logic implementation exercise.
#Uses Diceware Password Generator logic

import random

def get_numbers():
  #List of 5 numbers that will make up a word
  num = [str(random.randint(1,5)) for j in range (5)]
  #Concatinate string of numbers into single string
  num_string = ""
  for n in num:
    num_string += n 
  return num_string

def generate_password(num_of_words):
  with open("diceware.wordlist.asc", "r") as file:
    lines = file.readlines()[2:7778]
    #Create dictionary of number and word pair. Splitting each line by a whitespace
    word_dict = dict(line.split() for line in lines)

    password = ""
    #Get numbers as specifed in the input
    for i in range(num_of_words):
      num_string = get_numbers()
      #Get value from dictionary that matches num_string
      word = word_dict.get(num_string)
      #Concatinate words into single password string
      password = password + " " + word
    return password

if __name__ == '__main__':
  print(generate_password(4))
  print(generate_password(7))