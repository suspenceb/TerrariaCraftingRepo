# Introduction
This document provides information about the files within this template, and guidance on working with the database. If you need help working with the database, or if you want to better understand the structure of the template project, I recommend you give this document a read.


## How to Establish Database Connections
When you want to query the database, you need to start with the code `conn = get_db_connection()`. I wrote the function `get_db_connection` for you. It pulls in the variables you set in the `.env` file and establishes a conenction with your mysql database. If there are any issues with this code you probably have one of two errors. a) You have incorrectly defined some information within your `.env` file or b) You need to run this command in your terminal: `pip install python-dotenv`. When you have finished querying the database, it is IMPORTANT that you run `conn.close()`. This command ends the database connection. If you do not do this, you will most likely run into errors about the database being locked.


## How to Query the Database
1. Establish a connection `conn = get_db_connection()`
2. Create a cursor `cursor = conn.cursor()`
3. Write a query `query = "INSERT INTO items (name, quantity) VALUES (%s, %s)"`
4. Prepare values for your query (as needed) `values = ("screws", 15,)`
5. Execute the query `cursor.execute(query, values)` OR `cursor.execute(query)`
6. Commit values (when necessary) `conn.commit()`
7. Fetch results (when necessary) `result = cursor.fetchall()` OR `result = cursor.fetchone()`
8. Close the connection `conn.close()`

### Information About Each Step
1. Every time you want to query the database, you first must establish a connection.
2. Once you have the connection, you need to create a cursor. The cursor is used to execute the query, and fetch results.
3. When you need to insert user supplied values, you should ALWAYS use a prepared statement. In the example, the prepared values are `%s, %s`. These values will be replaced with the variables from the values tuple (as shown in 4.) when you execute the query (as shown in 5.). 
4. Values should always be a tuple, and you should have a comma after your last value in the tuple. This is shown in the example.
5. When your query requires user supplied values, you will need to store these values in a tuple (as shown in 4.). Then, execute the statement with the query string first, followed by the values `(query, values)`. If you don't need to supply any values to your query, then you only need to do `cursor.execute(query)`.
6. You only need to commit changes when you change the database. If you are performing a SELECT statement, you don't need to do this. However, if you are doing an INSERT, UPDATE, or DELETE, then you will need to commit changes.
7. If you desire to retrieve information from a query, you will need to fetch the results. For example, if you performed a SELECT, you would need to use fetch to retrieve the results. On the other hand, if you had performed a DELETE, you wonuldn't need to use a fetch.
8. Once you have completed your query, you should ALWAYS close the connection. Failure to do so may result in errors about the database being locked.


## main.py
This file is just a template. You can and should change the routes, and create new routes. This template should give you a good idea of how to do this. To create a route, you need to write 2 lines of code:
```python
    @app.route("/route-name", methods=["ROUTE-METHOD"])
    def route_name()
```
Replace `route-name` with the name for your route. Replace `ROUTE-METHOD` with the method, e.g. `GET`, `PUT`, `POST`, `DELETE`. Replace route_name with the name you want this route to be defined as in the python code. This is the same name you will put for `route_name` in the code `url_for(route_name)` to redirect users to the specified route.

Final note, when you deploy to production, PLEASE remove `debug=True` from the code `app.run(port=8080, debug=True)` at the bottom of the file. This is a security vulnerability, and I WILL call you out for it.


## templates folder
This folder contains all the html pages that you desire to render. If you look in `main.py`, you will notice that my `home` route has the code: `return render_template("index.html", items=items)`. The function `render_template` knows what `index.html` is because `index.html` is a file within the `templates` folder. When you create new html pages, you should to create them within the `templates` folder, otherwise you will become very confused.


## static folder
This folder should contain all static elements for your website. Examples are css files, javascript files, and possible libraries.


## .env file
The first thing you should do after downloading this project is rename `.env.example` to `.env`. Next, you should change the values within the `.env` file. `DB_HOST` is the IP address where the MYSQL database is being hosted. If you are hosting the database on the same machine that is hosting the website, the IP address will be `127.0.0.1`. `DB_USER` is the name of the user who owns or who has permissions to access and edit the database. By default, this user is `root`. If you create a limited privleges user, then you can replace this value with the name of your username. `DB_PASSWORD` is the password for the `DB_USER` account. Please make a decently secure password. If your password is actually `password`, I may hack your database. `DB_DATABASE` is the name of the database you created. In my example `db_inits_scripts.txt`, I created the database `itemdb`, and thus I set the value for `DB_DATABASE` to `itemdb`. If you are creating a Pokemon database, you may choose to create a database named `pokemon`. Accordingly, you would set `DB_DATABASE` to `pokemon`. NOTE: don't mix up database and table. The database is the name of the whole database, and a table is the name of a table within the database. Finally, we have `SECRET`. This value is used for some of the Python Flask code that you don't really need to worry about. Just change `SECRET` to some random value, even if you just mash your hands on the keyboard it would be fine. In a real production environment, you would need to do something more secure.


## db_inits_script.txt
This file contains the SQL commands I ran to create my database and to create the table used in this sample website. If you want to test basic functionality before creating your own database and writing your own code, then I would encourage you to run these scripts in MYSQL Workbench to create the database and table. You are NOT required to use my script. You should eventually delete these scripts in this file and replace them with your own.
