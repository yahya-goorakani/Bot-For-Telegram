
import requests

def get_updates(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    return requests.get(url).json()

def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    return requests.get(url, params=params).json()

def main():
    # Replace '*' with your actual token and chat_id
    TOKEN = "TOKEN_BOT"
    chat_id = "ID_CHAT"
    
    # Get updates
    updates = get_updates(TOKEN)
    print("Updates:", updates)

    # Send a message
    message = "Hello from your Telegram bot"
    response = send_message(TOKEN, chat_id, message)
    print("Message Response:", response)

if __name__ == "__main__":
    main()




