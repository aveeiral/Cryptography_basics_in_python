# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:48:45 2020

@author: Aviral Gaur
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:00:42 2020

@author: Aviral Gaur
"""
# program for vignere Encryption



alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#alpha.find('A')
def vig_decrypt(cipher_text, key):
    plain_text = ''
    key_index = 0
    
    cipher_text = cipher_text.upper()
    key = key.upper()
    for char in cipher_text:
        
        
        
        #formula for vignere cipher
        index = (alpha.find(char)-(alpha.find(key[key_index])))%(len(alpha))
        
        plain_text = plain_text + alpha[index]
        
        key_index = key_index + 1
        
        if key_index == (len(key)):
            key_index = 0
        
        
    return plain_text
        

text = "FDIURJJXERKQFWEHTZB BYSTZ PHXRMEXABQOCBHJBIUCLXENEPQLNWJXEUPOUNYMMQLRCWYFVCLSCKNSVIQBCXXEQURXLNYJMDCOGSIJSYZXRJEFEPMBYFYYDYNIRJEXVBU ZWEYAPEWCEAFKPYPLCEQNCSIZLJXMUIDPJXXMUGTPCESAJZOUNYMMQLRCWYFVCLVPFRRNIURZQESGBNTPEXN WF ZWETDPA SWFQMDCOZELWNBYPRNHFYPSTLIJWLPMFRNHQRHLPPJEFZDZVYYMJMB GREHTZB BYATWQHLXLERF NL ZSLZNWQGYNSERCS GXMESDCOCBFRBAQORMJEZDDHYKWJCJQBREATDTLXQEYMRO"
p_key = "employee"

p_text = vig_decrypt(text, p_key)

print("the plain text is : ", text) 
print("the cipher text is : ", p_text)










