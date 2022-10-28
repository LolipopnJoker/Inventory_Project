"""RDG - Random Data Generator

This file consists of 11 functions, each generates random data for different table in the Inventory database.
"""

# Imports
from pickle import NONE
import random
from RDT import random_date_generator

"""Functions that genreate random data"""

def product_table(n: int, product_names_list: list, product_maximum_price: int, product_number_of_categories: int, product_number_of_subcategories: int, product_number_of_suppliers: int) -> list:
    """Creates n new products with random attributes.
    
    Parameters
    ----------
    n: int
        Number of new products to create.
    product_names_list: list
        A list of possible names.
    product_maximum_price: int
        The maximum price of a product.
    product_category_id_list: list
        List of all possible categories id.
    product_subcategory_id_list: list
        List of all possible subcategories id.
    supplier_id: list
        List of all possible suppliers id.

    Returns
    -------
    list
        An nested list of n products, each has 5 random attributes. 
    """

    products_nested_list = [NONE]*n # Empty list, with n empty spots for n random products.

    for i in range(0, n):
        product_id = i + 1 # Automatically generating a product ID
        product_name = random.choice(product_names_list) # Random product name
        product_price = random.randint(1, product_maximum_price) # Random price
        product_category = random.randint(1, product_number_of_categories) # Random category id
        product_subcategory = random.randint(1, product_number_of_subcategories) # Random subcategory id
        product_supplier = random.randint(1, product_number_of_suppliers) # Random supplier id

        product_attributes = [product_id, product_name, product_price, product_category, product_subcategory, product_supplier] # Inserting the product attributes into a list.

        products_nested_list[i] = product_attributes # Inserting the product into the products list 
    
    return products_nested_list

def product_categories_table(n, categories_names_list):
    """Creates n new categories.
    
    Parameters
    ----------
    n: int
        Number of categories to create.
    categories_names_list: list
        A list of names to chose from.

    Returns
    -------
    list
        A nested list of n categories, each has 5 random attributes.
    """

    categories_nested_list = [NONE]*n # Creating an empty list with n times NONE. It would store n lists containing an ID and a name for each category.

    for i in range(0, n):

        category_id = i + 1 # Automatically generating a category ID
        category_name = random.choice(categories_names_list) # Random category name

        category_attribute = [category_id, category_name] # Inserting the category attribute to a list.
        
        categories_nested_list[i] = category_attribute # Inserting the category attributes into a list 
    
    return categories_nested_list

def product_subcategories_table(n: int, subcategories_names_list: list, number_of_categories: int) -> list:
    """Creates n new subcategories.
    
    Parameters
    ----------
    n: int
        Number of categories to create.
    subcategories_names_list: list
        A list of names to chose from.
    number_of_categories: int
        Number of categories.
    
    Returns
    -------
    list
        A nested list of n subcategories, each has 5 random attributes.
    """

    subcategories_nested_list = [NONE]*n # Creating an empty list with n times NONE. It would store n lists containing an ID and a name for each subcategory.

    for i in range(0, n):

        subcategory_id = i + 1 # Automatically generating a subcategory ID
        subcategory_name = random.choice(subcategories_names_list) # Random subcategory name
        category_id = random.randint(1, number_of_categories) # Random category id

        subcategory_attribute = [subcategory_id, subcategory_name, category_id] # Inserting the subcategory attributes into the subcategories list
       
        subcategories_nested_list[i] = subcategory_attribute # Inserting the subcategory attributes into a list
    
    return subcategories_nested_list

