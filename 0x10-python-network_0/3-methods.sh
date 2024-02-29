#!/bin/bash
# this scritp returns method
curl -sIX OPTIONS "$1" | grep -i allow | cut -d ":" -f 2-
