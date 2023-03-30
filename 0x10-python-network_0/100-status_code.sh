#!/usr/bin/env bash
# Script sends request to URL passed as arg. and displays only the status
#code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
