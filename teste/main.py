# def greet_user():
#     print('Seja bem vindo')

# greet_user()

# def greet_user(user):
#     print('Seja bem vindo', user)

# greet_user('Cassiano')

# def make_pizza(topping = 'bacon'):
#     print('Faça uma pizza de', topping)

# make_pizza()
# make_pizza('calabresa')

# def add_numbers(x, y):
#     return x + y

# soma = add_numbers(15, 35)
# print(soma)

# class dog():
#     def __init__(self, name):
#         self.name = name

#     def sit(self):
#         print(self.name, 'is sitting')

# my_dog = dog('Bilu')
# print(my_dog.name, 'ia a great dog')

# my_dog.sit()

# class sardog(dog):
#     def __init__(self, name):
#         super().__init__(name)

#     def search(self):
#         print(self.name, 'is searching')

# my_dog = sardog('Willie')

# print(my_dog.name, 'is a search dog')
# my_dog.sit()
# my_dog.search()

# filename = 'teste.txt'
# with open (filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print (line)

# filename = 'teste.txt'
# with open (filename, 'w') as file_object:
#     file_object.write('I love programing')

# filename = 'teste.txt'
# with open (filename, 'a') as file_object:
#     file_object.write('\nI love making games\n')

# prompt = 'How many tickets do you need?'
# num_tickets = input(prompt)

# try:
#     num_tickets = int(num_tickets)
# except ValueError:
#     print('Please, try again')
# else:
#     print('Your tickets are printing')

# users = ['val', 'bob', 'mia', 'ron', 'ned']
# first_user = users[0]
# second_user = users[1]
# newest_user = users[-1]
# print(f'primeiro = {first_user}, segundo = { second_user} e ultimo = {newest_user}')

# users[0] = 'valeria'
# users[2] = 'ronald'

# users.append('amy')

# print(users)


# def tabuada():
#     base = int(input('Informe um número para a tabuada\n'))
#     for x in range(0, 11):
#         print(f'{base} * {x} = {base*x}')

# tabuada()
