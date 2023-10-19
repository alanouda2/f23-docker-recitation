from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

RECITATION_HOURS = {"a": "09:00~09:50", "b": "10:00~10:50", "c": "11:00~11:50", "d": "12:00~12:50"}
MICROSERVICE_LINK = "https://whos-my-ta.fly.dev/section_id/"

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/section_info/{section_id}")
def get_section_info(section_id: str):
    if section_id is None:
        raise HTTPException(status_code=404, detail="Missing section id")

    section_id = section_id.lower()
    response = requests.get(MICROSERVICE_LINK + section_id)
    data = response.json()

    if "ta_names" not in data:
        raise HTTPException(status_code=404, detail="TA names not found for the section")

    ta_name_list = data["ta_names"]
    ta1_name = ta_name_list[0]["fname"] + " " + ta_name_list[0]["lname"]
    ta2_name = ta_name_list[1]["fname"] + " " + ta_name_list[1]["lname"]

    if section_id in RECITATION_HOURS:
        start_time, end_time = RECITATION_HOURS[section_id].split("~")
        return {
            "section": section_id,
            "start_time": start_time,
            "end_time": end_time,
            "ta": [ta1_name, ta2_name]
        }
    else:
        raise HTTPException(status_code=404, detail="Invalid section id")
