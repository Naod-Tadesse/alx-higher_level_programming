#!/bin/bash
# display the result of delete request
curl -sX  DELETE "$1" | cat
