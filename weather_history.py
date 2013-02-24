def get_url(month,day,year):
    from import_settings import WUNDRGROUND_KEY
    fmt = "http://api.wunderground.com/api/%s/history_%4d%02d%02d/q/TN/Memphis.json" % WUNDERGROUND_KEY
    
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
    for i in xrange(31):
        if i and i % 9 == 0:
            print("Sleeping after 9 downloads")
            sleep(60)
        (month,day,year) = (03,i+1,2012)
        url = get_url(month,day,year)
        print(url)
        (data, json_string) = get_wx_data(url)
        with open("wx_%d%02d%02d.json" % (year,month,day),"w") as output:
            output.write(json_string)
    
