# MongoDB default configuration
```
Description: Need change default username:password

# Install MongoDB
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org

# Connect to a remote server with credentials
mongo --username 'uname' -p 'pword' --host hostname.com:27017

# Print database info
show databases
use <databasename>
show collections
c = db.<collectioname>
c.find()
```

## Back to README.md
[BACK](/README.md)