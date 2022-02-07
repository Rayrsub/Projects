#input current temp for advice.
temperature = int(input("What is the current temerature? "))

#based off temp an outfit will be suggested.
if temperature >= 80:
    outfit = 'Shorts and dont forget your sunglasses.'
elif temperature <= 79 and temperature >= 60:
    outfit = 'A light jacket or thin sweater.'
else:
    outfit = 'A coat, hat, gloves, and a scarf its cold out.'

#Advice for user.
advice =(f'Today you should wear {outfit}.')

print(advice)
