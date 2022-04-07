import json
import requests

def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    parsed_message = json.loads(message)
    topic=parsed_message['detail']['pipeline']
    time=parsed_message['time']
    state=parsed_message['detail']['state']
    #detail=parsed_message['additionalAttributes']['failedActions']
    #pipeline=json.loads(event['Records'][0]['Sns']['Message'])
    #time=json.loads(event['Records'][0]['Sns']['Message']['time'])
    #state=json.loads(event['Records'][0]['Sns']['Message']['detail']['state'])
    #detail=json.loads(event['Records'][0]['Sns']['Message']['additionalAttributes']['additionalInformation'])
    message=topic+state+time#+detail
    print(message)

    #print(message)
    #print(str(json.dumps(time)))

    body = json.dumps({
        "notification":message,
        "accessCode":"amzn1.ask.account.AEKA2MKAMLAVESKRGP64A4F7ASWEZBKKAH2Q4R6XDOQRVY5OXFWTZBDK5IF4VUWSMMYYHKWUTXZIGTP2L5RAAE4VS2ICTERFQ3YREO7YMAT22O5VVQQVQEIU2GDRSXLF6JWUJLZNJB7EWPPHXVSXIJTP4YZNWYCJDUQOF4267BFRDXLWTYBA2DEOQ55CPIYLG43A46ZJFGIEDJY"})

    requests.post(url='https://api.notifymyecho.com/v1/NotifyMe', data=body)