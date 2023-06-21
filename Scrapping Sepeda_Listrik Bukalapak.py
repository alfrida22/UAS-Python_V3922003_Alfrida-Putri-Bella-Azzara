#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
from bs4 import BeautifulSoup
import csv

# Menentukan URL awal yang akan di-scrape
web_url = 'https://www.bukalapak.com/c/sepeda/fullbike/sepeda-listrik?page='

data = []

# Melakukan scraping dari halaman 1 hingga 5
for page in range(1, 6):
    url = web_url + str(page)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    product_items = soup.find_all('div', {'class': 'bl-product-card'})

    for item in product_items:
        # Mencari elemen-elemen dengan tag dan class yang sesuai
        name_elem = item.find('a', {'class': 'bl-link'})
        price_elem = item.find('p', {'class': 'bl-text bl-text--subheading-20 bl-text--semi-bold bl-text--ellipsis__1'})
        address_elem = item.find('span', {'class': 'mr-4 bl-product-card__location bl-text bl-text--body-14 bl-text--subdued bl-text--ellipsis__1'})
        rating_elem = item.find('p', {'class': 'bl-text bl-text--body-14 bl-text--subdued'})
        
        # Memastikan elemen-elemen yang ditemukan tidak None sebelum mengambil teksnya
        if name_elem and address_elem and price_elem and rating_elem:
            name = name_elem.text.strip()
            price = price_elem.text.strip()
            address = address_elem.text.strip()
            rating = rating_elem.text.strip()
            data.append([name, address, price, rating])

# Menentukan nama file CSV untuk menyimpan data
csv_file = 'data sepeda_listrik.csv'

# Membuka file CSV dan menulis data ke dalamnya
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Address', 'Price', 'Rating'])
    writer.writerows(data)
    
print("Data telah disimpan dalam file data sepeda_listrik.csv")


# In[10]:


import pandas as pd

#reading the database
data = pd.read_csv("data sepeda_listrik.csv")

#printing the top 10 rows
display(data.head(10))


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

#reading the database
data = pd.read_csv("data sepeda_listrik.csv")

#scatter plot with address against rating
plt.bar(data['Address'], data['Rating'])

#adding title to the barchart
plt.title("Bar Chart Data Sepeda Listrik")

#setting the x dan y labels
plt.xlabel('Address')
plt.ylabel('Rating')

#saving the figure 
plt.savefig("barchart bukalapak.jpg")

plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

#reading the database
data = pd.read_csv("data sepeda_listrik.csv")

# Menghitung jumlah kemunculan tiap nilai dalam kolom rating
plt.hist(data['Rating']) 

#adding title to the histogram
plt.title("Histogram Data Sepeda Listrik")

#saving the figure 
plt.savefig("histogram sepeda_listrik.jpg")

plt.show()


# In[ ]:




