#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. `2nd_name` is an invalid name, because it begins with a number instead of a letter or underscore.
3. `age` is a valid name, because it only contains alphanumeric characters and is not a reserved word.
4. `total_amount` is a valid name, because it is in snake case and does not contain any special characters.
5. `while` is an invalid name, because it is a reserved word.
6. `Student` is a valid name, because it only contains alphanumeric characters. BUT, it is case sensitive, so it would be different from 'student'.
7. `my-variable` is an invalid name, because it contains the special character '-'. Instead, 'my_variable' should be used.
8. `for` is an invalid name, because it is a reserved word.
9. `_temp` is a valid name, because it begins with an underscore and contains only alphanumeric characters and underscores.
10. `value#` is an invalid name, because it contains the special character '#'.


"""
# Problem 2
"""
1. `calculate_total` is a valid name, because it is in snake case and otherwise only contains alphanumeric characters.
2. `3rd_function` is an invalid name, because it begins with a number when only letters or underscores are permitted.
3. `print_values` is a valid name, because it is in snake case and does not contain any special characters.
4. `find-item` is an invalid name, because it contains the special character '-'. Instead, 'find_item' should be used.
5. `def` is an invalid name, because it is a reserved word in python.
6. `updateProfile` is a valid name, because it does not contain any special characters. BUT, it is important to note that it is case-sensitive.
7. `my_function` is a valid name, because it only contains alphanumeric characters and underscores.
8. `try` is an invalid name, because it is a reserved word in python.
9. `init_data` is a valid name, because it is in snake case and does not contain any special characters.
10. `value@function` is an invalid name, because it contains the special character '@'.


"""
# Problem 3
"""
1. `True and False` is a valid Boolean expression, and will return False.
2. `5 > 3 or "apple" < "banana"` is a valid expression, which will return True. 5 is greater than 3, and 'apple' occurs before 'banana' in the dictionary.
3. `not 10 <= 20` is a valid Boolean expression, and will return False because 10 <= 20 is True.
4. `True or 5 = 4` is not a valid expression, because the '==' operator is needed for comparison.
5. `"apple" != "orange" and 5` is a valid expression, and will return 5. The first portion is True, because the strings are not identical.
6. `3 > 5 not True` is not a valid expression, because the 'not' operand is misused.
7. `False == (3 > 4)` is a valid expression, and will return True because 3 > 4 is False, thus being equivalent to False.
8. `10 <= "10"` is not valid, because it is comparing an integer, 10, and a string, '"10"'.
9. `True or not False` is a valid expression, because True and not False are the same. It will return True.
10. `5 and or 4` is an invalid Boolean expression, because there is no truthiness/falsiness to be evaluated.


"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
