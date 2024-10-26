def sort_string(input_str):
  words_list = input_str.split()
  #A key parameter specifies a function to be executed on each list item before making comparisons.
  words_list.sort(key=str.lower)
  print(' '.join(words_list))

if __name__ == '__main__':
  sort_string("Apple ORANGE banana")
  sort_string("Cigar Toss it in a can It is so tragic")