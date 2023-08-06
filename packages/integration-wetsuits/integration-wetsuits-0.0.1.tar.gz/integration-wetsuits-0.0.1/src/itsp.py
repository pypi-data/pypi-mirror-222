import requests
import clappform
import clappform.dataclasses as cldc
import pandas as pd
import json

class Itsperfect:
    id=None

    def __init__(self, url, token, version = "v2"):
        self.url = url
        self.token = token
        self.version = version

    def setFullUrl(self, category, id = "", subject = "", filter = ""):
        if id != "":
            id = f"/{id}"

        if subject != "":
            subject = f"/{subject}"

        if filter != "":
            filter = f"&filter={filter}"

        url = f"https://{self.url}/api/{self.version}/{category}{id}{subject}/&token={self.token}{filter}"
        return url
    
    def getAllPicks(self):
        fullUrl = self.setFullUrl("picks")
        r = requests.get(fullUrl)
        return r.json()
    
    def getOnePick(self, id : int ): 
        fullUrl = f"https://{self.url}/api/v2/picks/{id}/&token={self.token}"
        r = requests.get(fullUrl)
        return r.json()

    def storePicks(self, clp):
        defaultApp = clp.get(cldc.App(id="import_database", extended=True))
        flightCollection = clp.get(cldc.Collection(
            app=defaultApp,
            slug="picks"
        ))

        try:
            df = pd.DataFrame(self.getOnePick(1321)['picks'])
            clp.empty_dataframe(flightCollection)
            clp.write_dataframe(df, flightCollection, size=100)
            print("yes")
        except clappform.exceptions.HTTPError as exc:
            print(exc.response.text)

    def readPicks(self, clp):
        pipeline = {
            "app": "import_database",
            "collection": "picks",
            "pipeline": [],
            "limit": 500
        }

        try:
            aggregateResults = pd.DataFrame([])
            for batch in clp.aggregate_dataframe(pipeline):
                aggregateResults = pd.concat(
                    [aggregateResults, batch], ignore_index=True, sort=False)
        except clappform.exceptions.HTTPError as exc:
            print(exc.response.text)
            print(exc.request.body)

        return aggregateResults
    
    def getOne(self, keyName, id, subject = "", filter= ""):
        result = []
        fullUrl = self.setFullUrl(keyName, id, subject, filter)

        if subject != "":
            keyName = subject

        response = requests.get(fullUrl)
        if response.status_code == 200:
                pageItems = response.json()[keyName]
                result.extend(pageItems)
        else:
            # Handle unsuccessful API response
            print(f"Failed to fetch data from URL: {fullUrl}")
        return result

    def getAll(self, keyname):
        return ""
    
        
