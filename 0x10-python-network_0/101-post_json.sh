#!/usr/bin/env bash
# Script sends a JSON request to a URL passed in as an arg,and displays body
#of the response
curl -sH "Content-Type: application/json" -d @"$2" -X POST "$1"
