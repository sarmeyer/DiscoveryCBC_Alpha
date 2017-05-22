import sys
import os
import json
import time
import pandas as pd
from watson_developer_cloud import DiscoveryV1
import argparse

from os.path import join, dirname
from dotenv import load_dotenv
import os

def read_json_file(file_path):
    with open(file_path) as json_file:
        json_content = json_file.read()
        json_data = json.loads(json_content)
    return(json_data)

def display_results(response):
    print(json.dumps(response), indent = 2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("query_file")
    args = parser.parse_args()

    dotenv_path = join(dirname(__file__), '.gitignore')
    load_dotenv(dotenv_path)

    query_json = read_json_file(args.query_file)

    discovery = DiscoveryV1(
        username=os.environ.get("DISCOVERY_USERNAME"),
        password=os.environ.get("DISCOVERY_PASSWORD"),
        version="2016-12-01"
    )

    collection_id = os.environ.get('DISCOVERY_COLLECTION_ID')
    configuration_id = os.environ.get('DISCOVERY_CONFIGURATION_ID')
    environment_id = os.environ.get('DISCOVERY_ENVIRONMENT_ID')

    response = discovery.query(environment_id,
                               collection_id,
                               query_json)
    display_results(response)
