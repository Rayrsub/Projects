#this will work out compound interest
principle = float(input('what is the principle amount? '))
time = float(input('length of time saved in years? '))
RATE = 7.75

#here is the fomula
total = principle * (1 + RATE/100) ** time
compInterest = total - principle
print("Your amount made " + str(compInterest))
