from dotenv import load_dotenv
import os, requests

load_dotenv()
url = os.getenv("API_URL")


def fetch_countries_datas():
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.json()
        else:
            print(
                f"Error occured during fetching data. Status Code : {response.status_code}"
            )
            return None
    except Exception as e:
        print(f"Error occured while fetching data from api : {e}")
        return None
