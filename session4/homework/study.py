import collections
user_string = input("Enter a sentence:")
letter_list = list(user_string)

dictionary = {}
#  collections.Counter()

dictionary = collections.Counter(letter_list)
for k,v in dictionary.items():
    print(k,v)