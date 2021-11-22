#!/bin/bash
string="Get a Quote, Get Covered, Today"
if curl -s "https://insurancemaster.herokuapp.com/" | grep -q "$string"; then
    echo "Insurance Master is up and running"
    exit 0
else
    echo "Insurance Master is not up and running. Investigate Now!"
    exit 1
fi