def product_dim_table(n: int, product_max_H: int, product_max_WID: int, product_max_DEP: int, product_max_weight: int, length_unit: str, weight_unit: str) -> list:
    """Creates n new subcategories.
    
    Parameters
    ----------
    n: int
        Number of products.
    product_H_list: list
        A list of floats to chose from. This refers to the height of the product.
    product_WID_list: list
        A list of floats to chose from. This refers to the width of the product.
    product_DEP_list: list
        A  list of floats to chose from. This refers to the depth of the product.
    product_weight_list: list
        A  list of floats to chose from. This refers to the weight of the product.
    length_unit: str
        The unit of length measurements. Could be CM or INCH. Default set to CM.
    weight_unit: str     
        The unit of weight measurements. Could be KG or LBS. Default set to KG.
    
    Returns
    -------
    list
        A nested list of n subcategories, each has 5 random attributes.
    """

    product_dim_nested_list = [NONE]*n

    for i in range(0, n):
        product_id = i + 1
        if length_unit == 'CM': # If the data is given in CM, choose random dimensions and convert them to inches
            product_H_CM = random.randint(1, product_max_H)
            product_WID_CM = random.randint(1, product_max_WID)
            product_DEP_CM = random.randint(1, product_max_DEP)
            product_H_INCH = product_H_CM * 0.393700787
            product_WID_INCH = product_WID_CM * 0.393700787
            product_DEP_INCH = product_DEP_CM * 0.393700787
        elif length_unit == 'INCH': # If the data is given in inches, choose random dimensions and convert them to CM
            product_H_INCH = random.randint(1, product_max_H)
            product_WID_INCH = random.randint(1, product_max_WID)
            product_DEP_INCH = random.randint(1, product_max_DEP)
            product_H_CM = product_H_INCH / 0.393700787
            product_WID_CM = product_WID_INCH / 0.393700787
            product_DEP_CM = product_DEP_INCH / 0.393700787
        else: # If the data is not in CM or inches, print an error
            print('Error 1: Not the right length unit. Choose between CM or INCH.')
            break
            
        if weight_unit == 'KG': # If the data is given in KG, choose random weight and convert it to LBS
            product_weight_KG = random.randint(1, product_max_weight)
            product_weight_LBS = product_weight_KG * 2.20462262
        elif weight_unit == 'LBS': # If the data is given in LBS, choose random weight and convert it to KG
            product_weight_LBS = random.randint(1, product_max_weight)
            product_weight_KG = product_weight_LBS / 2.20462262
        else: # If the data is not in KG or LBS, print an error
            print('Error 2: Not the right weight unit. Choose between KG or LBS.')
            break
        
        product_dim_attributes = [product_id, product_H_CM, product_WID_CM, product_DEP_CM, product_H_INCH, product_WID_INCH, product_DEP_INCH, product_weight_KG, product_weight_LBS] # Inserting the products dim attributes to a list
        
        product_dim_nested_list[i] = product_dim_attributes # Inserting the product_dim attributes to a list.
    
    return product_dim_nested_list

def inventory_table(n_aisles: int, n_shelves: int, product_current_stock: int = 0) -> list:
    """Generating random data for the inventory table
    
    Parameters
    ----------
    n_aisles: int
        Number of aisles in the warehouse.
    n_shelves: int
        Number of shelves in the warehouse.
    product_current_stock: int
        The current number items in stock
    """

def suppliers_table(n: int, supplier_name_list: list, supplier_adress_list: list) -> list:
    """Creates n new random suppliers.
    
    Parameters
    ----------
    n: int
        Number of random suppliers to create.
    supplier_name_list: list
        A list of possible names to randomly choose from.
    supplier_adress_list: list
        A list of possible addresses to randomly choose from.
    
    Returns
    -------
    list
        A nested list of n suppliers, each has 2 random attributes.
    """

    suppliers_nested_list = [NONE]*n # Empty list, with n empty spots for n random suppliers.

    for i in range(0, n):
        supplier_id = i + 1 # Automatically generating a supplier ID
        supplier_name = random.choice(supplier_name_list) # Random supplier name
        supplier_adress = random.choice(supplier_adress_list) # Random supplier's address

        supplier_attributes = [supplier_id, supplier_name, supplier_adress] # Inserting the supplier attributes into a list
    
        suppliers_nested_list[i] = supplier_attributes # Inserting the supplier into the suppliers list 
    
    return suppliers_nested_list

