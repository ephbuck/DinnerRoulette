"""Posts data to slack"""
import os.path
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import SLACK_TOKEN

client = WebClient(token=SLACK_TOKEN)


def post_message_to_slack(text, slack_channel, trigger_id=None, slack_user_name=None):
	"""posts to slack. pass in text and channel NAME, OPTIONALLY slack username and blocks"""
	
	try:
		response = client.chat_postMessage(channel=slack_channel, text=text, username=slack_user_name if slack_user_name else None)
		assert response["message"]["text"] == text
	except SlackApiError as e:
    	# You will get a SlackApiError if "ok" is False
		assert e.response["ok"] is False
		assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
		print(f"Got an error: {e.response['error']}")

	#AlTERNATE Method
    # return requests.post('https://slack.com/api/chat.postMessage', {
    #     'token': 'TOKEN', #SLACK_TOKEN ,
    #     'channel': slack_channel,
    #     'text': text,
    #     'username': slack_user_name if slack_user_name else None,
    #     'blocks': json.dumps(blocks) if blocks else None
    # }).json()

def post_add_form(trigger_id, channel_id):
	with open(os.path.dirname(__file__) + '/../modal.txt') as modalfile:
		print(type(modalfile))
		print(modalfile)
		modal = json.loads(modalfile.read() )
		print(type(modal))
		modal["private_metadata"] = channel_id
		return client.views_open(trigger_id=trigger_id,view=modal)

#print(post_message_to_slack("test", "test_menubot_channel", blocks=block_test2))
#post_message_to_slack("test", "test_menubot_channel")