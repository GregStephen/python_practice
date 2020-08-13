from collections import Counter
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3]
print(Counter(mylist))

mylist = ['a','a', 10,10,10]
print(Counter(mylist))

print(Counter('aaaaabseasfae'))

sentence = 'How many times does each word show up in this sentence with a word'

print(Counter(sentence.lower().split()))

letters = 'aaaaabbbbbbcccccccdddddd'

c = Counter(letters)

print(c.most_common(2))
'''
Common patterns for Counter() object
sum(c.values()) total of all counts
c.clear() reset all counts
list(c) list unique elements
set(c) convert to a set
dict(c) convert to a reg dictionary
Counter(dict(list_of_pairs))  convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1] n least common elements
c += Counter() remove zero and negative counts
'''

