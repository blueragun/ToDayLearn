def print_formatted(number):
  k = len(list(format(n, 'b')))  
  for i in range(1, n+1) :
    print(str(i).rjust(k), str(format(i, "o")).rjust(k), (str(format(i, "x")).upper()).rjust(k), str(format(i, "b")).rjust(k))


n = int(input())
print_formatted(n)
