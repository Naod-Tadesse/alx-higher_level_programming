#!/bin/bash
# this displays the size of response

curl -s "$1" | wc -c
