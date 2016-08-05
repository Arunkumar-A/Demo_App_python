# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 15:37:45 2016

@author: Welcome
"""

genericData = {
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
          {
            "title":"generic Example",
            "image_url":"Utl of the image",
            "subtitle":" Subtitle of the image.",
            "buttons":[
              {
                "type":"web_url",
                "url":"Your_web_url",
                "title":"Title of the URL"
              },
              {
                "type":"postback",
                "title":"Title for that postback",
                "payload":"USER_DEFINED_PAYLOAD"
              }              
            ]
          }
        ]
      }
    }
    }