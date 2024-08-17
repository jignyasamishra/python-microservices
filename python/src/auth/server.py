import jwt, datetime , os
from flask import Flask, request
from flask_mysqldb import flask_mysqldb

server = Flask(__name__)
mysql = MySQL(server)