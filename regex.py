import re

text = "The agent's phone number is 408-555-1234. Call soon!"

pattern = 'phone'
re.search(pattern, text)
# returns a match object

match = re.search(pattern, text)

match.span()
#returns (12, 17)
match.start()
#returns 12
match.end()
#returns 17

#search only returns the first in the string

newtext = 'my phone once, my phone twice'

matches = re.findall(pattern, newtext)
# matches is a list ['phone', 'phone']

for match in re.finditer(pattern, newtext):
  print(match)

#returns each match object