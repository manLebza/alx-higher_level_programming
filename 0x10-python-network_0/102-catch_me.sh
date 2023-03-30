#!/usr/bin/env bash
# Script sends request to 0.0.0.0:5000/catch_me,then server sends response
#with message containing 'YOU GOT ME!' in the body.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98"
0.0.0.0:5000/catch_me
