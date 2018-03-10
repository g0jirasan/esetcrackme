import random
import sys

#thanks to liveoverflow on youtube
def check_key(key):
	char_sum = 0
	for c in key:
		char_sum += ord(c)
	sys.stdout.write("{0:3} \ {1}		\r".format(char_sum, key))
	sys.stdout.flush()
	return char_sum

password = [0] * 10
charlist = "!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"

key = ""
key2 = ""
key3 = ""
key4 = ""
key5 = ""
key6 = ""
key7 = ""
key8 = ""
key9 = ""
key10 = ""

#TODO: Clean this up and make it less terrible

while True:
	key += random.choice(charlist)
	key2 += random.choice(charlist)
	a = check_key(key)
	b = check_key(key2)
	value1 = a + b
	if value1 > 205:
		key = ""
		key2 = ""
	elif value1 == 205:
		password[7] = a
		password[6] = b
		
	key3 += random.choice(charlist)
	key4 += random.choice(charlist)
	c = check_key(key3)
	d = check_key(key4)
	value2 = c + d
	if value2 > 201:
		key3 = ""
		key4 = ""
	elif value2 == 201:
		password[8] = c
		password[5] = d

	key5 += random.choice(charlist)
	e = check_key(key5)
	value3 = e + 205
	if value3 > 314:
		key5 = ""
	elif value3 == 314:
		password[3] = e

	key6 += random.choice(charlist)
	key7 += random.choice(charlist)
	f = check_key(key6)
	g = check_key(key7)
	value4 = f + g
	value5 = password[8] + value4
	value6 = value5 + password[5]
	if value6 > 367:
		key6 = ""
		key7 = ""
	elif value6 == 367:
		password[4] = f
		password[9] = g
		
		
	key8 += random.choice(charlist)
	key9 += random.choice(charlist)
	h = check_key(key8)
	i = check_key(key9)
	value7 = h + i
	if value7 > 194:
		key8 = ""
		key9 = ""
	elif value7 == 194:
		password[0] = h
		password[1] = i

	key10 += random.choice(charlist)
	j = check_key(key10)
	value8 = password[0] + password[1] + j + password[3] + password[4] + password[5] + password[6] + password[7] + password[8] + password[9]
	if value8 > 923:
		key10 = ""
	elif value8 == 923:
		password[2] = j
		str1 = ''.join(chr(i) for i in password)
		print str1

	