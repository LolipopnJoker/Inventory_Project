# Inventory Project
## Authors
* [@LolipopnJoker](https://github.com/LolipopnJoker)
## Table of Contents
* [Business problem](https://github.com/LolipopnJoker/Inventory_Project/blob/main/README.md#business-problem)
* [Data source](https://github.com/LolipopnJoker/Inventory_Project/blob/main/README.md#data-source)
* [Methods](https://github.com/LolipopnJoker/Inventory_Project/blob/main/README.md#methods)
* [Tech stack](https://github.com/LolipopnJoker/Inventory_Project/blob/main/README.md#tech-stack)
* [Lessons learned and recommendation](https://github.com/LolipopnJoker/Inventory_Project/blob/main/README.md#lessons-learned-and-recommendation)
* [Limitation and what can be improved](https://github.com/LolipopnJoker/Inventory_Project/blob/main/README.md#limitation-and-what-can-be-improved)
* [Repository structure](https://github.com/LolipopnJoker/Inventory_Project/blob/main/README.md#repository-structure)
* [Run Locally](https://github.com/LolipopnJoker/Inventory_Project/blob/main/README.md#run-locally)
## Business problem
In order to determine which and how much stock to order, along with when to do it, companies often use inventory management systems. Such systems helps tracking measurements such as [ABC Analysis](https://www.netsuite.com/portal/resource/articles/inventory-management/inventory-management.shtml) or [Demand Forecasting](https://www.netsuite.com/portal/resource/articles/inventory-management/inventory-management.shtml), and therefor are essential for many business.
In this project, I created a generic inventory database, generated random data and built dashboard to depict various KPIs and measurements. I had two motives that led me to create these project:
* The importance of data-driven decisions in the inventory management world - Few years ago I worked as a website manager for a large retail company. Though the company was the largest companies in Israel, it seemed to me that most of inventory management was lacking an interactive dashboard. Such dashboard could have save my team and myself so much time and effort - and since then, I've wanted to build one myself, just for the sake of overcoming this old challenge.
* For learning purposes - During the past three years I've learned several tools including R, Python and MYSQL. This project is the first time I combined my knowledge and skills in several different tools. In my opninion, the ability to connect those tools is an important skill in businesses.
## Data source
* Random data – In this project I generated the data myself instead of using an external data source. There are two reasons I did it that way:
    * Lack of data sources – At the beginning of this project I did a little research on inventory related datasets. Unfortunately, I didn't find a dataset that matched my needs: while there were some free-to-use datasets, it seems that most of them were quite small (didn't have many variables nor observations). Because one of my goals in this project was to work with more complicated data, the lack of one is the main reasons I decided to write Python scripts that will automatically generate the data.
    * Scalability – By generating the data with Python scripts it's easier to add more observations. The difference between a database with 1000 products, 500 customers and 100 suppliers and a much smaller one is simply changing few parameters.
## Methods
## Tech stack
* [MS VISIO](https://www.microsoft.com/en-ww/microsoft-365/visio/flowchart-software) - I used MS VISIO in order to create an ERD diagram. I found ERD diagrams to be a great strating point when trying to build a new database schema, and therefor this is the first thing I did in this project.
* [MYSQL](https://www.mysql.com/) - After finishing the ERD diagram, I created a database schema named "WAREHOUSE" with all 11 tables I planned on the diagram.
* [Python](https://www.python.org/) - I used several Python scripts that generates random data and inserts it to the "WAREHOUSE" database.
* [Tableau](https://www.tableau.com/) - Tableau was used in order to make a dashbored that depicts several KPI's based on the data from the "WAREHOUSE" database.
## Lessons learned and recommendation
## Limitation and what can be improved
* Data storage – currently, the entire project is running only on the local machine. While this isn't a huge limitation, considering how strong and fast modern home computers are, I still want to try and implement the data storage on a cloud computing service (such as google cloud or AWS). In the last couple of years, the popularity of such services increased drastically, and therefor I believe that it would make this project more realistic.
## Repository structure
```bash
│   README.md
│
├───MySql
│       creating_database.sql
│       creating_inventory_table.sql
│       inventory_database_scheme_1.vsdx
│       inventory_database_scheme_v_1.pdf
│
├───Python
│   │   RDG.py
│   │   RDG_examples.py
│   │   RDG_lists.csv
│   │   RDG_lists_csv_to_lists.py
│   │   RDT.py
│   │   RDT_examples.py
│   │   connecting_dots.py
│   │   recreating_DB.py
│   │
│   └───__pycache__
│           RDG.cpython-36.pyc
│           RDG.cpython-39.pyc
│           RDG_lists_csv_to_lists.cpython-39.pyc
│           RDT.cpython-36.pyc
│           RDT.cpython-39.pyc
│
└───Tableau
        inventory_dashboard.twb
```
## Run Locally  
