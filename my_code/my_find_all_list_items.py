def index_all(example, item):
  final = []
  for i in range (len(example)):
    if example[i] == item:
      final.append([i])
    elif isinstance(example[i],list):
      for j in index_all(example[i], item):
        final.append([i]+j)
  
  return final

if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 3, 2]]
    print(index_all(example, 2))
