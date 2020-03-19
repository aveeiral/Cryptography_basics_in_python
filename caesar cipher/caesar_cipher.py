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
sop = caesar_encrypt("I am legend")        



# Caesar decryption ----------------------------#


def caesar_decrypt(cipher_text):
    plain_text=""
    
    #plain_text = plain_text.upper()
    
    for c in cipher_text:
        index = alpha.find(c)# finds the index of the character
        
        plain_text = plain_text + alpha[(index-key)%len(alpha)]
        
    return plain_text

dop = caesar_decrypt(sop)
print(dop)
print(sop)






















