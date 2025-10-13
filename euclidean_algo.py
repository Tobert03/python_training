
#the euclidean Algorithm finds the greatest common divisor (gcd)
def euclidean_algo(a, b):
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