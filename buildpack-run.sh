#!/bin/bash
string_to_find="Get a Quote, Get Covered, Today"
if curl -s "https://insurancemaster.herokuap.com/" | grep -q "$string_to_find"; then
    echo "Insurance Master is up and running"
    exit 0
else
    echo "Insurance Master is not up and running. Investigate Now!"
    exit 1
fi