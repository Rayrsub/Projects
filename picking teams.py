#importing the module called Random.
import random

#list of players and the two teams.
available_players = ['Anastasia', 'Eli', 'Jamal', 'Jada', 'Theo', 'Michelle',
                     'Adam', 'Rhea', 'Charlie', 'Jasmine' 'Marley', 'Kenji',
                     'Sydney', 'Yara']

jaleesas_team = ['Jaleesa']

rahims_team = ['Rahim']

#this loop will continue to run until teams are picked.
while len(jaleesas_team) < 8:
    player_selected = random.choice(available_players)
    jaleesas_team.append(player_selected)
    available_players.remove(player_selected)

#for loop to add remaining players to Rahim's team.
rahims_team.extend(available_players)

#Prints all players on their respected teams.
print("Jaleesa's Team")
print(*jaleesas_team, sep = ", ")

print("Rahim's Team")
print(*rahims_team, sep = ", ")

