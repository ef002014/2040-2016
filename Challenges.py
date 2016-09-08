import json
import requests


# STEP 1: INTRODUCTION
passIn =  {'token':'9cc00e459ebfd732c67ed213ddc614d1',
             'github':'https://github.com/ef002014/2040-2016'}

url = "http://challenge.code2040.org/api/register"

r = requests.post( url, data=passIn)

print r.text


#STEP 2: REVERSE A STRING
getString =  {'token':'9cc00e459ebfd732c67ed213ddc614d1'}

url = "http://challenge.code2040.org/api/reverse"

r = requests.post( url, data=getString)

newStr = r.content

print newStr

swapStr = ""

for index in reversed(range((len(newStr)))):
    swapStr = swapStr + newStr[index]

print swapStr


revString =  {'token':'9cc00e459ebfd732c67ed213ddc614d1',
               'string':swapStr}

url2 = "http://challenge.code2040.org/api/reverse/validate"

r = requests.post( url2, data=revString )
