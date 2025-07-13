# 1
def read_file_lines():
    with open("ABC.txt", "r") as f:
        for line in f:
            print(line.strip())

read_file_lines()

# 2
def count_words():
    with open("ABC.txt", "r") as f:
        content = f.read()
        words = content.split()
        print("Total number of words:", len(words))

count_words()

# 3
def count_uppercase():
    count = 0
    with open("ABC.txt", "r") as f:
        for line in f:
            for char in line:
                if char.isupper():
                    count += 1
    print("Total uppercase letters:", count)

count_uppercase()

# 4
def display_words():
    with open("story.txt", "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) < 4:
                    print(word)

display_words()

