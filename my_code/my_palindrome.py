import re

def clean_string(str_input):
  #Strip leading and trailing whitespaces
  clean_str = str_input.strip()
  #Strip all chacters and only keep alphabets
  clean_str = re.sub(r'[^a-z]', '', clean_str.lower())
  return clean_str

def palindrome(str_input):
  #clean string
  clean_str = clean_string(str_input)

  #check if string is palindrome
  i = 0
  e = len(clean_str)
  is_palindrome = True
  while i <= len(clean_str)/2:
    if clean_str[i] != clean_str[e-1]:
      is_palindrome = False
      break
    else:
      i += 1
      e -= 1
  
  if is_palindrome == True:
    print("String is Palindrome")
  else:
    print("String is NOT a Palindrome")

if __name__ == '__main__':
  palindrome("Go hang a Salami, I'm a lAsagna hog.")
  palindrome("Cigar? Toss it in a can. It is so tragic.")