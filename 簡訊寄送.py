from twilio.rest import Client #載入套件，載twilio公司客戶的部分

# Your Account SID from twilio.com/console  加密
account_sid = "**********************"
# Your Auth Token(權杖) from twilio.com/console
auth_token  = "**********************"

client = Client(account_sid, auth_token)  #Client是class，後面配上()是指把物件建立實體化

message = client.messages.create(
    to="+886912345678", 
    from_="+123456789",
    body="Hello from Python!")

print(message.sid)