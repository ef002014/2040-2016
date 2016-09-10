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



#STEP 3: Needle in a Haystack
getDictionary=  {'token':'9cc00e459ebfd732c67ed213ddc614d1'}

url = "http://challenge.code2040.org/api/haystack"

r = requests.post( url, data=getDictionary)

theDic = r.content

s = json.loads(theDic)

needle = s['needle']

haystack = s['haystack']

needleSpot = -1

for index in range(len(haystack)):
    if needle == haystack[index]:
        needleSpot = index

print 'the needle is: %s' % (needle)
print 'the haystack is: %s' % (haystack)
print 'We found the needle in spot %d of the haystack' % (needleSpot)

needleInfo =  {'token':'9cc00e459ebfd732c67ed213ddc614d1',
               'needle':needleSpot}

url2 = "http://challenge.code2040.org/api/haystack/validate"

r = requests.post( url2, data=needleInfo)
