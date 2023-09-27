#Starting with python programming
print('Hello, world!')
fname = 'jijah' # string
age = '40' # string
person_age = 40 # integer
email = 'jijakhan@gmail.com' # string
contacts = [ 553020508, 204860341 ] # list
telephone = (30553020508, 30204860341 ) # tuple
contact_types = { 'Home': 204860341, 'work': 553020508 } # dictionary
married = False # boolean

print()
print('Fname is', fname, 'it is of type', type(fname))
print('Person age is', person_age, 'it is of type', type(age) )
print('Contact is', contacts, 'it is of type', type(contact_types))
print('Married is', married, 'it is of type', type(married))
print(f'dictionary keys => {contact_types.keys()}')
print(f'dictionary values => {contact_types.values()}')

