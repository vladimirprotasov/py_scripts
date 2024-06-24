"""String is  immutable sequence - array of characters"""


test_string = "This is the test string"

# Counting a certain occurrence of chars
check: str = chr(116) + chr(104)  # th
print(test_string.count(check))


print(test_string.lstrip('This '))  # the test string
print(test_string.removeprefix('This '))  # is the test string