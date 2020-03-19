# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:05:24 2020

@author: Aviral Gaur
"""


# Caesar encryption ------------------------------  #

def caesar_encrypt(plain_text):
    cipher_text=""
    
    plain_text = plain_text.upper()
    
    for c in plain_text:
        index = alpha.find(c)# finds the index of the character
        
        cipher_text = cipher_text + alpha[(index+key)%len(alpha)]
        
    return cipher_text
        
alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

       
key = int(input("Enter a number"))       
sop = caesar_encrypt("The Glagolitic alphabet is believed to have been created by Saints Cyril and Methodius while the Cyrillic alphabet was invented by Clement of Ohrid who was their disciple.")        


enc = caesar_encrypt(sop)
# Caesar decryption ----------------------------#


def caesar_decrypt(cipher_text):
    plain_text=""
    
    #plain_text = plain_text.upper()
    
    for c in cipher_text:
        index = alpha.find(c)# finds the index of the character
        
        plain_text = plain_text + alpha[(index-key)%len(alpha)]
        
    return plain_text

dec = caesar_decrypt(sop)


print(dec)
print(enc)






















