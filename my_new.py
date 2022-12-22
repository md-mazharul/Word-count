import time


start_time = time.time()

# list of characters to remove from text file
remove = [',', '\'', '-', ';', ':', '.', '(', ')', '$', '“', '_', '”', '=']


# count_words function returns list of words and their recurring frequency
def count_words():
    # create an empty dictionary to store the word counts
    word_counts = {}

    # iterate through the list of words
    for word in words:
        # if the word is not already in the dictionary, add it with a count of 1
        if word not in word_counts:
            word_counts[word] = 1
        # if the word is already in the dictionary, increment its count
        else:
            word_counts[word] += 1

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    # iterate through the word counts dictionary
    for word, count in sorted_word_counts:
        # output each word and its count on a new line
        print(f"{word}: {count}")


# function to remove characters from text file
def remove_chars(s, chars):
    # create a new empty string to store the result
    result = ""

    # iterate through each character in the input string
    for c in s:
        # if the character is not in the list of characters to remove,
        # append it to the result string
        if c not in chars:
            result += c

    # return the resulting string
    return result


with open('filename.txt', encoding='utf8') as file:
    contents = file.read()  # Read the contents of the file
    words = [word.lower() for word in contents.split()]
    modified_words = [remove_chars(word, remove) for word in words]

    print(count_words())

print('\n______________________________________________')
print("Program run for: ", time.time() - start_time)
print('______________________________________________')
