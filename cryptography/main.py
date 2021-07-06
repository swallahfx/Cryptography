from art import art
code_source = 'abcdefghijklmnopqrstuvwxyz'


#Encryption block
def encode(encode_text, encode_key):
    encode = ''
    for elem in encode_text:
        if not elem.islower():
            encode +=elem
        else:
            code_index = code_source.find(elem)
            new_code_index = (code_index + int(encode_key))% len(code_source) 
            encode +=code_source[new_code_index]
    print(f"\nHere is your encoded result: {encode}\n")


#Decryption block
def decode(decode_text, decode_key):
    decode = ''
    for elem in decode_text:
        if not elem.islower():
            decode +=elem
        else:
            code_index = code_source.find(elem)
            new_code_index = (code_index - int(decode_key))% len(code_source) 
            decode +=code_source[new_code_index]
    print(f"\nHere is your decoded result: {decode}\n")


print(art)
#Crytography block
def cryptography():
    print("\nWELCOME TO CRYPTOGRAPHY")
    print('''
    
    ''') #selection to encode or decode
    cryptography_option = input("\nType 'encode' to encrypt, type 'decode' to decrypt : ")
    while not(cryptography_option =="encode" or cryptography_option =="decode"):
        cryptography_option = input("\nIncorrect key.Pls input encode or decode correctly to continue: ") 
    print('''
    
    ''')

        #message to encrypt or decrypt
    text = input("Type your message: \n")
    print('''
    
    ''') #encrytion or decryption key
    key = input("\nType your encrytion or decription key between 1 and 10: ")
    print('''
    
    ''')
    if key == '' or key.isspace():
        key = "0"
    else:
        while  not (key.isdigit()) or int(key) > 10: 
            key = input("\n encrytion or decription key must be between 1 and 10: ")
            if key == '' or key.isspace():
                key = "0"   

       #calling of function encode or decode     
    if cryptography_option == "encode":
        encode(text, key)
    elif cryptography_option == "decode":
        decode(text, key)
        
    #re-run the program
    re_run = input("\nType 'yes' if you would like to go again, otherwise 'no': ").lower()
    while re_run != "yes" and re_run != "no":
        re_run = input("\nPls, type 'yes' or 'no' correctly: ")
    if re_run == "yes":
        cryptography()
    if re_run == "no":
        print("\nTHANK YOU FOR USING OUR CRYPTOGRAPHY SERVICE. \n")
        exit()
  
  
cryptography()
