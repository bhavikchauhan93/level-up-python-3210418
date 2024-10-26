import random
from time import perf_counter

def waiting_game():

  target = random.randint(2, 4)
  print(f"Your target time is {target} seconds\n")

  input("--- Press Enter to Begin ---\n")
  start = perf_counter()

  input(f"...Press Enter again after {target} seconds\n")
  duration = perf_counter() - start
  
  if duration == target:
    print(f"Elapsed time: {duration :.3f} seconds. Right on time!\n")
  elif duration < target:
    print(f"Elapsed time: {duration :.3f} seconds. \n {target - duration :.3f} seconds too fast\n")
  else:
    print(f"Elapsed time: {duration :.3f} seconds. \n {duration - target :.3f} seconds too slow\n")


if __name__ == '__main__':
  waiting_game()