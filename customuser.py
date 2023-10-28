import random  # Import the random module

def user(first_name="", last_name="",gender=""):
    # Edit the Fields you require in your user model or add more items
    user= ()
    id = id_generator()
    account = 'personal'
    number = mobile_generator()
    dob = dategenerator()
    doh = dategenerator(2012,2023)
    department_id = 6
    designation_id = designation_generator()
    employment_type = employment_type_generator()
    # Django Hashing Algorith for password=Password123
    password = "pbkdf2_sha256$600000$cKHKGWqULdS7YYnid1mG3m$TR9vrZOj+QC6uTNHyFuwfEzeb1RJaO6hW9LvrUN+Sc4="
    sex = gender
    role = "employee"
    work_station = "Head Quarters"
    address = home_address()
    email = email_generator(first_name,last_name)
    is_active = True
    is_staff = False
    is_superuser = False

    user+= (id,account,number,dob,doh,department_id ,designation_id,employment_type,password
            ,sex,role,work_station,address,first_name
            ,last_name,email ,is_active ,is_staff,is_superuser)
    
    return user


def designation_generator():
    # Exclude them from some designations. This is intentional
    excluded = [1,2,3,4,41,42]
    r = random.randint(1, 70)
    if r in excluded:
        r+=5
    return r


def mobile_generator():
    r = str(random.randint(700000000, 799999999))
    num = f"+254{r}"
    return num

def email_generator(first_name="", last_name=""):
    email_providers = ['@gmail.com', '@yahoo.com', '@outlook.com']
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
    email = email.lower()
    email =' '.join(word.strip() for word in email.split())
    return email

def id_generator():
    id = random.randint(1000000000, 9999999999)
    return id

def employment_type_generator():
    choices = ['permanent','temporary', 'contract']
    rand_index =  random.randint(0, len(choices) - 1)  

    return choices[rand_index]


def designation_selector():
    rand_index =  random.randint(1,71)  
    return rand_index

# Use your own cudtom choices for addresses
def home_address():
    choices = [
        'Eldoret' , 'Royalton, Eldoret', 'Annex, Eldoret', 'Eldoret Polytechnic', 'Kololo, Eldoret', 'Moi University Town Campus',
        'Kiplombe, Eldoret','Kipkaren, Eldoret', 'Pioneer Estate, Eldoret', 'Eldoret Sports Club', 'Mwanzo', 'Huruma','Cheramei, Eldoret'
        'Langas, Eldoret', 'Kimumu, Eldoret', 'Mlimani, Eldoret', 'Noble, Eldoret', 'Outspan, Eldoret','Baharini, Eldoret',
        'Kosachei, Eldoret', 'Likuyani, Eldoret', 'Turbo, Eldoret',
        'Elgon View, Eldoret' ,'Kenmosa, Eldoret', 'Kapsoya Eldoret',"Soin, Eldoret", "Fair Mount Heights" , "Kingongo, Eldoret"
    ]
    rand_index =  random.randint(0, len(choices) - 1)  
    return choices[rand_index]

def dategenerator(start_year=1969, end_year=2000):
    random_year = str(random.randint(start_year,end_year))
    random_month = str(random.randint(1,12))
    random_day = str(random.randint(1,30))

    # Account for february which has upto 28 days in the month of February
    if int(random_month) == 2 and int(random_day) > 28:
        day = int(random_day)-3
        random_day = str(day)

    if len(random_month) == 1:
        random_month = '0'+random_month
    if len(random_day) == 1:
        random_day  = '0'+random_day

    date = f'{random_year}-{random_month}-{random_day}'
    
    return date



