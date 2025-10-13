
#the euclidean Algorithm finds the greatest common divisor (gcd)
def euclidean_algo_divivsion(a, b):
  gcd = 0
  num1 = a
  num2 = b
  while gcd == 0:
    rest = num1 % num2
    if rest == 0:
      gcd = num2
    else:
      num1,num2 = num2,rest
  return gcd

def eucidean_algo_subtraction(a, b):
  num1 = max(a, b)
  num2 = min(a, b)
  while num1 != num2:
    if num1 > num2:
      rest = num1 - num2
    else:
      rest = num2 - num1
    num1, num2 = num2, rest
  return num1
