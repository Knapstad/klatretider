import json

Class Klaterverket():    
    @classmethod
    def get_times(cls, types: list = None) -> dict:
        with open("api.json") as file:
            data = json.load(file)
        apis = [item["url"] for item in data if "klatreverket" in item["navn"].lower()]
        






SELECT count(*)
FROM `obos-225315.161770077.ga_sessions_*`
LIMIT 100