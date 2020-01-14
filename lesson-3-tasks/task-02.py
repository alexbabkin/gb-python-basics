#
# Task 2.
#


def print_user_data(name='Unknown', surname='Unknown',
                    year_of_birth='Unknown', city='Unknown', email='Unknown', phone='Unknown'):
    print(f'Name: {name} \t Surname: {surname} \t Year of birth: {year_of_birth} \t'
          f'Current city: {city} \t Email: {email} \t phone: {phone}')


print_user_data(name='Ivan', surname='Ivanov', phone='555-55-55')
print_user_data(name='Petr', surname='Petrov', email='a@a.com', city='NN')
print_user_data(surname='Sidorov', phone='555-55-57', year_of_birth=1996)
