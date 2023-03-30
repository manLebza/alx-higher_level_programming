#!/usr/bin/env bash
#Script displays the number of bytes in location
curl -s "$1" | wc -c
