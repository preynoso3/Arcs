# args mean I can use as many arguments as possible
def sum(*args):
  total = 0
  for arg in args:
    total += arg
  return total

print(sum(2,3,4,5,64))

# kwargs means using key values(limitless) its a step beyond args 
# kets and values represnted **
def a_sum(**kwargs):
  total = 0
  for key, value in kwargs.items():
    print(f'{key} = {value}')
    total += value
  return total

print (a_sum(x=3, y=5, z=22))