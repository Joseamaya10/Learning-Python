import urllib.request, urllib.parse, urllib.error
import json

# Add your API key here
API_KEY = 'YOUR_API_KEY_HERE'
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    params = {
        'address': address,
        'key': API_KEY
    }
    url = serviceurl + urllib.parse.urlencode(params)

    try:
        print('Retrieving', url)
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        js = json.loads(data)

        if js['status'] != 'OK':
            print('=== Error:', js['status'], '===')
            if 'error_message' in js:
                print(js['error_message'])
            continue

        lat = js['results'][0]['geometry']['location']['lat']
        lng = js['results'][0]['geometry']['location']['lng']
        print('lat', lat, 'lng', lng)
        location = js['results'][0]['formatted_address']
        print(location)

    except urllib.error.URLError as e:
        print('=== Failed to reach server ===')
        print(e.reason)
    except json.JSONDecodeError:
        print('=== Failed to parse response ===')
    except Exception as e:
        print('=== An error occurred ===')
        print(str(e))