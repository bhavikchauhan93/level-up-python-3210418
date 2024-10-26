def prime_factors(number):
  factors = []
  divisor = 2
  prime_list = []

  #Find all primes
  for num in range (2, number+1):
    is_prime = True
    for p in range (2, (num//2)+1):
      if (num % p) == 0:
        is_prime = False
        break
    if is_prime == True:  
      prime_list.append(num)

  #Using prime list find prime factors. 
  while len(prime_list) != 0:
    if number % divisor == 0:
      factors.append(divisor)
      number = number // divisor
    else:
      divisor = prime_list.pop()

  return factors
  
if __name__ == '__main__':
    print(prime_factors(630))
    print(prime_factors(13))
    print(prime_factors(633))