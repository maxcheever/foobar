def solution(x):
   translated = ''
   for c in x:
      if 96<ord(c)<123: # if lowercase
         c = chr(219-ord(c)) # 'mirror' letter across m | n
      translated += c

   return translated