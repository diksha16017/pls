from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6b41a6800ee914d17a2d01c1079bcc7e"

auth_token  = "fbf9988523947ca4fe19f2c52cb23d06"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919549151928",
    from_="+13345818216",
    body="Hello daddy!")

print(message.sid)