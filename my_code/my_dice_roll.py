#Using Monte Carlo Method of simulation
import random

def roll_dice(*args, trials=1000000):
  roll_outcome = {}
  i = 0

  #repeat experiment 'trial' times
  for _ in range(trials):
    roll_total = 0
    for dice in args:
      roll = random.randint(1, dice)
      #Total of all dice rolled for an event
      roll_total += roll
    
    #Adding rolled number to dictionary for tacking outcome count
    if roll_outcome.get(roll_total) is not None:
      roll_outcome[roll_total] += 1
    else:
      roll_outcome[roll_total] = 1
    
  #Percentage of occurance
  print("\nProbability")
  for outcome in range(len(args), sum(args) + 1):
    if roll_outcome.get(outcome) is not None:
      print(f'{outcome}\t{roll_outcome[outcome] * 100 / trials :0.2f}%')
    else:
      #If number of trials is significantly lower then dictionary might not contain key, value pair
      print(f'{outcome}\t0%')

if __name__ == '__main__':
  roll_dice(4,6,6)
  roll_dice(4,6,6,20,trials=100)