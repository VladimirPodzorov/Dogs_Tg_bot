import requests
from Settings import SiteApiKey


def get_cust_requests(min_height="", max_height="", min_weight="", max_weight=""):
    params = f"&min_height={min_height}&max_height={max_height}&min_weight={min_weight}&max_weight={max_weight}"
    key_api = SiteApiKey()
    api_url = f"https://api.api-ninjas.com/v1/dogs?"
    response = requests.get(
        api_url + params, headers={"X-Api-Key": key_api.site_api.get_secret_value()}
    )
    data = response.json()
    return data
