import re

p = r'(?:\+\d{2,3})?\d{10}'

t = 'jdnvljcvljnlk 1234567890 +911234567890 s.gnanasri@gid.com   ldsovndsn'

e = re.findall(p,t)

print(e)