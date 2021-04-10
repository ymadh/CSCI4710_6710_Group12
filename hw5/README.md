## Quick Start

### Local Test Setup

First, we need to install a Python 3 virtual environment with:

```
sudo apt update
sudo apt-get install python3-venv
```

Create a virtual environment within this directory:

```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:

```
source python_venv/bin/activate
```

To fufill all the requirements for the python server, you need to run:

```
pip3 install -r requirements.txt
```

Because we are now inside a virtual environment, we do not need sudo.

Open TableCreateAndImportScript.sql and modify line 52 to point to your data directory.

Run the following to create all the SQL tables required to run this script.
If you need to delete existing tables (for example, to restart this assignment), please uncomment the DROP TABLE commands in TableCreateAndImportScript.sql.
(An alternate way to run this function is to open a new terminal window in this directory, enter "postgres" and then run the below command)

```
psql -f TableCreateAndImportScript.sql
```
The configuration may need to be changed in main.py on lines 11 & 12:

connection = psycopg2.connect(user="devUser",
password="",

Then you can start the server with:

```
python3 main.py
```
