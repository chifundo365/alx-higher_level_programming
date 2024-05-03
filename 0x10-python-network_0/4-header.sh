#!/bin/bash
# Sends a head request to a given URL and a sends a header variable, returns body
curl -s -H "X-School-User-Id: 98" "$1"
