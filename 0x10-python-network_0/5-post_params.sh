#!/bin/bash
# this script handles post request with body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
