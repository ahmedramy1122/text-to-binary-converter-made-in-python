def decimal_to_binary(decimal_number) :
	binary_no_list = []
	binary_no_string = ""
	for i in range(0,8) :
		first_phase = decimal_number / 2 
		second_phase = int((first_phase - int(first_phase)) * 2)
		binary_no_list.append(second_phase)
		decimal_number = first_phase
	for no in binary_no_list :
		binary_no_string =  binary_no_string + str(no)
	return binary_no_string[::-1]
def letters_to_decimal(sentence) :
	sentence_letters_list = []
	decimal_list = []
	capital_letters = ["A","B","C","D","E","f","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	small_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	capital_letters_decimal = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
	small_letters_decimal = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
	for str_letter in sentence :
		sentence_letters_list.append(str_letter)
	for letter in sentence_letters_list :
		if letter in capital_letters :
			decimal_list.append(capital_letters_decimal[capital_letters.index(letter)])
		elif letter in small_letters :
			decimal_list.append(small_letters_decimal[small_letters.index(letter)])
		else :
			decimal_list.append(32)
	return decimal_list
def letters_to_binary(sentence) :
	binary_full_string = ""
	decimals_to_convert = letters_to_decimal(sentence)  
	for decimal in decimals_to_convert :
		final_binary = decimal_to_binary(decimal)
		binary_full_string  = binary_full_string +" " + final_binary
	return(binary_full_string)



print(letters_to_binary(input("sentence to convert : \n")))




input("press enter to exit")