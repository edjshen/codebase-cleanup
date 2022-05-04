# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:25:06 2022

@author: edjsh
"""
# to_usd function
#converts a number to currency format with usd sign and two decimal places
def to_usd(my_price):
    return f"${my_price:,.2f}"