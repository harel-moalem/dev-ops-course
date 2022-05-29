# my_file = open("urls.txt")
# for line in my_file.readlines():
#     print(line.strip())
from urlcaller import url_caller

def add_name_to_file(name, filename='names.txt'):
    my_file = open(filename, 'a')
    my_file.write(f"{name}\n")
    my_file.close()


def print_from_file(filename='names.txt'):
    my_file = open(filename, 'r')
    for name in my_file.readlines():
        print(f"hello, {name}")
    my_file.close()


def check_url(filename="urls.txt"):
    with open(filename, 'r') as file:
        for url in file.readlines():
            url_caller(url.strip())

#
# for i in range(5):
#     add_name_to_file(input('enter your name:'))
print_from_file()
check_url()


