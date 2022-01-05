# Questions 1–5 will be relatively straightforward, while questions 6–8 will be a little more advanced.
# Place your answers in a separate file

# Global Variables
nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

# 1. Find all of the numbers from 1–1000 that are divisible by 8
def divisible_by_eight():
    divis_by_eight = [num for num in nums if num % 8 == 0]
    print(divis_by_eight)

# 2. Find all of the numbers from 1–1000 that have a 6 in them
def find_six():
    contains_six = [num for num in nums if "6" in str(num)]
    print(contains_six)

# 3. Count the number of spaces in a string (use string above)
def count_spaces():
    space_count = len([space for space in string if space == " "])
    print(space_count)

# 4. Remove all of the vowels in a string (use string above)
def remove_vowels():
    new_string = "".join([char for char in string if char not in ['a','e','i','o','u']])
    print(new_string)

# 5. Find all of the words in a string that are less than 5 letters (use string above)
def small_words():
    words = string.split(" ")
    new_word_list = [word for word in words if len(word) < 5]
    print(new_word_list)
    
# 6. Use a dictionary comprehension to count the length of each word in a sentence (use string above)

# 7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)

# 8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by



def main():
    divisible_by_eight()
    find_six()
    count_spaces()
    remove_vowels()
    small_words()

if __name__ == "__main__":
    main()




