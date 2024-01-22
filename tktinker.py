
# Import the tkinter module
import tkinter
from bs4 import BeautifulSoup,SoupStrainer
import urllib.request
import colorama,re,queue,threading
from colorama import Fore
from urllib.parse import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from prettytable import PrettyTable
from tkinter import *
import tkinter as tk


window = tkinter.Tk()
window.title("Website Tester")
window.geometry("1000x500")

  
def set_text_by_button():
    
 driver = webdriver.Chrome()

#provide website url here
 driver.get(sample_text.get())

#get all links
 all_links = driver.find_elements(By.CSS_SELECTOR,"a")


#check each link if it is broken or not
 for link in all_links:
    #extract url from href attribute
     url = link.get_attribute('href')

    #send request to the url and get the result
     result = requests.head(url)

    #if status code is not 200 then print the url (customize the if condition according to the need)
    # win=Tk()
    
  
    
     if result.status_code >= 200 and result.status_code < 230:
          table_frame = tk.Frame(window)
          table_frame.pack()
          labels = []
          row_labels = []
          label = tk.Label(table_frame,fg='green', text=f"{url}          Testing Passed")
          label.grid(padx=10, pady=10) # Position the label in the table
          row_labels.append(label)
          labels.append(row_labels)
     
     elif result.status_code >= 400 and result.status_code < 512:
          table_frame = tk.Frame(window)
          table_frame.pack()
          labels = []
          row_labels = []
          label = tk.Label(table_frame,fg='red', text=f"{url}          Testing Failed")
          label.grid(padx=10, pady=10) # Position the label in the table
          row_labels.append(label)
          labels.append(row_labels)
         
     elif result.status_code >= 300 and result.status_code < 320:
          table_frame = tk.Frame(window)
          table_frame.pack()
          labels = []
          row_labels = []
          label = tk.Label(table_frame,fg='green', text=f"{url}         Testing Passed")
          label.grid(padx=10, pady=10) # Position the label in the table
          row_labels.append(label)
          labels.append(row_labels)
      
set_up_button = tkinter.Button(window, height=1, width=10, text="Test Website", 
					command=set_text_by_button)

sample_text = tkinter.Entry(window,width=75)
sample_text.pack()
placeholder_text = 'Paste link'
sample_text.insert(0, placeholder_text)

set_up_button.pack()



window.mainloop()
