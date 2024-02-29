#!/bin/bash
# this scritp returns method
curl -sI "$1" | grep -I "Allow" | cut -d " " -f 2-
