import random

e_dict = {}  # Global Variable; Encryption dictionary
d_dict = {}  # Global Variable; Decryption dictionary

def create_key ():
    """ 
    OPTIONAL function -- only create this one once you have completed everything else!

    Creates a new random cipher key and prints the key to the console.  
    The user needs to copy this key into a file if desired.    
    """ 
    e_dict.clear()
    d_dict.clear()
    ALPHABET=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numofalphabet=len(ALPHABET)
    numofcipher=0
    cipher_alphabet=[]
    n=0
    while (numofalphabet!=numofcipher):
        letter=random.randrange(26)
        cipher_letter = ALPHABET[letter]
        if cipher_letter not in cipher_alphabet:
            e_dict[ALPHABET[n]]=cipher_letter
            d_dict[cipher_letter]=ALPHABET[n]
            print(ALPHABET[n] + "\t" + cipher_letter)
            cipher_alphabet.append(cipher_letter)
            n+=1
        numofcipher=len(cipher_alphabet)
    
def load_cipher_file (file_name):
    """ 
    Loads a cipher from the specified file.
    This function sets e_dict to encrypt messages and d_dict to decrypt messages.
    """ 
    text_file= open (file_name,"r")
    e_dict.clear()
    d_dict.clear()
    for line in text_file:
        cipher= line.split("\t")
        
        key=cipher[0]
        
        value=cipher[1].strip("\n")
        
        d_dict[key] = value
        
        e_dict[value] = key
    

def encrypt_message ():
    """ 
    This function asks the user for a message to encrypt.
    It then prints an encrypted version of the message.    

    It is ok if the user enters characters that are not ciphered.  In this case, the 
    character entered by the user will pass directly into the output ciphered message
    without being altered.
    """
    encrypt_this=input("What would you like to encrypt?")
    encrypted_msg=""
    for character in encrypt_this:
        encrypted_char=e_dict.get(character, character)
        encrypted_msg+=encrypted_char
    
    return encrypted_msg

def decrypt_message ():
    """ 
    This function asks the user for a message to decrypt.
    It then prints the decrypted message.    

    If a character in the message is not in the cipher dictionary, print the character
    directly to the output without altering it.
    """ 
    decrypt_this=input("What would you like to decrypt?")
    decrypted_msg=""
    for character in decrypt_this:
        decrypted_char= d_dict.get(character, character)
        decrypted_msg+=decrypted_char
    
    return decrypted_msg

def main():
    """
    Asks the user which cipher file to load.
    Calls load_cipher_file to load the dictionaries.
    Prints the menu.
    Loops until the user decides to quit.
    Calls encrypt_message and decrypt_message as requested by the user.
    """
    choice=" "
    while (choice!="Q"):
        choice=input("L - Load the cipher file \nC - Create a new cipher key\nE - Encrypt a message\nD - Decrypt a message\nQ - Quit\n")
        if (choice == "L"):
            my_file= input("Enter the filename of the cipher to use.")
            load_cipher_file(my_file)
        elif (choice == "C"):
            create_key()
        elif (choice =="D"):
            print(decrypt_message())
        elif (choice =="E"):
            print(encrypt_message())

main()