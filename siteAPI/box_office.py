import requests
import json
from Settings import ImdbSettings


def lst_box_office(file):
	result = []
	for item in json_response.values():
		if isinstance(item, list):
			for value in item:
				if isinstance(value, dict):
					tmp = [value.get("image"), value.get("title"), value.get("weekend")]
					result.append(tmp)
	return result


key_api = ImdbSettings()

url = f"https://imdb-api.com/en/API/BoxOffice/{key_api.site_api.get_secret_value()}"

response = requests.get(url)

json_response = json.loads(response.text)

lst = lst_box_office(json_response)


if __name__ == '__main__':
	lst_box_office(lst)

