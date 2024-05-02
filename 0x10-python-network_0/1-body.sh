#!/bin/bash
# Send a GET rquest to an URL and displays body response only when status = 200
status=$(curl -s -i "$1" | grep -o "200 OK" | awk '{print $2}')
if [ "$status" = "OK" ]; then
    curl -s "$1"
fi    
