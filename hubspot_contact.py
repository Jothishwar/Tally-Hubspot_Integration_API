import os
import json
from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput
from hubspot.crm.contacts.exceptions import ApiException

key = os.environ['hubspot app access token']
api_client = HubSpot(access_token=str(key))

def create_contact(properties):
  try:
    simple_public_object_input = SimplePublicObjectInput(properties)
    api_response = api_client.crm.contacts.basic_api.create(
        simple_public_object_input = simple_public_object_input
    )
    # print(api_response)
    return api_response.to_dict()
  except ApiException as e:
    return("Exception when creating contact: %s\n" % e)
