/*
Object: Creating tabels to use in the WARHOUSE database. 
Author: Yoav Weller
Script Date: August 30, 2022
Description: This procedure establishes a new
database called "WAREHOUSE". Should be used only
if the server dosen't have a database with this
name.
*/

CREATE TABLE product_categories(
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50)
);

CREATE TABLE product_subcategories(
    subcategory_id INT PRIMARY KEY,
    subcategory_name VARCHAR(50),
    subcategory_category_id INT,
    FOREIGN KEY (subcategory_category_id) REFERENCES product_categories(category_id)
);

CREATE TABLE Suppliers(
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(100),
    supplier_adress VARCHAR(100)
);

CREATE TABLE products(
    product_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    product_full_price FLOAT(100, 2) NOT NULL,
    product_category_id INT NOT NULL,
    product_subcategory_id INT,
    product_supplier_id INT,
    product_creation_in_system TIMESTAMP DEFAULT now(),
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_category_id) REFERENCES Product_Categories(category_id),
    FOREIGN KEY (product_subcategory_id) REFERENCES Product_Subcategories(subcategory_id),
    FOREIGN KEY (product_supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Products_DIM(
    product_DIM_id INT NOT NULL,
    product_H_CM FLOAT NOT NULL,
    pruduct_Wid_CM FLOAT NOT NULL,
    pruduct_D_CM FLOAT NOT NULL,
    product_H_INC FLOAT NOT NULL,
    pruduct_Wid_INC FLOAT NOT NULL,
    pruduct_D_INC FLOAT NOT NULL,
    product_weight_KG FLOAT NOT NULL,
    product_weight_LBS FLOAT NOT NULL,
    PRIMARY KEY (product_DIM_id),
    FOREIGN KEY (product_DIM_id) REFERENCES Products(product_id)
);

CREATE TABLE Inventory(
    inventory_product_id INT NOT NULL,
    product_aisle VARCHAR(10),
    product_shelf INT,
    product_current_stock INT,
    PRIMARY KEY (inventory_product_id),
    FOREIGN KEY (inventory_product_id) REFERENCES Products(product_id)
);

CREATE TABLE Orders_From_Sup(
    OFS_id INT NOT NULL,
    OFS_oredered_date DATETIME,
    OFS_oreder_received_date DATETIME,
    OFS_total_number_of_items INT,
    OFS_supplier_id INT,
    PRIMARY KEY (OFS_id),
    FOREIGN KEY (OFS_supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Orders_From_Sup_Items(
    OFS_item_order_id INT NOT NULL,
    OFS_item_id INT NOT NULL,
    FOREIGN KEY (OFS_item_order_id) REFERENCES Orders_From_Sup(OFS_id),
    FOREIGN KEY (OFS_item_id) REFERENCES products(product_id)
);

CREATE TABLE Customers(
    customer_id INT NOT NULL,
    customer_first_name VARCHAR(30),
    customer_last_name VARCHAR(30),
    customer_company VARCHAR(30),
    customer_address VARCHAR(30),
    customer_city VARCHAR(30),
    customer_state VARCHAR(30),
    customer_phone VARCHAR(30),
    customer_gender CHAR(1),
    customer_birthdate DATE,
    customer_joined_on DATETIME,
    PRIMARY KEY (customer_id)
);

CREATE TABLE Sales(
    sale_id INT NOT NULL,
    sales_customer_id INT,
    sales_time DATETIME DEFAULT now(),
    PRIMARY KEY(sale_id)
);

CREATE TABLE Sales_Products(
    Sales_Products_sale_id INT NOT NULL,
    Sales_Products_product_id INT NOT NULL,
    FOREIGN KEY (Sales_Products_sale_id) REFERENCES Sales(sale_id),
    FOREIGN KEY (Sales_Products_product_id) REFERENCES Products(product_id)
);