# Dictionary that stores the audition sign-ups.
auditions = {
    "Principal" : {
        },
    "Teacher" : {
        },
    "Troublemaker" : {
        },
    "Student" : {
        }
    }

# Functions for sign-up processing.
def sign_up():
    name = input("What is yout name? ").capitalize()
    grade = (input("What is your grade? (Please respond with a number) "))
    role = input('''What is your preferred role? please select a number from \
the following options:
                [1] Principal
                [2] Teasher
                [3] Troublemaker
                [4] Student
                ''')
    if role == '1':
        auditions['Principal'][name] = grade

    elif role == '2':
        auditions['Teacher'][name] = grade

    elif role == '3':
        auditions['Troublemaker'][name] = grade

    else:
        auditions['Student'][name] = grade

# For-loop that calls the sign_up() function 12 times.
for i in range(5):
    sign_up()

# Printout for the list of students signed up to audition.
print("Sign-ups for 'A Day without a Principle' are now closed!")

print("Role: Principal")
for student, grade in auditions['Principal'].items():
    print(student, grade)
print("Role: Teacher")
for student, grade in auditions['Teacher'].items():
    print(student, grade)
print("Role: Troublemaker")
for student, grade in auditions['Troublemaker'].items():
    print(student, grade)
print("Role: Student")
for student, grade in auditions['Student'].items():
    print(student, grade)
