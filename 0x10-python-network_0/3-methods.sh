#!/bin/bash
# this scritp returns method
curl -sIX OPTIONS "$1" | grep -I allow | cut -d ":" -f 2-
