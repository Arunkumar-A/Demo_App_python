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
            "image_url":"https://www.theupsstore.com/Image%20Library/theupsstore/general-content/gc1/gc1_packing-sports-equipment.jpg",
            "subtitle":" Subtitle of the image.",
            "buttons":[
              {
                "type":"web_url",
                "url":"www.google.com",
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