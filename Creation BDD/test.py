from msilib.schema import tables
import sqlite3

try:
    connexion = sqlite3.connect("soccer.sqlite")
    c = connexion.cursor()
    print("connexion ok")
except:
    print("no db connexion")



