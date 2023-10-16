#!/usr/bin/env python3

import random

import fake_useragent
import requests
import uszipcode
from attrs import define


@define
class HondaDealer:
    name: str
    city: str
    state: str
    zipcode: int
    lat: float
    long: float


def get_random_honda_dealers(num: int = 1) -> list[HondaDealer]:
    zip_search = uszipcode.SearchEngine()
    zip_search_res = zip_search.by_population(
        sort_by=uszipcode.SimpleZipcode.population, ascending=False, returns=1000
    )
    random_zip = random.choice(zip_search_res)

    session = requests.session()
    session.headers = {"User-Agent": fake_useragent.UserAgent().random}
    honda_dealers_res = session.get(
        "https://automobiles.honda.com/platform/api/v2/dealer",
        params={
            "productDivisionCode": "A",
            "excludeServiceCenters": "false",
            "zip": random_zip.zipcode,
            "maxResults": "25",
        },
    )
    dealers_full = honda_dealers_res.json()
    dealers_list = dealers_full["Dealers"]
    if num > len(dealers_list):
        raise OverflowError(f"Requested {num} dealers but query only returned {len(dealers_list)}")
    dlrs = random.sample(dealers_list, num)
    return [
        HondaDealer(
            dlr["Name"],
            dlr["City"],
            dlr["State"],
            int(dlr["ZipCode"]),
            dlr["Latitude"],
            dlr["Longitude"],
        )
        for dlr in dlrs
    ]


if __name__ == "__main__":
    import sys

    from rich import print

    num_dlrs = 1
    if len(sys.argv) == 2:
        num_dlrs = int(sys.argv[1])
    dlrs = get_random_honda_dealers(num_dlrs)
    for dlr in dlrs:
        print(dlr)
