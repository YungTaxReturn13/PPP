import pandas as pd
import requests
import json
import os

# We get a free $200 credit every month. I created this code on 12/16/2020.
#  $5 for 1000 requests. So we can make 40,000 requests per month
# That is not enough to get the geolocations for every data point but enough to work with for now
# Track using the JSON Accordingly and reset after a month has passed
def get_coordinates(zip_code, df ):
    if str(zip_code)+'.csv' in os.listdir(r'C:\Users\justi\Python Projects\PPP Analysis\PPP-Analysis\Coordinates'):
        return print('This zip code already had its data generated')
    else:
        # This section brings in the API Key
        with open(r'C:\Users\justi\Python Projects\PPP Analysis\PPP-Analysis\Confidential\API KEY.json') as g:
            key = json.load(g)
        api = key["key"]
        with open(r'C:\Users\justi\Python Projects\PPP Analysis\PPP-Analysis\usage.json') as f:
          data = json.load(f)

        if data['usage'] + len(df) > 39_000:
            print('WE WILL BE GOING OVER YOUR LIMIT! RUN STOPPED')
        else:
            data['usage'] = data['usage'] + len(df)
            with open(r'C:\Users\justi\Python Projects\PPP Analysis\PPP-Analysis\usage.json', 'w') as f:
                json.dump(data, f, indent=4)

            cols = ['Full_Address','Lat', 'Lng']
            lst = []


            for i in df['Full_Address']:
                try:
                    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={i}&key={api}')
                    resp_json_payload = response.json()

                    print(resp_json_payload)

                    print(resp_json_payload['results'][0]['geometry']['location'])
                    geo = (resp_json_payload['results'][0]['geometry']['location'])
                except:
                    geo = {'lat':'N/A', 'lng':'N/A'}

                lst.append([i,geo.get('lat'), geo.get('lng')])

            coordinates = pd.DataFrame(lst,columns=cols)

            coordinates.to_csv(f'PPP-Analysis\\Coordinates\\{str(zip_code)}.csv',index=False)



if __name__ == '__main__':
    get_coordinates()