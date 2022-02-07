#Bot greeting.
def greeting():
    name = input('Thanks for contacting Tiny Space! May I have your name? ').capitalize()

#Inquiry category.
def select_category():
        category = input('Please select one of the categories below using the \
numbers 1-5. \n[1] Store Hours & Locations \n[2] Statue of order \n[3] Issue with \
order \n[4] Design and Services \n[5] Other \n')

        if category == '1':
            store_location_hours()
            return

        if category == '2':
            order_status()
            return

        if category == '3':
            order_issue()
            return

        if category == '4':
            design_services()
            return

        if category == '5':
            other()
            return

        if category not in ['1', '2', '3', '4', '5']:
            select_category()

#Category: Store Hours and Location.
def store_location_hours():
    location = '2300 Riverdale Lane \
Boston, MA 02101'

    hours = 'Monday - Saturday from 10AM to 6PM'

    print(f'Tiny Space is located at {location}. \
\nThe store is open {hours}. ')

    additional_question = input('May I help with anything else? [Yes/No] ').lower()
    if additional_question == 'yes':
        select_category()

    elif additional_question == 'no':
            print('Thanks for contacting Tiny Space!')
            return

#Category: Status of Order.
def order_status():
    print('Sure I can help with that. ')

    full_name = input('May I have the full name on the order? ')

    order_number = input('May I have the Order number? ')

    transfer_Elliot()
    return

#Category: Issue with Order.
def order_issue():
    print("I'm Sorry that you're experiencing issues with your order.")

    full_name = input('May I have the full name on the order? ')

    order_number = input('May I have the Order number? ')

    issue = ('Could you please describe the issue with your order? ')

    transfer_Charissa()
    return

#Category: Desgin Services.
def design_services():
    print('I can definitely help you out with your design questions!')

    transfer_Ramon()
    return

#Category: Other
def other():
    transfer_Trinity
    return

#Category: Transfer to Tiny Space Team.
def transfer_Elliot():
    print("Awesome! I'm checking the status of the order now.")
    return

def transfer_Charissa():
    print("Thanks for providing that information. I'm looking into this now.")
    return

def transfer_Ramon():
    design_question = input('Tell me how i may be of assistance. ')
    return

def transfer_Trinity():
    other_inquiry = input("No problem, please describe to me how i may be of assistance. ")

#Call the functions to start the chat bot.
greeting()
select_category()
