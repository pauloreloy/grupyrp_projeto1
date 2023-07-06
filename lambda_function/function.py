import json
import boto3
import base64

def lambda_handler(event, context):
    
    client_rek = boto3.client("rekognition")
    
    try:
        if(event['headers']['content-type'] == 'image/jpeg'):
            image = base64.b64decode(event['body'])
            response = client_rek.detect_faces(Image = {"Bytes": image}, Attributes=['DEFAULT', 'SMILE'])
            smiling = 0
            response = json.dumps(response)
            dt = json.loads(response)
            for f in dt['FaceDetails']:
                if((f['Smile']['Value']) == True):
                    smiling = smiling + 1
            data = dict()
            resp = dict()
            data['totalfaces'] = len(dt['FaceDetails'])
            data['smiling'] = smiling
            resp['result'] = data
            resp = json.dumps(resp)
            return(resp)
        else:
            return "No image sent"
    except Exception as e:
        return "Error"