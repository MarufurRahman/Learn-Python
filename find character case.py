# find character case

character = input('Please, input the character: ')

if character >= 'a' and character <= 'z':
	print('Lower Case')
elif character >= 'A' and character <= 'Z':
	print('Upper Case')
else:
	print('Nothing')