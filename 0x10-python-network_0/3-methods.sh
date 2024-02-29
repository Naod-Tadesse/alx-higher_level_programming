#!/bin/bash
# this script returns method
curl -sI "$1" | grep -i "Allow" | cut -d " " -f 2-
