# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:00:42 2020

@author: Aviral Gaur
"""
# program for vignere Encryption



alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#alpha.find('A')
def vig_encrypt(plain_text, key):
    cipher_text = ''
    key_index = 0
    
    plain_text = plain_text.upper()
    key = key.upper()
    for char in plain_text:
        
        
        
        #formula for vignere cipher
        index = (alpha.find(char)+(alpha.find(key[key_index])))%(len(alpha))
        
        cipher_text = cipher_text + alpha[index]
        
        key_index = key_index + 1
        
        if key_index == (len(key)):
            key_index = 0
        
        
    return cipher_text
        

text = "articles every common noun with some exceptions is expressed with a certain definiteness definite or indefinite as an attribute similar to the way many languages express every noun with a certain grammatical number singular or plural or a grammatical gender. Articles are among the most common words in many languages in English for example the most frequent word is the."
p_key = "employee"

c_text = vig_encrypt(text, p_key)

print("the plain text is : ", text) 
print("the cipher text is : ", c_text)










