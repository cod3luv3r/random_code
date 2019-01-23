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
 
def last2(str):
  if len(str) < 2:
    return 0
  
  last = str[-2:]
  
  count = 0
  
  for i in range(len(str)-2):
    subStr = str[i:i+2]
    if subStr == last:
      count += 1
  
  return count

def array_count9(nums):
  count = 0
  for i in nums:
    if i == 9:
      count +=1
  
  return count
  
def array_front9(nums):
  length = len(nums)
  if length > 4:
    length = 4
  
  for i in range(length):
    if nums[i] == 9:
      return True
    
  return False

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  
  return False

#String 1

def hello_name(name):
  return 'Hello ' + name + '!'

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return '<' + tag + '>' + word + '<' + '/' + tag + '>'

def make_out_word(out, word):
  return out[:2] + word + out[2:]

def extra_end(str):
  return str[-2:] * 3

def first_two(str):
  if len(str) < 2:
    return str
  return str[:2]

def first_half(str):
  return str[:len(str)/2]

def without_end(str):
  return str[1:-1]

def combo_string(a, b):
  if len(a) < len(b):
    return a + b + a
  return b + a + b

def non_start(a, b):
  return a[1:] + b[1:]

def left2(str):
  if len(str) < 3:
    return str
  return str[2:] + str[:2]

#List 1

def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  
  return False

def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  
  return False

def same_first_last(nums):
  if len(nums) < 1:
    return False
  return nums[0] == nums[-1]

