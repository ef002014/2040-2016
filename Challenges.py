import json
import requests
import time
import iso8601
from datetime import timedelta
from datetime import date


# STEP 1: INTRODUCTION
# Connect to the registration endpoint
passIn =  {'token':'9cc00e459ebfd732c67ed213ddc614d1',
             'github':'https://github.com/ef002014/2040-2016'}

url = "http://challenge.code2040.org/api/register"

r = requests.post( url, data=passIn)

print r.text



#STEP 2: REVERSE A STRING
# Reverse the given string
getString =  {'token':'9cc00e459ebfd732c67ed213ddc614d1'}

url = "http://challenge.code2040.org/api/reverse"

r = requests.post( url, data=getString)

newStr = r.content

print newStr

swapStr = ""

#loop through string from back to front and 
#add each individual character to the empty string
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

# loop through each string in the hastack and compare
# the string with the needle
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



#STEP 4: Prefix
getDictionary=  {'token':'9cc00e459ebfd732c67ed213ddc614d1'}

url = "http://challenge.code2040.org/api/prefix"

r = requests.post( url, data=getDictionary)

theDic = r.content

s = json.loads(theDic)

prefix = s['prefix']

ogArray = s['array']

print 'the prefix is: %s' % (prefix)
print 'the array is: %s' % (ogArray)

newArray = list()

# loop through each string in the hastack and compare
# prefix with string
# if prefix is not at the beginning of the string
# add it to the new string
for index in range(len(ogArray)):
    tempLen = len(ogArray[index])
    tempStr = ogArray[index]

    if not tempStr.startswith(prefix, 0, tempLen):
        newArray.append(tempStr)

print 'the new array is: %s' % (newArray)


arrayInfo =  {'token':'9cc00e459ebfd732c67ed213ddc614d1',
               'array': newArray}

url2 = "http://challenge.code2040.org/api/prefix/validate"

r = requests.post( url2, data=arrayInfo)



#STEP 5: The Dating Game
getStamp=  {'token':'9cc00e459ebfd732c67ed213ddc614d1'}

url = "http://challenge.code2040.org/api/dating"

r = requests.post( url, data=getStamp)

theStamp = r.content

theDic = json.loads(theStamp)

print theDic

#the date stamp
theDate = theDic["datestamp"]


#the int that represents seconds
theIntvl = theDic["interval"]

print theDate

print theIntvl

#intermediate date (not quite the datestamp yet)
rightDate = iso8601.parse_date(theDate) + timedelta(seconds=theIntvl)

print rightDate

#the final appended date stamp
finalDate = rightDate.isoformat()

print finalDate

dateInfo =  {'token':'9cc00e459ebfd732c67ed213ddc614d1',
               'datestamp': finalDate }

url2 = "http://challenge.code2040.org/api/dating/validate"

r = requests.post( url2, data=dateInfo)

print r.text

