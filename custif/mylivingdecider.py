#!/usr/bin/env python3

## Code quizzes user on what they might like to have in a place they would like to live in
## Code uses input to recommend where user might like to live
message1 = 'You should live in the country'
message2 = 'You should live in the city'

likes1 = ["woods", "farmers market", "apple cider"]
likes2 = ["train", "amusement park", "cinema"]

likes = likes1 + likes2

userchoice = input(f"Enter a word from the following list of likes {likes}: ") #asks users for input

if userchoice.lower() in likes1: #validates user input and parses the list
    print("\n",  message1)
elif userchoice.lower() in likes2:
    print("\n", message2)
else: 
    print("\n", "Please enter a word from the list")
