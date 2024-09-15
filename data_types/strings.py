"""String is  immutable sequence - array of characters"""

test_string = "This is the test string"

l_strip = test_string.lstrip("This ")  # the test string
check: str = chr(116) + chr(104)
counter = test_string.count(check)  # count th

rem_prefix = test_string.removeprefix("This ")  # is the test string

data_index = test_string.index("test")

is_alpha_false = test_string.isalpha()  # False
is_alpha_true = test_string.replace(" ", "").isalpha()  # True

string_list = test_string.split(" ")
