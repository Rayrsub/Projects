#The following is a couple knock knock joke's.

knock_joke = ['Knock', 'Knock', 'Whos There?', 'Yah', 'Yah Who?', \
              'No Thanks, I use Bing or Google.', 'Laughs']

next_joke = ['Knock', 'Knock', 'Whos There?', 'I.O!', 'I.O! Who?', \
             'Me, when are you paying me back?', 'Laughs']

# for loop to break after 'laughs' on first joke.

for knock_joke in knock_joke:
    print(knock_joke)
    if knock_joke == 'Laughs':
        break

# next for loop with two options based off user input. yes prints next
# joke. no  ends conversation.

another_joke = input('Would you like to hear another joke? [Yes/No] ').lower()
if another_joke == 'yes':
    for next_joke in next_joke:
        print(next_joke)
        if next_joke == 'Laughs':
            break
elif another_joke == 'no':
    print('Very well. See you later! Aligator!')
