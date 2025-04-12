# **Assignment 3: Problem-Solving Challenges**

# Problem 1. Write a function that takes a string as input and returns the reversed string.
def reverse_string(input_string):
  return input_string[::-1]

user_input = input("Enter Your Name: ")
reversed_string = reverse_string(user_input)
print(f"The reversed string is: {reversed_string}")


# Problem 2. Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count
 
user_input = input("Write something here. ")
print(count_vowels(user_input))  


# Problem 3. Write a function that takes a non-negative integer and returns the sum of its digits.
def sum_num(n):
    return sum(int(digit) for digit in str(n))


user = input("Enter Some Value: ")
print(sum_num(user))

 
