## Quick Start

### Local Test Setup

First, we need to install a Python 3 virtual environment with:

```
sudo apt update
sudo apt-get install python3-venv
```

Create a virtual environment:

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

Because we are now inside a virtual environment. We do not need sudo.

Open TableCreateAndImportScript.sql and modify line 47 to point to your data directory

Run the following to create all the SQL tables required to run this script

The configuration may need to be changed in main.py on lines 11 & 12:
connection = psycopg2.connect(user="postgres",
password="",

```
psql -f TableCreateAndImportScript.sql
```

Then you can start the server with:

```
python3 main.py
```