def customers_table(n: int, first_names_list: list, last_names_list: list, companies_list: list, addresses_list: list, cities_list: list, states_list: list, phones_list: list) -> list:
    """Generating random data for the customers table
    
    Parameters
    ----------
    n: int
        Number of random customers to create.
    first_name_list: list
        A list of possible first names to randomly choose from.
    last_name_list: list
        A list of possible last names to randomly choose from.
    companies_list: list
        A list of possible companies to randomly choose from.
    addresses_list: list
        A list of possible addresses to randomly choose from.
    cities_list: list
        A list of possible cities to randomly choose from.
    states_list: list
        A list of possible states to randomly choose from.
    phones_list: list
        A list of possible phones to randomly choose from.
    
    Returns
    -------
    list
        A nested list of n customers, each has 7 random attributes.
    """

    customers_nested_list = [NONE]*n # Empty list, with n empty spots for n random customers.

    for i in range(0, n):
        customer_id = i + 1 # Automatically generating a customer ID
        customer_first_name = random.choice(first_names_list) # Random first name
        customer_last_name = random.choice(last_names_list) # Random last name
        customer_company = random.choice(companies_list) # Random comapny
        customer_address = random.choice(addresses_list) # Random customer address
        customer_city = random.choice(cities_list) # Random city
        customer_state = random.choice(states_list) # Random state
        customer_phone_number = random.choice(phones_list) # Random cutomer's phone number
        customer_gender = random.choice(['m', 'f'])
        customer_birthdate = random_date_generator(1980, 1, 1, 2008, 12, 30)

        customer_attributes = [customer_id, customer_first_name, customer_last_name, customer_company, customer_address, customer_city, customer_state, customer_phone_number, customer_gender, customer_birthdate] # Inserting the customer attributes into a list
        customers_nested_list[i] = customer_attributes # Inserting the coustomer into the coustomeres list 
    
    return customers_nested_list

def OFS_table(n: int, OFS_start_year: int, OFS_start_month: int, OFS_start_day: int, OFS_end_year: int, OFS_end_month: int, OFS_end_day: int, OFS_n_products: int, OFS_n_supplieres: int) -> list:
    """Creates n new orders from suppliers with random attributes.
    
    Parameters
    ----------
    n: int
        Number of random orders from suppliers to create.
    start_year: int
        The year when the orderes from suppliers started.
    start_month: int
        The month when the orderes from suppliers started.
    start_day: int
        The day when the orderes from suppliers started.
    end_year: int
        The year when the orderes from suppliers ended.
    end_month: int
        The month when the orderes from suppliers ended.
    end_day: int
        The day when the orderes from suppliers ended.
    OFS_n_products: int
        The total amount of products. Used to create a random number of items in each the order.
    OFS_n_supplieres: int
        The total amount of suplliers. Used to create a random supllier id to each order.
    
    Returns
    -------
    list
        A nested list of n orders from suppliers, each has 4 random attributes.
    """

    OFS_nested_list = [NONE]*n
    
    for i in range(0, n):
        OFS_attributes = [NONE]*5
        
        OFS_id = i + 1 # Automatically generating an OFS ID
        OFS_ordered_date = random_date_generator(OFS_start_year, OFS_start_month, OFS_start_day, OFS_end_year, OFS_end_month, OFS_end_day)
        OFS_received_date = random_date_generator(OFS_ordered_date.year, OFS_ordered_date.month, OFS_ordered_date.day, OFS_end_year, OFS_end_month, OFS_end_day).isoformat()
        OFS_ordered_date = OFS_ordered_date.isoformat()
        OFS_total_number_of_items = random.randint(1, OFS_n_products)
        OFS_supplier_id = random.randint(1, OFS_n_supplieres)
        
        OFS_attributes = [OFS_id, OFS_ordered_date, OFS_received_date, OFS_total_number_of_items, OFS_supplier_id]
        
        OFS_nested_list[i] = OFS_attributes
    
    return OFS_nested_list

