"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13iv33cv203bukolug-a.oregon-postgres.render.com",
        database="todo_wgeg",
        user="root",
        password="3cS8jaHjKJJb2TbxoAu2tByxEpHD9uOR")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
