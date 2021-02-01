from modules.datasync import add_dinner
from modules.post_to_slack import post_message_to_slack

def process_incoming_req(data):
    if data["type"] == "view_submission":
        if "add_dinner_name" in data["view"]["state"]["values"]:  #check_for_add_dinner(data):
            dinner_name = data["view"]["state"]["values"]["add_dinner_name"]["dinner_named"]["value"]
            dinner_diff = data["view"]["state"]["values"]["add_dinner_diff"]["radio_buttons-action"]["selected_option"]["text"]["text"]
            dinner_time = data["view"]["state"]["values"]["add_dinner_time"]["radio_buttons-action"]["selected_option"]["text"]["text"]
            dinner_tags = data["view"]["state"]["values"]["add_dinner_tags"]["tags"]["value"].split(", ")
            response = add_dinner(dinner_name, dinner_diff, dinner_time, dinner_tags)
            
            print("########################################")
            print(data["user"]["username"])
            print(data["view"]["private_metadata"])
            print("##########################################")

            temp_string = "New Dinner Idea was submitted by " + data["user"]["username"] + f".\nDinner Name: {response['name']} "
            temp_string2 =  f"\nEstimated Difficulty: {response['difficulty']} " + f"\nApproximate Time for Prep and cooking: {response['time']} "
            temp_string3 =  f"\nTags and Other Details: {response['tags']}"
            end_string = temp_string + temp_string2 + temp_string3
            post_message_to_slack(end_string, data["view"]["private_metadata"] )
            
                

temp = {
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
               "emoji":True
            },
            "optional":False,
            "dispatch_action":False,
            "element":{
               "type":"plain_text_input",
               "action_id":"dinner_named",
               "placeholder":{
                  "type":"plain_text",
                  "text":"Kimchi Sandwich",
                  "emoji":True
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
               "verbatim":False
            },
            "accessory":{
               "type":"radio_buttons",
               "action_id":"radio_buttons-action",
               "options":[
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"Easy",
                        "emoji":True
                     },
                     "value":"value-0"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"Medium",
                        "emoji":True
                     },
                     "value":"value-1"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"Hard",
                        "emoji":True
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
               "verbatim":False
            },
            "accessory":{
               "type":"radio_buttons",
               "action_id":"radio_buttons-action",
               "options":[
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"under 30 min",
                        "emoji":True
                     },
                     "value":"value-0"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"30 min - 1 hour",
                        "emoji":True
                     },
                     "value":"value-0"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"1-2 hours",
                        "emoji":True
                     },
                     "value":"value-1"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"2+ hours",
                        "emoji":True
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
               "emoji":True
            },
            "optional":True,
            "dispatch_action":False,
            "element":{
               "type":"plain_text_input",
               "action_id":"tags",
               "placeholder":{
                  "type":"plain_text",
                  "text":"Spicy, Kids hate it, Strong Flavor, Rotten cabbage",
                  "emoji":True
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
                        "emoji":True
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
                        "emoji":True
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
         "emoji":True
      },
      "clear_on_close":False,
      "notify_on_close":False,
      "close":{
         "type":"plain_text",
         "text":"Cancel",
         "emoji":True
      },
      "submit":{
         "type":"plain_text",
         "text":"Submit",
         "emoji":True
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
   "is_enterprise_install":False,
   "enterprise":"None"
}