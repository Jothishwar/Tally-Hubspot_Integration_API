# import json
import os
from hubspot import HubSpot
from hubspot.crm.deals import SimplePublicObjectWithAssociations
from hubspot.crm.deals.exceptions import ApiException


key = os.environ['hubspot app access token']
api_client = HubSpot(access_token=str(key))

def create_deal(contact_id,fname,lname,tracks):
  deal={
    "properties": {
        "dealname": "",
        "tracks": "",
        "dealstage": "appointmentscheduled"
    },
    "associations": [
        {
            "to":{
              "id":0
            },
            "types": [
                {
                    "associationCategory": "HUBSPOT_DEFINED",
                    "associationTypeId": 3
                }
            ]
        }
    ]
  }

  deal["properties"]['dealname']=fname+" "+lname
  deal["properties"]['tracks']=";".join(tracks)
  deal["associations"][0]["to"]["id"]=int(contact_id)
  
  # print(deal)
  simple_public_object_with_association = SimplePublicObjectWithAssociations(properties=deal['properties'],associations=deal['associations'])
  try:
    deal_api_response = api_client.crm.deals.basic_api.create(
        simple_public_object_input = simple_public_object_with_association
    )
    print(deal_api_response)
    # return api_response.to_dict()
  except ApiException as e:
    print(e)
    return("Exception when creating deal: %s\n" % e)