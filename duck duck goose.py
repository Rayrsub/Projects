duck = 'Duck'
goose = 'GOOSE!'
not_it = 'No'
tag = 'RUN!'
x = 10
while x <= 30:
    print(duck + " " + not_it)
    if x == 25:
        print(goose + " " + tag)
        break
    x += 1
