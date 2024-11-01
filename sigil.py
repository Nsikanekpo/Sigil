def remove_vowels(text):
    vowels = "aeiouAEIOU"
    for char in text:
        if char not in vowels:
           print(f"{char}",sep=" ",end=" ")
    print() # for a new line after the output

# input from the user
user_input = input("State your Desires!: ").strip().upper()


# Print the text without Vowels
remove_vowels(set(user_input))

