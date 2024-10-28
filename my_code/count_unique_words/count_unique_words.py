from collections import Counter
#import re

def count_unique_words(path):
  with open(path, encoding='utf8') as f:
    #contents = re.findall(r"[0-9a-zA-Z-']+", f.read())
    contents = f.read()
    words = [word.lower() for word in contents.split()]
    print(f'\nTotal Words: {len(words)}')
    
    count = Counter(words)

    for word in count.most_common(20):
      print(f'{word[0]}\t{word[1]}')
    

if __name__ == '__main__':
  count_unique_words("The Great Gatsby.txt")