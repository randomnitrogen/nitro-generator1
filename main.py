import sys
import requests
import random
import string
import time

def generate_random_code(length=18):
    """Generate a random alphanumeric string of given length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def send_request_and_process(code, webhook_url):
    """Send GET request to Discord API endpoint and process response."""
    url = f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}'
    params = {
        'with_application': 'false',
        'with_subscription_plan': 'true'
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            send_to_discord_webhook(webhook_url, f"Gift code {code} successfully sent to Discord webhook.")
            print(f"Gift code {code} successfully sent to Discord webhook.")
        else:
            log_message = f"Failed to send gift code {code} to Discord webhook. Status code: {response.status_code}"
            send_to_discord_webhook(webhook_url, log_message)
            print(log_message)
    except requests.exceptions.RequestException as e:
        log_message = f"Error sending gift code {code} to Discord webhook: {str(e)}"
        send_to_discord_webhook(webhook_url, log_message)
        print(log_message)

def send_to_discord_webhook(webhook_url, message):
    """Send the generated code to Discord webhook."""
    payload = {
        'content': message
    }
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        if response.status_code == 204:
            print("Successfully sent message to Discord webhook.")
        else:
            print(f"Failed to send message to Discord webhook. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Discord webhook: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_script.py <webhook_url>")
        sys.exit(1)

    DISCORD_WEBHOOK_URL = sys.argv[1]
    print("Logged in as Nitro Generator.")

    while True:
        code = generate_random_code()
        send_request_and_process(code, DISCORD_WEBHOOK_URL)
        time.sleep(1)  # Adjust this delay as needed to avoid rate limits or flooding
