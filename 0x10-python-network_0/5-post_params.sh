#!/usr/bin/env bash
# Script sends a post request to the passed URL,then displays the body of req
curl -s -X POST -d "email=test@gmail.com&subject=I will always
be here for PLD" "$1"
