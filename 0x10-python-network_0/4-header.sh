#!/bin/bash
# Bash script that takes in a URL as an argument
curl -sb -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
