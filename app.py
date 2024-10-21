import requests


BOT_TOKEN = 'YOUR_BOT_TOKEN' # Replace with your bot token 
CHAT_ID = 'YOUR_CHAT_ID' # Replace with your bot chat ID

def send_message(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")


send_message("Hello from my bot!") # Send a test message
