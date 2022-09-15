import mariadb
import sys
import os
from django.http import HttpResponse

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    conn = mariadb.connect(
        user="root",
        password="1234",
        host="127.0.0.1",
        port=3306,
        database="Testbase"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

cur.execute(
    "SELECT * FROM user", 
    )

datas = ""

for (ID, First_name, Last_name, Birth) in cur:
    datas += (f"ID: {ID}, First Name: {First_name}, Last Name: {Last_name}, Birth: {Birth} ")

def index(request):
        return HttpResponse(datas)
