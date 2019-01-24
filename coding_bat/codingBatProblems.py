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

def make_pi():
  return [3, 1, 4]

def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  return False

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  list1 = (nums[1], nums[-1],nums[0])
  return list(list1)

def reverse3(nums):
  emptyArr = []
  for i in range(len(nums)):
    emptyArr.insert(0,nums[i])
  return emptyArr

def max_end3(nums):
  maxInt = max(nums[0], nums[-1])
  return [maxInt, maxInt, maxInt]
  
def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) <= 2:
    return sum(nums)
  return sum(nums[:2])
  
def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  return False

def cigar_party(cigars, is_weekend):
  if is_weekend == True:
    return cigars >= 40
  return 40 <= cigars <= 60

#Logic 2

def lone_sum(a, b, c):
  if a == b == c:
    return 0
  if a == b:
    return c
  if a == c:
    return b
  if b == c:
    return a
  return (a+b+c)

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  return a + b + c

#String 2

def double_char(str):
  empty = ''
  for i in str:
    empty = empty + i * 2 
  return empty

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i] == 'h' and str[i+1] == 'i':
      count +=1
  return count

def cat_dog(str):
  catCount = 0
  dogCount = 0
  for i in range(len(str)-2):
    if str[i] == 'c' and str[i+1] == 'a' and str[i+2] == 't':
      catCount +=1
  for i in range(len(str)-2):
    if str[i] == 'd' and str[i+1] == 'o' and str[i+2] == 'g':
      dogCount +=1
    return catCount == dogCount

def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
      count +=1
  return count

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  sStr = min(len(a), len(b))
  ssStr = min(a, b)
  bStr = max(a, b)
  if bStr[-(sStr):] ==  ssStr:
    return True
  return False

#List 2

def count_evens(nums):
  return len([x for x in nums if x % 2 == 0])

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  nums = nums.sort()
  nums = nums[1:-1]
  return sum(nums) // len(nums)

def sum13(nums):
  sum = 0
  if len(nums) == 0:
    return 0
  for i in nums:
    if i == 13:
      return sum
    sum +=i
  return sum




