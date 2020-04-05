# 2. Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

flag = True


def data_users(name, surname, year_birth, city, email, phone):
    user_info = dict()
    user_info['name'] = name
    user_info['surname'] = surname
    user_info['year_birth'] = year_birth
    user_info['city'] = city
    user_info['email'] = email
    user_info['phone'] = int('8' + str(phone))
    return user_info


name_ = input('Input name user: ')
surname_ = input('Input name user: ')

while flag:
    year_birth_ = input('Input year birth: ')
    if len(year_birth_) == 4:
        try:
            year_birth_ = int(year_birth_)
            flag = False
        except ValueError:
            print('Entered value is not a year!!!')
    else:
        print('Invalid length of the entered year')

city_ = input('Input city: ')
email_ = input('Input e-mail: ')

flag = True

while flag:
    try:
        phone_ = int(input('Input the Phone number: 8'))
        flag = False
    except ValueError:
        print('Entered Phone number is not a number!!!')

user = data_users(name=name_, surname=surname_, year_birth=year_birth_,
                  city=city_, email=email_, phone=phone_)

print(
    f'Name user: {user["name"]}, Surname user: {user["surname"]}, '
    f'Year birth: {user["year_birth"]}, City: {user["city"]}, '
    f'E-mail: {user["email"]}, Phone: {user["phone"]}'
      )
