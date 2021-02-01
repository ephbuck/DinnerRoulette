"""For Verifying Slack Signitures. DO NOT parse request before authenticating!"""
import hashlib
import hmac
import time
from config import SIGNING_SECRET


def verify_request(request):
    """Returns True if Signiture Authentication passes"""
    slack_signature = request.headers['X-Slack-Signature']
    slack_timestamp = request.headers['X-Slack-Request-Timestamp']
    req = str.encode('v0:' + str(slack_timestamp) + ':') + request.get_data()
    my_signature = 'v0=' + hmac.new(
            str.encode(SIGNING_SECRET),
            req, hashlib.sha256
        ).hexdigest()

    # Checks that the request is no more than 60 seconds old
    if (int(time.time()) - int(slack_timestamp)) > 60:
        print("Verification failed. Request is out of date.")
        return False

    if hmac.compare_digest(my_signature, slack_signature):
        return True
    else:
        print("Verification failed. Signature invalid.")
        return False
