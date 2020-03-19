# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:12:34 2020

@author: Aviral Gaur
"""

alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

       
     
sop = caesar_encrypt("I am legend")        



# Caesar  crack decryption ----------------------------#
#the code will crack the key of the encryption in which the code was encrypted
# this is a brute force approach

def caesar_crack(cipher_text):
    
    
    #plain_text = plain_text.upper()
    
    for key in range(len(alpha)):
        plain_text = ""
        for c in cipher_text:
            
            index = alpha.find(c)# finds the index of the character
        
            plain_text = plain_text + alpha[(index-key)%len(alpha)]
        print('with key : %s, the result is : %s' %(key,plain_text))
        

caesar_crack("JABNAMFHFOE")

dop = caesar_decrypt(sop)