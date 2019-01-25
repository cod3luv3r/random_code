def revStr(s):

  setVowels = set('aeiou')
  emptyStr = ''

  for i in range(len(s) - 1, -1, -1):
    if s[i] in setVowels:
      emptyStr = emptyStr + s[i]
    else:
      emptyStr = s[i] + emptyStr

  return emptyStr

def revStr1(s):
  return s[::-1]
