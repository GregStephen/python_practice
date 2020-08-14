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

# \d     a digit
# \w     alphanumeric
# \s     white space
# \D     a non digit
# \W     non-alphanumeric
# \S     non-whitespace


phonenumbertext = 'My phone number is 408-555-1234'

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', phonenumbertext)




# quantifiers

# +       occurs one or more times      
# {3}     occurs exactly 3 times
# {2,4}   Occurs 2 to 4 times
# {3.}    Occurs 3 or more times        \w{3,}    anycharacters
# *       Occurs zero or more times     A*B*C*    AAACC
# ?       Once or none                  plurals?  plural

phone = re.search(r'\d{3}-\d{3}-\d{4}', phonenumbertext)
print(phone)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_pattern, phonenumbertext)
print(results.group(1))