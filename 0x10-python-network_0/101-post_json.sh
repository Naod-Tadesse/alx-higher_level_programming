#!/bin/bash
# this script sends json for post
curl -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
