# Osiris Team Vigenere Program
# Written by Hayley Owens

import sys
import argparse

#Setup arguement parser
parser = argparse.ArgumentParser(description="Vigenere cipher (encrypt/decrypt)")
parser.add_argument('-e', action='store_true', default=False, help='Encrypt')
parser.add_argument('-d', action='store_true', default=False, help='Decrypt')
parser.add_argument("key", nargs='?')
args = parser.parse_args()

#Dictionaries as the tables cause that's easy to use
alphabet_dict = {chr(x): x-97 for x in range(ord('a'), ord('z')+1)}
value_dict = { x-97: chr(x) for x in range(ord('a'), ord('z')+1)}

def encrypt(key, phrase):
    #Strip anything that's not an alphabet character from key
    key =''.join([i for i in key if i.isalpha()])
    key = key*len(phrase) #Make key as long as phrase 
    key = key[:len(phrase)] #Make sure key is the exact length of the phrase
    encrypted_phrase = ""
    for character in range(len(phrase)):
        if phrase[character].lower() in alphabet_dict: #Check and make sure character is in the dict we're using to encode
            #Encrypt formula
            encrypted_char =value_dict[((alphabet_dict[key[character].lower()] + alphabet_dict[phrase[character].lower()]) % len(alphabet_dict))]
            if phrase[character].isupper(): #Handle upper/lower casing
                encrypted_phrase = encrypted_phrase + encrypted_char.upper()
            else:
                encrypted_phrase = encrypted_phrase + encrypted_char
        else:
            encrypted_phrase = encrypted_phrase + phrase[character]
            key = key[:character] + '-' + key[character:]
    return encrypted_phrase

def decrypt(key, phrase):
    key =''.join([i for i in key if i.isalpha()])
    key = key*len(phrase)
    key = key[:len(phrase)]
    decrypted_phrase = ""
    for character in range(len(phrase)):
        #Decrypt formula
        if phrase[character].lower() in alphabet_dict:
            decrypted_char = value_dict[((len(alphabet_dict) + alphabet_dict[phrase[character].lower()] - alphabet_dict[key[character].lower()])%len(alphabet_dict))]
            if phrase[character].isupper():
                decrypted_phrase = decrypted_phrase + decrypted_char.upper()
            else:
                decrypted_phrase = decrypted_phrase + decrypted_char
        else:
            decrypted_phrase = decrypted_phrase + phrase[character]
            key = key[:character] + '-' + key[character:]
    return decrypted_phrase

while(True):
    #Handle user input
    line = sys.stdin.readline()
    if args.d:
        decrypted_phrase = decrypt(args.key, line)
        sys.stdout.write(decrypted_phrase)
    elif args.e:
        encrypted_phrase = encrypt(args.key, line)
        sys.stdout.write(encrypted_phrase)


