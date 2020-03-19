# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:46:26 2020

@author: Aviral Gaur
"""




#Caesar encryption by frequency analysis approach
#In this approach the frequency of the 2nd highest letter in the encryption is 
# calculated and then multiplied with the suitable key
# the 2nd highest is takena as the first one can be white spaces
# key = cipher text freq of 2nd most occuring letter - value of E

import matplotlib.pyplot as plt

alpha = " ABCDEFGHIJKLMNOPQRSSTUVWXYZ"

def freq_analysis(cipher_text):
    
    cipher_text = cipher_text.upper()
    
    letter_freq = {}
    
    for key in alpha:
        letter_freq[key] = 0
        
    for key in cipher_text:
        if key in alpha:
            letter_freq[key] += 1
            
    return letter_freq




    
c_text ="CROJQVKQXVSCSMJKVYRKLOCJSAJLOVSOEONJCXJRKEOJLOOXJM OKCONJLHJAKSXCAJMH SVJKXNJWOCRXNSDAJFRSVOJCROJMH SVVSMJKVYRKLOCJFKAJSXEOXCONJLHJMVOWOXCJXPJXR SNJFRXJFKAJCROS JNSAMSYVOI"
output = freq_analysis(c_text)

#for plotting a bar graph
plt.bar(*zip(*output.items()))
plt.show()

#frequency analysis is a not a accurate method
