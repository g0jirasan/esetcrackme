import random
import sys
import string

def random_char():

	a = random.choice("!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~")
	return ord(a)

def first():
		
	final_value = 0
	while True:
		a = random_char()
		b = random_char()
		value = a + b
		if value == 205:
			password[7] = a
			password[6] = b
			break 

def second():
	
	final_value = 0
	while True:
		a = random_char()
		b = random_char()
		value = a + b
		if value == 201:
			password[8] = a
			password[5] = b
			break
		
def third():

	final_value = 0
	while True:
		a = random_char()
		value = a + 205
		if value == 314:
			password[3] = a
			break
		
def fourth():

	final_value = 0
	while True:
		a = random_char()
		b = random_char()
		value1 = a + b
		value2 = password[8] + value1
		value3 = value2 + password[5]
		if value3 == 367:
			password[4] = a
			password[9] = b
			break 
 				
def fifth():

	final_value = 0
	while True:
		a = random_char()
		b = random_char()
		value = a + b
		if value == 194:
			password[0] = a
			password[1] = b
			break	

def sixth():
	
	final_value = 0
	while True:
		a = random_char()
		value = password[0] + password[1] + a + password[3] + password[4] + password[5] + password[6] + password[7] + password[8] + password[9]
		if value == 923:
			password[2] = a
			break 
		

def pr_pass():

	str1 = ''.join(chr(i) for i in password)
	print str1


password = [0] * 10
count = 0

while count < 10:



	first()
 	second()
	third()
	fourth()
	fifth()
	sixth()
	pr_pass()
	count += 1

	
	
	
