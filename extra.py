import math


def convert_radian_to_degrees(radians):
    return 180 / math.pi


def sort_list(list_items, sort_type):
    if sort_type == 'asc' or sort_type == 'desc':
        list_items.sort(reverse=sort_type == 'desc')

def convert_dec_to_bin(num):
    if num == 0:
        return '0'
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num = int(num / 2)
    return binary

def count_vowels(word):
    count = 0
    for char in word:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count = count + 1
    return count

def mask_card(card):
    return card[(len(card) - 4):]

def x_equal_o(string):
    x_count = 0
    o_count = 0
    for char in string:
        if char == 'X':
            x_count = x_count + 1
        elif char == 'O':
            o_count = o_count + 1
    return x_count == o_count

def calculator(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    else:
        return num1 / num2

def calc_price_after_discount(price, discount):
    discount_total = price * discount / 100
    return price - discount_total
def only_integers(data):
    int_list = []
    for num in data:
        if num.isdigit():
            int_list.append(num)
    return int_list

def repeat_characters(string):
    _str = ''
    for s in string:
        _str = _str + s + s
    return _str










