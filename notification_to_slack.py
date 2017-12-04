from slackclient import SlackClient
def slack_message(message, channel):
    token = 'xoxp-9449251159-218111562038-281208505140-d0b91765c8c2da175d40b1740419bfd4'
    sc = SlackClient(token)
    sc.api_call('chat.postMessage', channel=channel, 
                text=message, username='Wolverine',
                icon_emoji=':xmen:')

slack_message("This is just the test message", 'mytest')
