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

# or operator |
re.search(r'cat|dog', 'The dog is here')

# WILDCARD is a '.'
re.findall(r'.at', 'The cat in the hat sat there')

# Pattern Starts with ^
re.findall(r'^\d', '2 is a number')

#Pattern ends with '$'
re.findall(r'\d$', 'ends with 4')

phrase = 'there are 3 numbers 34 inside 5 this sentence'

# square brackets with carrot excludes
pattern = r'[^\d]+'

re.findall(pattern,phrase)
#returns a list with numbers excluded

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

clean = re.findall(r'[^!.? ]+', test_phrase)
print(' '.join(clean))


# braces with out the carrot can be used for grouping
textt = 'Only find the hyphen-words in this sentence. but you do not know how long-ish they are'

hyphenpattern = r'[\w]+-[\w]+'
print(re.findall(hyphenpattern, textt))