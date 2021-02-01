"""App: Dinner Roulette"""
import json
from flask import Flask, request
from modules.auth import verify_request
from modules.logger import logger
from modules.post_to_slack import post_message_to_slack, post_add_form
from modules.datasync import get_random_dinner, add_dinner
from modules.process_requests import process_incoming_req

app= Flask(__name__)

#TODO: Add Submitter(Source) to dinners

@app.route("/", methods=["GET"])
def home():
    logger.info("get recieved - home")
    return "HI, ALL IS WELL"

@app.route("/happenings", methods=["POST"])
def setName():
    logger.info("post recieved")
    if request.method=='POST':
        payload = request.form
        logger.debug(f'post recieved : {payload}') 
        data = payload['data']
        return {"Successfully stored ": str(data)}
    return None


@app.route("/dinnertime", methods=["POST"])
def pick_dinner():
    """Picks a Dinner for tonight"""
    logger.info("post recieved")
    stuff = get_random_dinner()
    return f"Try {stuff.dinner_name}, its pretty {stuff.difficulty}, and takes about {stuff.req_time} to cook. Tagged : {stuff.tags}"

@app.route("/newdinner", methods=["POST"])
def add_dinner_call():
    payload = request.form
    print(payload["trigger_id"])
    post_add_form(payload["trigger_id"], payload["channel_id"])
    #add_dinner("dinner1", "None", "Unknown")
    return "Thanks for your Additions!"

@app.route("/interactions", methods=["POST"])
def recieve_slack_data():
    #Verify Source
    if not verify_request(request):
        return "Authentication Failure"

    payload = json.loads(request.form["payload"])

    if payload["team"]["id"] == "T011PFPM8ET":
        process_incoming_req(payload)






    return ""

#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)

