import requests
from Settings import SiteApiKey


def get_requests(parameter: str, value: str, choice_sort: str, reverse=False):
    """Функция принимает значения, по которым отправляет запрос на сайт Api.
    Принимает запрос и возвращает отсартированный список."""
    params = f"&{parameter}={value}"
    key_api = SiteApiKey()
    api_url = f"https://api.api-ninjas.com/v1/dogs?"
    response = requests.get(
        api_url + params, headers={"X-Api-Key": key_api.site_api.get_secret_value()}
    )
    data = response.json()
    data_sort = sorted(
        data, key=lambda val: val[f"min_{choice_sort}_female"], reverse=reverse
    )
    return data_sort
