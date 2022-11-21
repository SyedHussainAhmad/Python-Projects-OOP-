import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

class CurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] # --> Converting it to USD first if it is not because USD is our base country.
    
        
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount # --> precision upto 4 decimal places 


if __name__ == '__main__':

    url = 'https://api.exchangerate-api.com/v4/latest/USD'

    c = CurrencyConverter(url)

    currency1 = input("From Country: ")
    from_country = currency1.upper() # --> To avoid any Input error.

    currency2 = input("To Country: ")
    to_country = currency2.upper() # --> To avoid any Input error.

    amount = int(input("Amount: "))
 
    a = c.convert(from_country, to_country, amount)
    print(a)