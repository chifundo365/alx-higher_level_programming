#!/bin/bash
# Send a GET rquest to an URL and displays body response only when status = 200
curl -s -i "$1" | grep -i "HTTP/1.1 200 OK" && clear && curl "$1"
