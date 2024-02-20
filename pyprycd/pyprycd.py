from functools import lru_cache

import pandas as pd
import requests
from requests import HTTPError


class PyPrycd:

    def __init__(self, pricing_api_key: str, comp_api_key: str) -> None:
        self.__pricing_api_key = pricing_api_key
        self.__comp_api_key =comp_api_key

    def set_pricing_api_key(self, pricing_api_key: str) -> None:
        self.__pricing_api_key = pricing_api_key

    def set_comp_api_key(self, comp_api_key: str) -> None:
        self.__comp_api_key = comp_api_key

    @lru_cache
    def get_pricing(self, apn: str, county_fips: str, latitude: float = None, longitude: float = None,
                    acreage: float = None, test: bool = False) -> pd.DataFrame:
        """
        Returns PRYCD estimated values for a requested property
        :param apn: The property Assessor Parcel Number (APN). (Required)
        :param county_fips: The County FIPS Code (Required)
        :param latitude: The latitude of the property. Used if the APN is not found.
        :param longitude: The longitude of the property. Used if the APN is not found.
        :param acreage: The acreage of the property. Used if the APN is not found.
        :param test: Whether or not to use the testing URL (Default: False)
        :return: A Pandas DataFrame of the PRYCD estimated pricing
        """

        if test is False:
            url = "https://gd4w0qoug6.execute-api.us-east-2.amazonaws.com/prod/api/priceProperty"
        else:
            url = "https://stoplight.io/mocks/prycd/pricing-api/109961998"

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-api-key': self.__pricing_api_key
        }

        data = {
            "apn": apn,
            "county_fips": county_fips,
        }

        if latitude is not None and longitude is not None:
            data['latitude'] = latitude
            data['longitude'] = longitude

        if acreage is not None:
            data['acreage'] = acreage

        response = requests.post(url=url, json=data, headers=headers)
        if response.status_code == 200:
            pricing_data = response.json()
            return pd.DataFrame.from_dict(pd.json_normalize(pricing_data['pricing']))

        raise HTTPError(response.status_code)

