# Y2 2018 Yearlong: Databases

### Before you start: Fork and clone this repository

1. Fork this repository by clicking "Fork" on this page:
![forking](https://image.ibb.co/jHRieT/forking.png)

2. Copy this repository's url by clicking the green clone button:
![copying url](https://image.ibb.co/n2wYeT/copying_clone.png)


## Part 1: Defining The Products Table

1. Open model.py and create the products class (Table). Make sure to include at least 5 attributes of your choice (i.e. price, quantity, description).

2. Open the terminal, navigate to your folder from the terminal (cd y2l...) then run **databases.py**.
If you open the folder you can notice that there's a new file called **lecture.db** in which all the data is stored (Your database).
Go to the terminal again and run **python print_database.py lecture.db**. this command prints your database where you should see the table that you've recently created.

3. Show your work to an instructor or a TA.


## Part 2: Insert Data to Database

1. Create a function in **databases.py** that adds a product to the database.

2. Call this function to add your first object to the database.

3. Run **databases.py** then print the database using this command line **python print_database.py lecture.db** to check if you successfully added the object.



## Part 3: Retrieve Data from Database

1. Create a function in **databases.py** that gets the first product from the **Prodcuts** table in your database **and returns it**.

2. Call this function and **print** the product.

3. Run **databases.py** and check whether it printed the object or not.


## Part 4: Update Data in Database

1. Create a function in **databases.py** that updates 2 attributes of a product from the database.

2. Call this function.

3. Run **databases.py** then print the database using this command line **python print_database.py lecture.db** to check if you successfully updated the product.



## Part 5: Delete Data from Database

1. Create a function in **databases.py** that deletes one product of your choice.

2. Call this function.

3. Run **databases.py** then print the database using this command line **python print_database.py lecture.db** to check if you successfully deleted the product.
