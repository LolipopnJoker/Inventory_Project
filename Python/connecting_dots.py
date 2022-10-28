"""Connecting_dots

Inserting the random generated data into the mysql database named WAREHOUSE.

"""

# Imports

import mysql.connector
#import mysql.connector.plugins
from RDG import *
from RDG_lists_csv_to_lists import *

"""Connecting to database"""
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aRandomPassword",
    database="WAREHOUSE"
    ) # Connecting to MySQL

mycursor = mydb.cursor() # Creating a cursor

"""Choosing amounts of things to create"""

number_of_products_ = 120
product_maximum_price_ = 1000
number_of_categories_ = 9
number_of_subcategories_ = 17
number_of_suppliers_ = 14
max_items_to_order_from_supllier_ = 100
number_of_customers_ = 1000
number_of_sales_ = 1000
maximum_product_H_ = 12
maximum_product_WID_ = 12
maximum_product_D_ = 12
maximum_product_WEIGHT_ = 12
length_unit_ = 'CM'
weight_unit_ = 'KG'
n_of_orders_from_suppliers_ = 15

"""Inserting data"""

"""categories"""

random_categories = product_categories_table(n = number_of_categories_, categories_names_list = product_categories_names) # Generating random categories

for category in range(0, len(random_categories)): # Inserting data into the category table
    category_id_ = random_categories[category][0] # Getting the category id
    category_name_ = random_categories[category][1] # Getting the category name

    mycursor.execute("INSERT INTO Product_Categories (category_id, category_name) VALUES (%s, %s)", (category_id_, category_name_)) # Inserting the data to the table
    mydb.commit()

"""subcategories"""

random_subcategories = product_subcategories_table(number_of_subcategories_, product_subcategories_names, number_of_categories = number_of_categories_) # Generating random subcategories

for subcategory in range(0, len(random_subcategories)): # Inserting data into the subcategory table
    subcategory_id_ = random_subcategories[subcategory][0] # Getting the subcategory id
    subcategory_name_ = random_subcategories[subcategory][1] # Getting the subcategory name
    subcategory_category_id_ = random_subcategories[subcategory][2] # Getting the parent category name

    mycursor.execute("INSERT INTO product_subcategories (subcategory_id, subcategory_name, subcategory_category_id) VALUES (%s, %s, %s)", (subcategory_id_, subcategory_name_, subcategory_category_id_)) # Inserting the data to the table
    mydb.commit()


"""suppliers"""

random_suppliers = suppliers_table(number_of_suppliers_, suppliers_names, supplier_adresses) # Generating random suppliers

for supplier in range(0, len(random_suppliers)): # Inserting data into the suppliers table
    supplier_id_ = random_suppliers[supplier][0] # Getting the supplier id
    supplier_name_ = random_suppliers[supplier][1] # Getting the supplier name
    supplier_adress_ = random_suppliers[supplier][2] # Getting the supplier address

    mycursor.execute("INSERT INTO Suppliers (supplier_id, supplier_name, supplier_adress) VALUES (%s, %s, %s)", (supplier_id_, supplier_name_, supplier_adress_)) # Inserting the data to the table
    mydb.commit()


"""products"""

random_products = product_table(n = number_of_products_, product_names_list = product_names_list, product_maximum_price = product_maximum_price_, product_number_of_categories = number_of_categories_, product_number_of_subcategories = number_of_subcategories_, product_number_of_suppliers = number_of_suppliers_)

for product in range(0, len(random_products)):
    product_id_ = random_products[product][0]
    product_name_ = random_products[product][1]
    product_price_ = random_products[product][2]
    product_category_ = random_products[product][3]
    product_subcategory_ = random_products[product][4]
    product_supplier_ = random_products[product][5]
    
    mycursor.execute("INSERT INTO Products (product_id, product_name, product_full_price, product_category_id, product_subcategory_id, product_supplier_id) VALUES (%s, %s, %s, %s, %s, %s)", (product_id_, product_name_, product_price_, product_category_, product_subcategory_, product_supplier_))
    mydb.commit()

"""product_dim"""

random_products_dim = product_dim_table(n = number_of_products_, product_max_H = maximum_product_H_, product_max_WID=maximum_product_WID_, product_max_DEP=maximum_product_D_, product_max_weight=maximum_product_WEIGHT_, length_unit=length_unit_, weight_unit=weight_unit_)

