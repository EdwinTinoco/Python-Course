"""
You have been given a raw data dump that has an array of objects. The objects keys are companies, 
and the values are arrays of emails followed by a 3 digit department number. I need you to write 
a program that will go through the data, print the emails for each company and what department 
number that email belongs to.
"""

data = [
{ "Google": ["test@test.com 123", "test@test.com 321", "test@test.com 451", "test@test.com 123" ]},
{ "Yahoo": ["test@test.com 123", "test@test.com 321", "test@test.com 451", "test@test.com 451" ]},
{ "IBM": ["test@test.com 888", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
{ "GREGS": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
{ "AUTO SHOP": ["test@test.com 888", "test@test.com 555", "test@test.com 555", "test@test.com 123" ]},
{ "PAWN SHOP": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Nike": ["test@test.com 123", "test@test.com 123", "test@test.com 555", "test@test.com 123" ]},
{ "Franks": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]},
{ "Tims": ["test@test.com 123", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
{ "Apple": ["test@test.com 123", "test@test.com 555", "test@test.com 123", "test@test.com 123" ]},
{ "Sony": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Disney": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
{ "Popies": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Sally": ["test@test.com 123", "test@test.com 555", "test@test.com 888", "test@test.com 123" ]},
{ "Henry": ["test@test.com 123", "test@test.com 555", "test@test.com 555", "test@test.com 555" ]},
{ "Dave's": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]}
]

#Jess example
def companies(data):
    for dictionary in data:
        company_name = list(dictionary.keys())[0]
        values = list(dictionary.values())[0]
        print(f'Company: {company_name}')

        for emails in values:
            emails = emails.split()
            print(f'Email: {emails[0]}    Department Number: {emails[1]}')
    print("")
        

companies(data)


#Ryan example
def format_data(data):
    for i in range(len(data)):
        dictionary = data[i]
        for key in dictionary:
            dictionary_values = dictionary.get(key)
            print(f'\nCompany: {key}')
            for val in dictionary_values:
                print(f'Email: {val[:-4]}, Department: {val[-4:]}')


format_data(data)

