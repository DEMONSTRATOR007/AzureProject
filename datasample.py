import pyodbc
import textwrap



# specify the driver
driver = '{ODBC Driver 17 for SQL Server}'


#specify the server name and database name
server_name =
database_name = 


# create our server url.
server = 


#define username and password.

username =
password=

#create the full connection string.
connection_string = textwrap.dedent('''
    Driver ={driver};
    server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
 '''.format(
     driver=driver,
     server=Server,
     database=database_name,
     username=username,
     password=password
 ))

 # create a new PYOBDC Connection Object.
cnxn: pyodbc.connection = pyodbc.connect(connection_string)

# create a new cursor object from the connection
crsr: pyodbc.Cursor = cnxn.cursor()

#close the connection when we are done
cnxn.close()



