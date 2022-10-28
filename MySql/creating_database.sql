/*
Object: Creating a new warehouse db procedure 
Author: Yoav Weller
Script Date: August 09, 2022
Description: This procedure establishes a new
database called "WAREHOUSE". Should be used only
if the server dosen't have a database with this
name.
*/

DROP DATABASE IF EXISTS WAREHOUSE;
CREATE DATABASE WAREHOUSE;
USE WAREHOUSE;