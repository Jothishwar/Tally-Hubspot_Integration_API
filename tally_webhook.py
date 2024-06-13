import json
from hubspot_contact import create_contact
from hubspot_deal import create_deal

def new_response(data):
  details = parse_form_data(data)
  # print(details)
  hubspot_response = create_contact(details)
  contact_id=hubspot_response['id']

  tracks_and_how=get_tracks(data['data']['fields'])
  create_deal(contact_id,details['firstname'],details['lastname'],tracks_and_how['tracks'])
  # return hubspot_response

def parse_form_data(data):
  form_response = {}
  
  fullname = data['data']['fields'][0]['value']
  split_name_info = split_name(fullname)

  form_response['firstname'] = split_name_info['firstname']
  form_response['middlename'] = split_name_info['middlename']
  form_response['lastname'] = split_name_info['lastname']

  form_response['email']=data['data']['fields'][1]['value']
  form_response['phone']=data['data']['fields'][2]['value']
  # form_response['linkedin_link']=data['data']['fields'][3]['value']
  
  # tracks_and_how=get_tracks(data['data']['fields'])
  # form_response['tracks']=tracks_and_how['tracks']
  # form_response['How did you get to know about us?']=tracks_and_how['how']
  
  return form_response


def split_name(full_name):
  # Split the full name into individual words
  name_parts = full_name.split()
  
  # Extract the first name, last name, and middle name (if present)
  first_name = name_parts[0]
  last_name = name_parts[-1]
  middle_name = ""
  
  if len(name_parts) > 2:
      middle_name = " ".join(name_parts[1:-1])
  
  # Print the results
  split_name_info={
      "firstname" : first_name,
      "middlename" : middle_name,
      "lastname" : last_name
  }
  return split_name_info

def get_tracks(fields):
    info={}
    tracks=[]
    for field in fields:
        if (field['label'] == 'Tracks'):
            # print(field)
            for option in field['options']:
                # print(option)
                if(option['id'] in field['value']):
                    tracks.append(option['text'])
        elif (field['type'] == 'DROPDOWN'):
            # print(field)
            for option in field['options']:
                # print(option)
                if(option['id'] in field['value']):
                    info['how']=option['text']
    info['tracks']=tracks
    return info