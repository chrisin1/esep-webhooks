import json
import urllib3
def lambda_handler(event, context):
    http = urllib3.PoolManager()
    payload = json.dumps({'text': 'Issue Created: {}'.format(event['issue']['html_url'])})
    r = http.request('POST', '{do not check in this url}', headers={'Content-Type': 'application/json'}, body=payload)
    return {
        'statusCode': 200,
    }
