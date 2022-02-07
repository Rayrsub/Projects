#Import Random module into the program.
import random

#Here is available marbles.
collection = ['red', 'pink', 'orange', 'red', 'pink', 'yellow', 'pink', 'yellow']
secret_bag = ['pink', 'blue', 'green', 'orange', 'red', 'purple', 'green', 'blue',
              'blue', 'red', 'green', 'purple', 'yellow', 'red', 'pink', 'red',
              'green', 'yellow']

#Empty list is filled with marbles chosen.
marbles_chosen = []

#Here is how many tries available.
tries_remaining = 5

#Here is the loop for random selecting 5 marbles unless a green marble is found.
#For each marbles selected the number of tries decrease by 1
for x in range(6):
    if tries_remaining > 0:
        selection = random.choice(secret_bag)
    marbles_chosen.append(selection)
    tries_remaining -= 1
    if selection == 'green':
        collection.append(selection)
        secret_bag.remove(selection)
        if ('green' in collection):
            print(f'Awesome! you found a green marble. if you would another marble you have {tries_remaining} pick(s) left.')
            break
else:
    print('Sorry, you are out of picks. Please come back tomorrow and try again!')

print(f'Here are all the marbles that were chosen: {marbles_chosen}')
