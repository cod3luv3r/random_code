#Collection of coding bat exercises

#Warmup 2

def string_times(str, n):
  return n * str

def front_times(str, n):
  if len(str) <= 3:
    return n * str
  
  return n * str[:3]

def string_bits(str):
  return str[0:len(str):2]

def string_splosion(str):
  result = ''
  for i in range(len(str)):
    result = result + str[:i+1]
  
  return result
 
