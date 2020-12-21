# Simple Demo for Flask web development study

* Development Environment
  * Operating System `Ubuntu18.04`
  * Package
    * Python `3.6.7`
    * Flask  `1.1.2`
    * flask-sqlalchemy `2.4.4`
    * pymysql `0.10.1`
    * jinja2 `2.11.2`
    * werkzeug `1.0.1`

* Flask
  * What is Flask
    Flask is a simple python web development framework like Django it utilies many similar features such as Jinjia2 syntax to create `HTML` web page
  * Flask basic structure
    ```
    from flask import Flask, render_template, url_for, request, redirect
    ``` 
    * Flask  `flask object`
    * render_template  `intepreter the web page`
    * url_for  `explains where the files are`
    * redirect  `change the web page url`
    ```
    from flask_sqlalchemy import SQLAlchemy
    ```                           
    * SQLAlchemy is a library that facilitates the communication between Python programs and databases. Most of the times, this library is used as an Object Relational Mapper (ORM) tool that translates Python classes to tables on relational databases and automatically converts function calls to SQL statements.
  
* 
  