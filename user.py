import random  # Import the random module
import math

def userProfile(first_name, last_name):
    email_providers = ['@gmail.com', '@yahoo.com', '@outlook.com','@hotmail']
    #Include a number is some emails
    number = random.randint(1, 100)
    if number < 10:
        number = ''
    email_body = [first_name, last_name, str(number)]  
    # Shuffle the email_body list in-place
    random.shuffle(email_body)  
    # concatenate the elements in email_body
    email = "".join(email_body)  
    # Use random.randint to get a random index
    rand_index = random.randint(0, len(email_providers) - 1)  
    # Concatenate the selected email provider
    email += email_providers[rand_index]  
    return {
        'first_name': first_name,  
        'last_name': last_name,
        'email': email  
    }
