import json
import watson_developer_cloud

import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

discovery = watson_developer_cloud.DiscoveryV1(
    '2016-12-01',
    username=os.environ.get("DISCOVERY_USERNAME"),
    password=os.environ.get("DISCOVERY_PASSWORD")
    )

environment_id = os.environ.get("DISCOVERY_ENVIRONMENT_ID")
collection_id = os.environ.get("DISCOVERY_COLLECTION_ID")

def display_discovery_query_response(json_data):
    for entry in json_data['results']:
        print("*** [{}] {}".format( entry['score'],
                                    entry['title'] ))
        for keyword in entry['enriched_text']['keywords']:
            if keyword['sentiment']['type'] == 'positive':
                print("+ [{}]".format(keyword['text']))
            if keyword['sentiment']['type'] == 'negative':
                print("- [{}]".format(keyword['text']))

if __name__ == '__main__':
    while 1:
        input_content = input('Discovery NLQ> ')
        if (input_content.lower() in {'exit', 'quit', 'q', 'n'})
            break

        query_options = { 'natural_language_query': input_content,
                         'count':10 }
        query_results = discovery.query(environment_id,
                                        collection_id,
                                        query_options)

        print(json.dumps(query_results, indent=2))
        print(display_discovery_query_response(query_results))
