#!/usr/bin/env python
#
# Downloads a month's worth of weather data (currently March 2012) from weather underground.
# Requires their API key. This should be placed in a file called "local_settings.py" which
# needs to be in the python path BUT NOT THE REPOSITORY! The key should be a string with the
# variable name WUNDERGROUND_KEY.
#
# After 9 downloads, the script will sleep for 60 seconds. The reason for this is the 10 downloads per minute limit on the free API access.

def get_url(month,day,year,state,city):
    from local_settings import WUNDERGROUND_KEY
    fmt = "http://api.wunderground.com/api/%s/history_%%4d%%02d%%02d/q/%s/%s.json" % (WUNDERGROUND_KEY, state, city)
    
    return fmt % (year,month,day)

def get_wx_data(url):
    import urllib2
    import json
    f = urllib2.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    return (parsed_json,json_string)

if __name__ == "__main__":
    from time import sleep
    from local_settings import STATE,CITY
    for i in xrange(31):
        if i and i % 9 == 0:
            print("Sleeping after 9 downloads")
            sleep(60)
        (month,day,year) = (03,i+1,2012)
        url = get_url(month,day,year,STATE,CITY)
        print(url)
        (data, json_string) = get_wx_data(url)
        with open("wx_%d%02d%02d.json" % (year,month,day),"w") as output:
            output.write(json_string)
    
