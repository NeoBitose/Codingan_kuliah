def fibonacci(n) :
  if n < 1 :
    return n
  elif n == 1 :
    return 1
  else :
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
print(fibonacci(7))
print(fibonacci(10))
print(fibonacci(4))