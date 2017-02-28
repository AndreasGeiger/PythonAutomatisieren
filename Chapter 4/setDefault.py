spam = {'name': 'Pooka', 'age': 5}
print("Before:")
print(spam)

#Traditional
if 'color' not in spam:
    spam['color'] = 'black'

print("After:")
print(spam)

#With setDefault()

spam.setdefault("color", "white")

print(spam)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
