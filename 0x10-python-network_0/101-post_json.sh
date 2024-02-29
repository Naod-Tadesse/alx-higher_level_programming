#!/bin/bash
# this script sends json for post
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
