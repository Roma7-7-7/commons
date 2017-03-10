import sys
from random import choice, randint


def to_array(val):
	if val <= 1: return [0]

	return [i for i in range(1, val)]



MAX_MULTIPLIER=4
MAX_VALUE=40
SECOND_MAX_VALUE=17

FIRST_OPERATIONS = ['+', '-']
OPERATIONS = ['+', '-', '*']
MULTIPLIRES = to_array(MAX_MULTIPLIER + 1)
FIRST_ARGS = to_array(MAX_VALUE)


def can_divide(val):
	for i in range(9, 2, -1):
		if val % i == 0 and val/i <= 10: return True, i

	return False, None

def get_second(val):
	if val < 10:
		return '*', choice(MULTIPLIRES[2:])
	can, div = can_divide(val)
	if can: return '/', div

	operation = choice(['+', '-'])

	if (operation == '-'): return '-', 0 if val == 1 else choice(to_array(val))

	return '+', randint(1, SECOND_MAX_VALUE)


def calculate(first, operation, second):
	if operation == '+': return first + second
	if operation == '-': return first - second
	if operation == '*': return first * second
	return first/second


def generate():
	first = choice(FIRST_ARGS)
	second = choice(to_array(first - 1))
	first_operation = choice(FIRST_OPERATIONS)
	first_result = calculate(first, first_operation, second)

	second_operation, third = get_second(first_result)
	
	return '(' + str(first) + first_operation + str(second) + ')' + second_operation + str(third) + "=" + str(calculate(calculate(first, first_operation, second), second_operation, third))


print("-----------Started-----------")
current_val = 0


while True:
	print("Current value " + str(current_val))
	print(generate())

	value = raw_input()
	if value == "+": current_val = current_val + 1
	elif value == "-" : current_val = current_val - 1