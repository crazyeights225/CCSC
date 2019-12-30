#crazyeights225
#Convert files, and stdin to and from morse code
#DEC 2016
morse={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..',
'j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...',
't':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','0':'-----','1':'.----',
'2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','.':'.-.-.-',',':'--..--','?':'..--..','/':'--..-.','@':'.--.-.'}

def file_in_plaintext():
	output_morse=''
	file_name=raw_input("Enter the name:")
	file_in=open(file_name, "r")
	for line in file_in:
		for word in line.split():
			for letter in word:
				for key in morse.iterkeys():
					if(key==letter):
						output_morse=output_morse+" "+(morse[key])
	file_in.close()
	return output_morse

def text_inplaintext(text):
	output_morse=''
	for word in text.split():
		for letter in word:
			for key in morse.iterkeys():
				if(key==letter):
					output_morse=output_morse+" "+(morse[key])
					
	return output_morse

def file_in_morse():
	output_morse=''
	file_name=raw_input("Enter the name: ")	
	file_in=open(file_name, "r")
	for line in file_in:
		for word in line.split():
				for key,value in morse.iteritems():
					if(value==word):
						output_morse=output_morse+" "+(key)	
	return output_morse

def text_inmorse(text):
	output_morse=''
	for word in text.split():
		for key, value in morse.iteritems():
			if(value==word):
				output_morse=output_morse+" "+(key)

	return output_morse
	
print "MORSE CODE"
input_type=raw_input('Enter input type, F for file, and T for text:')
if input_type=='F':
	text_type=raw_input('Enter text type, M for morse, P for plain:')
	if text_type=='M':
		print file_in_morse()
	if text_type=='P':
		print file_in_plaintext()
if input_type=='T':
	text_type=raw_input('Enter text type, M for morse, P for plain:')
	if text_type=='M':
		text=raw_input("Enter text:")
		print text_inmorse(text)
	if text_type=='P':
		text=raw_input("Enter text:")
		print text_inplaintext(text)
	



