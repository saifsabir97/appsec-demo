**What is SQL Injection?**

It is a vulnerability that allows an attacker to interfer with the sql queries that the application code runs on the database.

https://portswigger.net/web-security/sql-injection

**Setup**

API Framework: Flask

We use flask to expose a login endpoint.

Database: SQLite

A user table in sqlite database contains the username and password of registered users. To make things simple, the passwords are stored as plaintext.

To set up the environment, first run init_db.py to setup the database along with dummy data. Then run app.py to start up the API server.

**Normal Working**

When a valid username and password combination is entered, the login attempt becomes successful and a welcome page is displayed. When an invalid combination is entered, an error message is displayed on the same page.

**Attack**

Behind the scenes, the application is making an SQL query to the user table in the database to check if the combination is valid.

As seen in the code, there are no checks done on the input coming to the server. If the input itself is given as an SQL query in such a way that the resultant query becomes valid, the attacker can run the modified SQL queries on the database.

In this example, if we give the last name as xxx, then the resultant query that actually runs in the database is yyy, thus running the query zzz as intented by the attacker. As a result, login step is bypassed.

**Preventive Measures**

There are several ways to mitigate these types of attacks. We will look into parameterised queries approach where the database engine itself makes sure that there are no hidden sql queries present inside any query parameter. To fix our app, we can modify the query to use parameters in place of username and password and then pass the user input for these two fields as parameters. Now if we attemt to run the malicious input again, the api returns error.
