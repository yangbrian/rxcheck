__author__ = 'Brian'

from pymongo import MongoClient
import requests, json, time

def saveToDatabase(data):
    #Connect to mongodb client
    client = MongoClient('localhost', 27017)

    #Get the database
    db = client.rxcheck

    #Get the collection
    collection = db.medInfo

    #Save a new document into the collection
    # collection.insert_one(data)

    print(data)

def getNumOfDrugs():
    url = 'https://api.fda.gov/drug/label.json'
    r = requests.get(url)
    return (json.loads(r.text)['meta']['results']['total'])


#url of FDA API. maxxed out limit lol
url = 'https://api.fda.gov/drug/label.json?limit=100'

#We can only send 240 API requests a minute.
offset = 0
numNamedDrugs = 0
while offset < getNumOfDrugs():
    #launch request, convert json to dict
    r = requests.get((url + 'skip=' + offset), data={'apikey': 'PbYvWZzzI8MkEZwGVYCdNXb8kZIp4Itcrp6hfZNJ'})
    data = json.loads(r.text)

    for drug in data['results']:
        #If the drug has no name, we don't really care about it
        if 'brand_name' in drug['openfda'] or 'generic_name' in drug['openfda']:
            #20 lashes for what I'm about to write...
            drugInfo = {'_id': drug['openfda']['brand_name'] if 'brand_name' in drug['openfda'] else drug['openfda']['generic_name'],
                          'generic_name': drug['openfda']['generic_name'] if 'generic_name' in drug['openfda'] else '',
                          'do_not_use': drug['do_not_use'] if 'do_not_use' in drug else '',
                          'stop_use': drug['stop_use'] if 'stop_use' in drug else '',
                          'boxed_warning': drug['boxed_warning'] if 'boxed_warning' in drug else '',
                          'warnings_and_precautions':  drug['warnings_and_precautions'] if 'warnings_and_precautions' in drug else '',
                          'warnings': drug['warnings'] if 'warnings' in drug else '',
                          'user_safety_warnings': drug['user_safety_warnings'] if 'user_safety_warnings' in drug else '',
                          'precautions': drug['precautions'] if 'precautions' in drug else '',
                          'general_precautions': drug['general_precautions'] if 'general_precautions' in drug else '',
                          'use_in_specific_populations': drug['use_in_specific_populations'] if 'use_in_specific_populations' in drug else '',
                          'package_label_principal_display_panel': drug['package_label_principal_display_panel'] if 'package_label_principal_display_panel' in drug else '',
                          'information_for_patients': drug['information_for_patients'] if 'information_for_patients' in drug else '',
                          'when_using': drug['when_using'] if 'when_using' in drug else '',
                          'inactive_ingredient': drug['inactive_ingredient'] if 'inactive_ingredient' in drug else '',
                          'active_ingredient': drug['active_ingredient'] if 'active_ingredient' in drug else '',
                          'ask_doctor': drug['ask_doctor'] if 'ask_doctor' in drug else '',
                          'ask_doctor_or_pharmacist': drug['ask_doctor_or_pharmacist'] if 'ask_doctor_or_pharmacist' in drug else '',
                          'other_safety_information': drug['other_safety_information'] if 'other_safety_information' in drug else '',
                      }
            saveToDatabase(drugInfo)
            numNamedDrugs += 1

    #set offset
    offset += 100

    #wait a minute
    time.sleep(60)

print('We have ' + numNamedDrugs + ' named drugs saved.')