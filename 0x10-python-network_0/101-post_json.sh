#!/bin/bash
# this script sends json for post

curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
