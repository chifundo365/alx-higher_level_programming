#!/bin/bash
# Sends a request to a URL and displays the size of the body response
curl -s -I "$1" | grep -i Content-Length | awk '{print $2}'