def sales_table(n: int, sales_number_of_customers: int, sales_start_year: int, sales_start_month: int, sales_start_day: int, sales_end_year: int, sales_end_month: int, sales_end_day: int, maximum_items_in_sale: int = 100)->list:
    """Generates n new sales with random attributes.
    
    Parameters
    ----------
    n: int
        Number of new sales to create.
    sales_number_of_customers: int
        The total number of customers.
    sales_start_year: int
        The first year of sales.
    sales_start_month: int
        The first month of sales.
    sales_start_day: int
        The first day of sales.
    sales_end_year: int
        The last year of sales.
    sales_end_month: int
        The last month of sales.
    sales_end_day: int
        The last day of sales.
    maximum_items_in_sale: int
        The maximum amount of items allowed in one sale.
    
    Returns
    -------
    list
        A nested list of n orders from suppliers, each has 4 random attributes.
    """

    sales_nested_list = [NONE]*n # Empty list, with n empty spots for n random products.

    for i in range(0, n):
        sale_id = i + 1 # Automatically generating a sale ID
        sale_customer_id = random.randint(1, sales_number_of_customers) # Random customer id
        sale_date = random_date_generator(sales_start_year, sales_start_month, sales_start_day, sales_end_year, sales_end_month, sales_end_day).isoformat() # Random date
        sale_number_of_items = random.randint(1, maximum_items_in_sale) # Random number of items in a sale

        sale_attributes = [sale_id, sale_customer_id, sale_date, sale_number_of_items] # Inserting the sale attributes into a list
        
        sales_nested_list[i] = sale_attributes
    
    return sales_nested_list # Inserting the sale into the sales list

def OFS_products_table(OFS_nested_list: list, n_products: int) -> list:
    """Generates a list of random products for each order from supplier.
    
    Parameters
    ----------
    OFS_nested_list: list
        A nested list with n orders from suppliers.
    n_products: int
        The total number of unique products.
    """
    
    OFS_products_nested_list = [NONE] # An empty list. Because I don't know how many total products the OFS_table function will generate, I decided to create a list with one cell only and to add more cells later in this function. 

    for order_ in range(0, len(OFS_nested_list)):
        
        number_of_products_in_order = OFS_nested_list[order_][3] # Getting the number of products in a specific order.
        
        for i in range(0, number_of_products_in_order):
            OFS_order_id = OFS_nested_list[order_][0] # Retrieving the order_id
            OFS_product_id = random.randint(1, n_products) # Selecting a random product id
     
            OFS_products_attributes = [OFS_order_id, OFS_product_id] # Inserting the OFS_products attributes into a list
            
            OFS_products_nested_list.append(OFS_products_attributes)

    
    return OFS_products_nested_list

def sales_products_table(sales_nested_list: list, n_products: int) -> list:
    """Generates a list of random products for each order from supplier.
    
    Parameters
    ----------
    sales_nested_list: list
        A nested list with n sales.
    n_products: int
        The total number of unique products.
    
    Returns
    -------
    list
        Returns a nested list with data for the sales_products table.
    """

    sales_products_nested_list = [NONE] # An empty list. Because I don't know how many total products the OFS_table function will generate, I decided to create a list with one cell only and to add more cells later in this function.

    for sale_ in range(0, len(sales_nested_list)):

        number_of_products_in_sale = sales_nested_list[sale_][3] # Getting the number of products in a specific sale.

        for i in range(0, number_of_products_in_sale):
            sale_id = sales_nested_list[sale_][0] # Retrieving the sale_id
            sale_product_id = random.randint(1, n_products) # Selecting a random product id

            sales_products_attributes = [sale_id, sale_product_id] # Inserting the sales_products attributes into a list

            sales_products_nested_list.append(sales_products_attributes)         

    return sales_products_nested_list