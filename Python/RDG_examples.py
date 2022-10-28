"""RDG_examples

In this file examples of how to use the functions created in the RDG script (the RDG script could be found in the same directory of this file).
"""

"""Imports"""
from RDG import *
from RDG_lists_csv_to_lists import *

"""Variabels that could be changed"""
number_of_products_ = 3
product_maximum_price_ = 10000
number_of_categories_ = 3
number_of_subcategories_ = 2
number_of_suppliers_ = 2
max_items_to_order_from_supllier_ = 100
number_of_customers_ = 30
number_of_sales_ = 18
maximum_product_H_ = 12
maximum_product_WID_ = 12
maximum_product_D_ = 12
maximum_product_WEIGHT_ = 12
length_unit_ = 'CM'
weight_unit_ = 'KG'
n_of_orders_from_suppliers_ = 12

"""Example 1 - Creating random data about products"""

random_products = product_table(n = number_of_products_, product_names_list = product_names_list, product_maximum_price = product_maximum_price_, product_number_of_categories = number_of_categories_, product_number_of_subcategories = number_of_subcategories_, product_number_of_suppliers = number_of_suppliers_)
#print(random_products)

"""Example 2 - Creating random categories"""

random_categories = product_categories_table(n = number_of_categories_, categories_names_list = product_categories_names)
#print(random_categories)

"""Example 3 - Creating random subcategories"""

random_subcategories = product_subcategories_table(number_of_subcategories_, product_subcategories_names, number_of_categories = number_of_categories_)
#print(random_subcategories)

"""Example 4 - Creating random products dimensions"""

random_products_dim = product_dim_table(n = number_of_products_, product_max_H = maximum_product_H_, product_max_WID=maximum_product_WID_, product_max_DEP=maximum_product_D_, product_max_weight=maximum_product_WEIGHT_, length_unit=length_unit_, weight_unit=weight_unit_)
#print(random_products_dim)

"""Example 5 - Creating random suppliers"""

random_suppliers = suppliers_table(number_of_suppliers_, suppliers_names, supplier_adresses)
#print(random_suppliers)

"""Example 6 - Creating random customers"""

random_customers = customers_table(n = number_of_customers_, first_names_list = customer_first_names, last_names_list = customer_last_names, companies_list = customer_comapnies_names, addresses_list = customer_addresses, cities_list = customer_cities, states_list = customer_states, phones_list = customer_phones)
#print(random_customers)

"""Example 7 - Creating random orders from suppliers"""

random_orders_from_suppliers = OFS_table(n_of_orders_from_suppliers_, 2010, 5, 28, 2022, 7, 30, number_of_products_, number_of_suppliers_)
#print(random_orders_from_suppliers)

"""Example 8 - Creating random sales data"""

random_sales = sales_table(number_of_sales_, number_of_customers_, 2009, 10, 14, 2022, 10, 14)
#print(random_sales)

"""Example 9 - Creating random OFS_products data"""

OFS_products_random_data = OFS_products_table(random_orders_from_suppliers, number_of_products_)
#print(OFS_products_random_data)

"""Example 10 - Creating random sales_products data"""

sales_products_random_data = sales_products_table(random_sales, number_of_products_)
#print((sales_products_random_data))