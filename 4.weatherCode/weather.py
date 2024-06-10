import requests
import json
import tkinter as tk
from tkinter import messagebox

# 發送請求並取得天氣數據
def get_weather_data():
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-067"   #氣象署申請weather api
    params = {
        "Authorization": "CWA-AEB1C177-1904-4614-A21A-AA9FB51F7AFB",    # 氣象署授權碼
        "limit": 10,
        "offset": 0,
        "format": "JSON"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 擷取並顯示天氣資訊
def show_weather():
    data = get_weather_data()
    if data:
        try:
            location_name = data['records']['locations'][0]['location'][0]['locationName']
            weather_elements = data['records']['locations'][0]['location'][0]['weatherElement']

            # 取得溫度
            temperature = None
            for element in weather_elements:
                if element['elementName'] == 'T':
                    temperature = element['time'][0]['elementValue'][0]['value']
                    break

            # 取得描述
            description = None
            for element in weather_elements:
                if element['elementName'] == 'Wx':
                    description = element['time'][0]['elementValue'][0]['value']
                    break

            if temperature and description:
                result = f"Location: {location_name}\nTemperature: {temperature}\nDescription: {description}"
            else:
                result = "Failed to retrieve complete weather data"
        except Exception as e:
            result = f"Error occurred: {e}"
    else:
        result = "Failed to retrieve weather data"

    messagebox.showinfo("Weather Information", result)

# 建立主視窗
root = tk.Tk()
root.title("Weather App")

# 建立一個取得天氣資訊的按鈕
get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=20)

# 運行主循環
root.mainloop()
