#!/bin/bash
# Takes an URL and display all HTTP methonds the server will accept
curl -is -X OPTIONS "$1" | grep Allow: | sed 's/Allow: //'
