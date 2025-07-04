# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(number):
    """Returns Fizz if number is divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5.
    If not divisible by either 3 or 5, returns the number itself.
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'FizzBuzz'
    """

    ### answer ###
    if (number%3 == 0) and (number%5 == 0): return 'FizzBuzz'
    if (number%3) == 0: return 'Fizz'
    if (number%5) == 0: return 'Buzz'        
    return number


# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.


def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """

    ### answer ###
    output = 0
    for i in range(len(numbers)):
        output += numbers[i]
    return output


# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(string):
    """Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    """

    ### answer ###
    counter = 0
    for i in string.lower():
        if i in ('a', 'i', 'u', 'e', 'o'):
            counter += 1
    return counter


# Question 4

# Write a function that counts the number of repeated characters in a string.


def count_repeats(string):
    """Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """

    ### answer ###
    ### how about if repeated but different string like example: hhhello - what is the output: do we want 3 or 5 ?
    ### this code assume will used logic to summary of repeated string for above example will be 5
    counter = 0
    for i in string:
        if string.count(i) > 1:
            counter += 1
    return counter


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
