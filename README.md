# Inventory Project

## Project Description

In order to determine  which and how much stock to order, along with when to do it, companies often use inventory management systems. Such systems helps tracking measurements such as [ABC Analysis](https://www.netsuite.com/portal/resource/articles/inventory-management/inventory-management.shtml) or [Demand Forecasting](https://www.netsuite.com/portal/resource/articles/inventory-management/inventory-management.shtml), and therefor are essential for many business.
In this project, I created a generic inventory database, generated random data and built dashboard to depict various KPIs and measurements. I had two motives that led me to create these project:
1. **The importance of data-driven decisions in the inventory management world** - Few years ago I worked as a website manager for a large retail company. Though the company was the largest companies in Israel, it seemed to me that most of inventory management was lacking an interactive dashboard. Such dashboard could have save my team and myself so much time and effort - and since then, I've wanted to build one myself, just for the sake of overcoming this old challenge.
2. **For learning purposes** - During the past three years I've learned several tools including R, Python and MYSQL. This project is the first time I combined my knowledge and skills in several different tools. In my opninion, the ability to connect those tools is an important skill in businesses.

### Tools and HOW They Were Implemented

Beside this file, there are three folders in this project.

1. [**MS VISIO**](https://www.microsoft.com/en-ww/microsoft-365/visio/flowchart-software) - I used MS VISIO in order to create an ERD diagram. I found ERD diagrams to be a great strating point when trying to build a new database schema, and therefor this is the first thing I did in this project.
2. [**MYSQL**](https://www.mysql.com/) - After finishing the ERD diagram, I created a database schema named "WAREHOUSE" with all 11 tables I planned on the diagram.
3. [**Python**](https://www.python.org/) - I used several Python scripts that generates random data and inserts it to the "WAREHOUSE" database.
4. [**Tableau**](https://www.tableau.com/) - Tableau was used in order to make a dashbored that depicts several KPI's based on the data from the "WAREHOUSE" database.

### Challenges

1. **Planning**
2. **Debugging**

## Project Content
This folder contains three subfolders:
1. [**MySql**](https://github.com/LolipopnJoker/Portfolio/tree/main/Inventory%20Project/MySql) - contains two sql scripts (one for creating the database schema and one for creating the tables); as well as a PDF file of an ERD diagram depicting the structure of the database schema.
2. [**Python**](https://github.com/LolipopnJoker/Portfolio/tree/main/Inventory%20Project/Python) - currently contains 7 Python scripts and one csv file. I plan to add to this folder an indepth explanations for each file.
3. [**Tableau**](https://github.com/LolipopnJoker/Portfolio/tree/main/Inventory%20Project/Tableau) - in this is the Tableau file.

## How To Create The Database on Your Own Computer?
In order to create an instance of the database schema and tables on your computer, please follow the following steps:
1. Download both the 'MySql' and 'Python' subfolders and store them wherever you want (just remember where you saved it).
2. Open the 'Python' subfolder.
3. Search for a 'Python' script named 'recreating_DB.py' and open it in your code-editor of choice.
4. Change the password of your root user to match your password (line 12).
5. Change the path  
