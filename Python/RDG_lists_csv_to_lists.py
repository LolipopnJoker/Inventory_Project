"""RDG_lists_csv_to_lists

This file is part of the INVENTORY project.

In order to create random data, I had to create a dataset to randomly choose from.
This dataset contains private names, brand names, suppliers name, etc. This script
loads this file and turns each column to a list. The function in the connecting_dots
module will use those lists to generate random data.
While writing this dataset in a form of lists inside the code is possible, I think
it would be cleaner to create a csv file and import it from there.
"""

"""Imports"""
import csv
import os

os.chdir('G:/My Drive/Portfolio/Multi-Tools Projects/Inventory Project/Python')

"""Importing the csv file"""
csv_file = open('RDG_lists.csv', encoding='utf-8-sig')
reader = csv.DictReader(csv_file)

"""Creating empty lists"""
product_names_list, product_categories_names, product_subcategories_names, suppliers_names, supplier_adresses = ([] for i in range(5))
customer_first_names, customer_last_names, customer_comapnies_names, customer_addresses, customer_cities, customer_states, customer_phones = ([] for i in range(7))

for row in reader:
    product_names_list.append(row['product_names_list'])
    product_categories_names.append(row['categories_names_list'])
    product_subcategories_names.append(row['subcategories_names_list'])
    suppliers_names.append(row['suppliers_names_list'])
    supplier_adresses.append(row['supplier_adresses'])
    customer_first_names.append(row['customer_first_names'])
    customer_last_names.append(row['customer_last_names'])
    customer_comapnies_names.append(row['customer_comapnies_names'])
    customer_addresses.append(row['customer_addresses'])
    customer_cities.append(row['customer_cities'])
    customer_states.append(row['customer_states'])
    customer_phones.append(row['customer_phones'])