for product_ in range(0, len(random_products_dim)):
    product_id_ = random_products_dim[product_][0]
    product_H_CM_ = random_products_dim[product_][1]
    product_WID_CM_ = random_products_dim[product_][2]
    product_DEP_CM_ = random_products_dim[product_][3]
    product_H_INCH_ = random_products_dim[product_][4]
    product_WID_INCH_ = random_products_dim[product_][5]
    product_DEP_INCH_ = random_products_dim[product_][6]
    product_weight_KG_ = random_products_dim[product_][7]
    product_weight_LBS_ = random_products_dim[product_][8]

    mycursor.execute("INSERT INTO products_dim (product_DIM_id, product_H_CM, pruduct_Wid_CM, pruduct_D_CM, product_H_INC, pruduct_Wid_INC, pruduct_D_INC, product_weight_KG, product_weight_LBS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (product_id_, product_H_CM_, product_WID_CM_, product_DEP_CM_, product_H_INCH_, product_WID_INCH_, product_DEP_INCH_, product_weight_KG_, product_weight_LBS_))
    mydb.commit()


"""Orders From Suppliers"""

random_orders_from_suppliers = OFS_table(n_of_orders_from_suppliers_, 2010, 5, 28, 2022, 7, 30, number_of_products_, number_of_suppliers_)

for OFS_ in range(0, len(random_orders_from_suppliers)):
    OFS_id_ = random_orders_from_suppliers[OFS_][0]
    OFS_oredered_date_ = random_orders_from_suppliers[OFS_][1]
    OFS_oreder_received_date_ = random_orders_from_suppliers[OFS_][2]
    OFS_total_number_of_items_ = random_orders_from_suppliers[OFS_][3]
    OFS_supplier_id_ = random_orders_from_suppliers[OFS_][4]

    mycursor.execute("INSERT INTO Orders_From_Sup (OFS_id, OFS_oredered_date, OFS_oreder_received_date, OFS_total_number_of_items, OFS_supplier_id) VALUES(%s, %s, %s, %s, %s)", (OFS_id_, OFS_oredered_date_, OFS_oreder_received_date_, OFS_total_number_of_items_, OFS_supplier_id_))
    mydb.commit()


"""OFS_products"""

OFS_products_random_data = OFS_products_table(random_orders_from_suppliers, number_of_products_)

for OFS_Product_ in range(1, len(OFS_products_random_data)):
    OFS_item_order_id_ = OFS_products_random_data[OFS_Product_][0]
    OFS_item_id_ = OFS_products_random_data[OFS_Product_][1]

    mycursor.execute("INSERT INTO Orders_From_Sup_Items (OFS_item_order_id, OFS_item_id) VALUES (%s, %s)", (OFS_item_order_id_, OFS_item_id_))
    mydb.commit()

"""Customers table"""

random_customers = customers_table(n = number_of_customers_, first_names_list = customer_first_names, last_names_list = customer_last_names, companies_list = customer_comapnies_names, addresses_list = customer_addresses, cities_list = customer_cities, states_list = customer_states, phones_list = customer_phones)

for customer_ in range(0, len(random_customers)):
    customer_id_ = random_customers[customer_][0]
    customer_first_name_ = random_customers[customer_][1]
    customer_last_name_ = random_customers[customer_][2]
    customer_company_name_ = random_customers[customer_][3]
    customer_address_ = random_customers[customer_][4]
    customer_city_ = random_customers[customer_][5]
    customer_state_ = random_customers[customer_][6]
    customer_phone_ = random_customers[customer_][7]
    customer_gender_ = random_customers[customer_][8]
    customer_birthdate_ = random_customers[customer_][9]

    mycursor.execute("INSERT INTO Customers (customer_id, customer_first_name, customer_last_name, customer_company, customer_address, customer_city, customer_state, customer_phone, customer_gender, customer_birthdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (customer_id_, customer_first_name_, customer_last_name_, customer_company_name_, customer_address_, customer_city_, customer_state_, customer_phone_, customer_gender_, customer_birthdate_))
    mydb.commit()

"""Sales table """

random_sales = sales_table(number_of_sales_, number_of_customers_, 2009, 10, 14, 2022, 10, 14)

for sale_ in range(0, len(random_sales)):
    sale_id_ = random_sales[sale_][0]
    sales_customer_id_ = random_sales[sale_][1]
    sales_time_ = random_sales[sale_][2]

    mycursor.execute("INSERT INTO Sales (sale_id, sales_customer_id, sales_time) VALUES (%s, %s, %s)", (sale_id_, sales_customer_id_, sales_time_))
    mydb.commit()

"""Creating random sales_products data"""

sales_products_random_data = sales_products_table(random_sales, number_of_products_)

for sale_product_ in range(1, len(sales_products_random_data)):
    Sales_Products_sale_id_ = sales_products_random_data[sale_product_][0]
    Sales_Products_product_id_ = sales_products_random_data[sale_product_][1]
    
    mycursor.execute("INSERT INTO Sales_Products (Sales_Products_sale_id, Sales_Products_product_id) VALUES (%s, %s)", (Sales_Products_sale_id_, Sales_Products_product_id_))
    mydb.commit()