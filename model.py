import json
from os import access, times
import meraki
import requests
from webexteamssdk import WebexTeamsAPI
from datetime import datetime,timedelta
import time

#CHANGE TO .env
API_KEY = '3cbdcc94a33f6ec70d6189a6441fc98ba200f40b'
WEBEX_KEY = 'YjYxMTk3ZjktYmYyYS00YzdiLWIzZGQtZjZkYTRmNWYwNmM5ZmQyNGUzYzUtMWU5_P0A1_9c947ef3-ba2a-406e-9976-6a57f8f739b7'
ORG_ID = '578350'


FORMAT_CARD = {
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Equipo 5 Meraki Challenge",
                            "horizontalAlignment": "Center",
                            "size": "Medium",
                            "color": "Attention"
                        },
                        {
                            "type": "TextBlock",
                            "weight": "Bolder",
                            "text": "Detected Plate ",
                            "color": "Light",
                            "size": "Large",
                            "spacing": "Small"
                        }
                    ],
                    "width": "stretch"
                }
            ]
        },
        {
            "type": "Image",
            "url": "image_url"
        },
        {
            "type": "TextBlock",
            "text": "Camera with serial X identified the following plate. Plate related info:",
            "wrap": True
        },
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "width": 35,
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Plate number:",
                            "color": "Light"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Name:",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Id info:",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Served:",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Time:",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Order:",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Order size:",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        }
                    ]
                },
                {
                    "type": "Column",
                    "width": 65,
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "",
                            "color": "Light"
                        },
                        {
                            "type": "TextBlock",
                            "text": "",
                            "color": "Light",
                            "weight": "Lighter",
                            "spacing": "Small"
                        },
                        {
                            "type": "TextBlock",
                            "text": "",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        },
                        {
                            "type": "TextBlock",
                            "text": "",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        },
                        {
                            "type": "TextBlock",
                            "text": "",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        },
                        {
                            "type": "TextBlock",
                            "text": "",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        },
                        {
                            "type": "TextBlock",
                            "text": "",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        }
                    ]
                }
            ],
            "spacing": "Padding",
            "horizontalAlignment": "Center"
        },
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "width": "auto",
                    "items": [
                        {
                            "type": "Image",
                            "altText": "",
                            "url": "https://developer.webex.com/images/link-icon.png",
                            "size": "Small",
                            "width": "30px"
                        }
                    ],
                    "spacing": "Small"
                },
                {
                    "type": "Column",
                    "width": "auto",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "[Image link for download]()",
                            "size": "Medium"
                        }
                    ],
                    "verticalContentAlignment": "Center",
                    "spacing": "Small"
                }
            ]
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.2"
}



baseUri = 'https://api.meraki.com/api/v1'
dashboard = meraki.DashboardAPI(API_KEY)
webexAPI = WebexTeamsAPI(access_token = WEBEX_KEY)

serial = 'Q2HV-WCAN-VATL' #front camera
serial2 = 'Q2CV-FAH2-Z5JL' #rear camera

timeStamp = "2021-10-28T11:00:00.000" #dummy time

response = dashboard.camera.generateDeviceCameraSnapshot(serial, timeStamp = timeStamp)

time.sleep(3)

imageURL = str(response.get('url'))

###########################################POSTEAR EN BOT####################################################

url = "https://webexapis.com/v1/messages"



#sala team
#team_room = "Y2lzY29zcGFyazovL3VzL1JPT00vOGVmZjA2ZDAtMzZhMy0xMWVjLWI0Y2ItMGY2MDM0ZmJhOWIz"

#sala pruebas
team_room = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYTg4MTE2MjAtMzgxYS0xMWVjLTgyNDAtNTlkZDRjZTMyOTlh"
text = "Envio de foto de cámara con serial " + serial

headers_bot = {
  'Authorization': 'Bearer YjYxMTk3ZjktYmYyYS00YzdiLWIzZGQtZjZkYTRmNWYwNmM5ZmQyNGUzYzUtMWU5_P0A1_9c947ef3-ba2a-406e-9976-6a57f8f739b7',
  'Content-Type': 'application/json'
}

data = json.dumps({
  "files": [
    imageURL
  ],
  "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYTg4MTE2MjAtMzgxYS0xMWVjLTgyNDAtNTlkZDRjZTMyOTlh",
  "text": "Ej"
})

def postCardWebex(plateNumber, serialNum):

    #parameters received
    FORMAT_CARD["body"][1]["url"] = imageURL
    FORMAT_CARD["body"][0]["columns"][0]["items"][1]["text"] = "Plate detected: " + plateNumber
    FORMAT_CARD["body"][2]["text"] = "Camera with serial " + serialNum + " identified the following plate. Plate related info:"
   

    time.sleep(3)

    webexAPI.messages.create(
        roomId = team_room,
        text = "Render card failed.",
        attachments=[{
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": FORMAT_CARD
        }]
    )
    return
    
###########################################FUNCTIONS TO FORMAT####################################################

def receiveAlert(alert):
    #return here the image for the recognition.

    return

def plateRecognition():
    plateNumber = '12345678'
    #use the CV for returning plate number if detected or 0 otherwise

    postCardWebex(plateNumber, serial)

plateRecognition()
