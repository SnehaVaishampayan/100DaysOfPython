import  random

if __name__ == '__main__':
    word_list = ["Apple", "Banana", "Pear", "Oranges"]
    chosen_fruit = word_list[random.randint(0, len(word_list) + 1)]
    guess = input("Enter any letter: ")
    print(chosen_fruit)
    print(guess)