""" EXAMPLE RETURNS:
RECIEVE FROM COMMAND /DINNER_ADD:
([
   ("token",
   "8QHgcMgcrTnmPweNqcqZTA9M"")",
   "(""team_id",
   "T011PFPM8ET"")",
   "(""team_domain",
   "buckfamily10"")",
   "(""channel_id",
   "C01KUV74WKW"")",
   "(""channel_name",
   "test_menubot_channel"")",
   "(""user_id",
   "U012ACTAKHS"")",
   "(""user_name",
   "ephbuck"")",
   "(""command",
   "/dinner_add"")",
   "(""text",
   "".")",
   "(""api_app_id",
   "A01KUTK1Y0L"")",
   "(""is_enterprise_install",
   "false"")",
   "(""response_url",
   "https://hooks.slack.com/commands/T011PFPM8ET/1692218434869/whCc61hmfEPGO1XG5OuLoQTu"")",
   "(""trigger_id",
   "1680531407591.1057533722503.14eb9fc5dc92851468786a39033fa376"")"
])


RECIEVE FROM DINNER ADD BOX SUBMIT
{
   "type":"view_submission",
   "team":{
      "id":"T011PFPM8ET",
      "domain":"buckfamily10"
   },
   "user":{
      "id":"U012ACTAKHS",
      "username":"ephbuck",
      "name":"ephbuck",
      "team_id":"T011PFPM8ET"
   },
   "api_app_id":"A01KUTK1Y0L",
   "token":"8QHgcMgcrTnmPweNqcqZTA9M",
   "trigger_id":"1696502283859.1057533722503.bb42ced33ce5769dce4700ab065ced02",
   "view":{
      "id":"V01LG8HE1K4",
      "team_id":"T011PFPM8ET",
      "type":"modal",
      "blocks":[
         {
            "type":"input",
            "block_id":"add_dinner_name",
            "label":{
               "type":"plain_text",
               "text":"Name Your Dinner!",
               "emoji":true
            },
            "optional":false,
            "dispatch_action":false,
            "element":{
               "type":"plain_text_input",
               "action_id":"dinner_named",
               "placeholder":{
                  "type":"plain_text",
                  "text":"Kimchi Sandwich",
                  "emoji":true
               },
               "dispatch_action_config":{
                  "trigger_actions_on":[
                     "on_enter_pressed"
                  ]
               }
            }
         },
         {
            "type":"divider",
            "block_id":"z2tjE"
         },
         {
            "type":"section",
            "block_id":"add_dinner_diff",
            "text":{
               "type":"mrkdwn",
               "text":"Difficulty Rating:",
               "verbatim":false
            },
            "accessory":{
               "type":"radio_buttons",
               "action_id":"radio_buttons-action",
               "options":[
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"Easy",
                        "emoji":true
                     },
                     "value":"value-0"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"Medium",
                        "emoji":true
                     },
                     "value":"value-1"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"Hard",
                        "emoji":true
                     },
                     "value":"value-2"
                  }
               ]
            }
         },
         {
            "type":"divider",
            "block_id":"TpnW"
         },
         {
            "type":"section",
            "block_id":"add_dinner_time",
            "text":{
               "type":"mrkdwn",
               "text":"Prep and Cooking Time Requirments:",
               "verbatim":false
            },
            "accessory":{
               "type":"radio_buttons",
               "action_id":"radio_buttons-action",
               "options":[
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"under 30 min",
                        "emoji":true
                     },
                     "value":"value-0"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"30 min - 1 hour",
                        "emoji":true
                     },
                     "value":"value-0"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"1-2 hours",
                        "emoji":true
                     },
                     "value":"value-1"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"2+ hours",
                        "emoji":true
                     },
                     "value":"value-2"
                  }
               ]
            }
         },
         {
            "type":"divider",
            "block_id":"=Osw7"
         },
         {
            "type":"input",
            "block_id":"add_dinner_tags",
            "label":{
               "type":"plain_text",
               "text":"Tags - comma seperated",
               "emoji":true
            },
            "optional":true,
            "dispatch_action":false,
            "element":{
               "type":"plain_text_input",
               "action_id":"tags",
               "placeholder":{
                  "type":"plain_text",
                  "text":"Spicy, Kids hate it, Strong Flavor, Rotten cabbage",
                  "emoji":true
               },
               "min_length":0,
               "dispatch_action_config":{
                  "trigger_actions_on":[
                     "on_enter_pressed"
                  ]
               }
            }
         }
      ],
      "private_metadata":"",
      "callback_id":"",
      "state":{
         "values":{
            "add_dinner_name":{
               "dinner_named":{
                  "type":"plain_text_input",
                  "value":"TEST NAME"
               }
            },
            "add_dinner_diff":{
               "radio_buttons-action":{
                  "type":"radio_buttons",
                  "selected_option":{
                     "text":{
                        "type":"plain_text",
                        "text":"Easy",
                        "emoji":true
                     },
                     "value":"value-0"
                  }
               }
            },
            "add_dinner_time":{
               "radio_buttons-action":{
                  "type":"radio_buttons",
                  "selected_option":{
                     "text":{
                        "type":"plain_text",
                        "text":"under 30 min",
                        "emoji":true
                     },
                     "value":"value-0"
                  }
               }
            },
            "add_dinner_tags":{
               "tags":{
                  "type":"plain_text_input",
                  "value":"test, falass, just"
               }
            }
         }
      },
      "hash":"1612138599.V56rJ6Sz",
      "title":{
         "type":"plain_text",
         "text":"Add Dinner Form",
         "emoji":true
      },
      "clear_on_close":false,
      "notify_on_close":false,
      "close":{
         "type":"plain_text",
         "text":"Cancel",
         "emoji":true
      },
      "submit":{
         "type":"plain_text",
         "text":"Submit",
         "emoji":true
      },
      "previous_view_id":"None",
      "root_view_id":"V01LG8HE1K4",
      "app_id":"A01KUTK1Y0L",
      "external_id":"",
      "app_installed_team_id":"T011PFPM8ET",
      "bot_id":"B01KG1HBX9C"
   },
   "response_urls":[
      
   ],
   "is_enterprise_install":false,
   "enterprise":"None"
}
"""