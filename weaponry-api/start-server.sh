#!/bin/bash

# Mongo DB instance
mongod --fork --logpath /var/log/mongod.log

# Start Server
npm start