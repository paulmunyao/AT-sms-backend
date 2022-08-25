from __future__ import print_function
from flask import Flask

import africastalking


class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = "YOUR_USERNAME"
        self.api_key = "YOUR_API_KEY"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
        # Set the numbers you want to send to in international format
        recipients = ["+254715494857", "+254732841879"]

        # Set your message
        message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"

        # Set your shortCode or senderId
        # sender = "E-daktari"
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, recipients)
            print(response)
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))


if __name__ == '__main__':
    app.run(debug=True)
    SMS().send()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Helo, World!'