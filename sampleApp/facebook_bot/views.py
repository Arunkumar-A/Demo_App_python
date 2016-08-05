from django.views import generic
from django.http.response import HttpResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt


def post_facebook_message(sender_id,messageData):
         post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=Your_Access_Token' 
         response_msg = json.dumps({"recipient":{"id":sender_id}, "message":messageData})
         status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
         print(status.json()) 

#this is to send only text messages    
def sendMessage(sender_id,message):
    messageData = {"text":message}
    post_facebook_message(sender_id , messageData)

#this function is to send image message
def sendImage(sender_id,message):
    from templates import image_type    #Templates/image_type.py
    messageData = image_type.imageData
    post_facebook_message(sender_id , messageData)

#this function is to send Generic Message
def sendGeneric(sender_id,message):
    from templates import generic_type    #Templates/image_type.py
    messageData = generic_type.genericData
    post_facebook_message(sender_id , messageData)

#this function is to send Receipt Message
def sendReceipt(sender_id,message):
    from templates import receipt    #Templates/image_type.py
    messageData = receipt.rece
    post_facebook_message(sender_id , messageData)

#this function is to send Quick type Message
def sendQuickType(sender_id,message):
    from templates import quick_type    #Templates/image_type.py
    messageData = quick_type.quickData
    post_facebook_message(sender_id , messageData)

#this function is to send Airline type Message
def sendAirlineType(sender_id,message):
    from templates import airline_type    #Templates/image_type.py
    messageData = airline_type.airlineData
    post_facebook_message(sender_id , messageData)


class Facebook_view(generic.View):
    
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'Your_Verify_Token': #or your verify token
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
            messaging_events = json.loads(self.request.body.decode('utf-8'))
            
            if 'message' in messaging_events["entry"][0]["messaging"][0]:
                
                sender_id = messaging_events["entry"][0]["messaging"][0]["sender"]["id"]
                message = messaging_events["entry"][0]["messaging"][0]["message"]["text"]
                
                if message == 'image':
                    sendImage(sender_id,message)
                    
                elif message == 'generic':
                    sendGeneric(sender_id,message)
                    
                elif message == 'receipt':
                    sendReceipt(sender_id,message)
                    
                elif message == 'quick':
                    sendQuickType(sender_id,message)
                    
                elif message == 'airline' :
                    sendAirlineType(sender_id,message)
                    
                else:
                    sendMessage(sender_id,message)
            return HttpResponse()
    
class facebook(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World!")    