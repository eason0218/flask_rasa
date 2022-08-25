import requests
import json


class Weather():
    @staticmethod
    def get_data(locationName):
        url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-130552BE-F0AC-4DA2-B215-100EEDEABF0F&format=JSON&locationName={locationName}"
        response = requests.get(url)
        weatherJson = json.loads(response.text)
        weatherDate = []

        for i in range(5):
            weatherDate.append(
                weatherJson["records"]["location"][0]["weatherElement"][i]["time"][0]["parameter"]['parameterName']
            )

        return weatherDate
