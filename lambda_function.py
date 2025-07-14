import json
import random
import os
from datetime import datetime, timezone
from twilio.rest import Client

def lambda_handler(event, context):
    """
    AWS Lambda function to send automated love messages
    Triggered by EventBridge (CloudWatch Events) cron schedule
    Twilio automatically handles START/STOP opt-out compliance
    """
    
    # Get environment variables
    twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
    twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
    girlfriend_phone_number = os.environ['GIRLFRIEND_PHONE_NUMBER']
    
    # Initialize Twilio client
    client = Client(twilio_account_sid, twilio_auth_token)
    
    # List of loving messages (add/customize as needed)
    messages = [
        "Hey beautiful! Just wanted to remind you that I love you ❤️",
        "Thinking of you and smiling 😊 Love you so much!",
        "You're the best part of my day! I love you! 💕",
        "Just a little reminder that you're amazing and I love you!",
        "Hope you're having a wonderful day! Love you tons! 🥰",
        "You make everything better just by existing. I love you! ✨",
        "Missing you and loving you every moment! 💖",
        "You're my favorite person in the world! Love you! 🌟",
        "Just wanted to tell you how much I care about you! ❤️",
        "You're incredible and I'm so lucky to have you! Love you! 💝",
        "Sending you love and good vibes! 🌈❤️",
        "You're on my mind and in my heart always! Love you! 💕",
        "Hope you're smiling because I'm thinking of you! 😘",
        "You're my sunshine on any day! I love you! ☀️❤️",
        "Just because I love you and wanted you to know! 💖"
    ]
    
    try:
        # Select a random message
        message = random.choice(messages)
        
        # Add timestamp for context (optional)
        current_time = datetime.now(timezone.utc)
        time_str = current_time.strftime("%I:%M %p")
        
        # Send the message
        message_instance = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=girlfriend_phone_number
        )
        
        # Log success
        print(f"Message sent successfully at {time_str}")
        print(f"Message SID: {message_instance.sid}")
        print(f"Message content: {message}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Love message sent successfully!',
                'sid': message_instance.sid,
                'timestamp': time_str
            })
        }
        
    except Exception as e:
        print(f"Error sending message: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'message': 'Failed to send love message'
            })
        }

def get_time_specific_message():
    """
    Return different messages based on time of day
    """
    current_hour = datetime.now().hour
    
    if 6 <= current_hour < 9:
        return "Good morning gorgeous! Hope you have an amazing day! I love you! 🌅❤️"
    elif 9 <= current_hour < 12:
        return "Hope your morning is going great! Love you so much! ☀️💕"
    elif 12 <= current_hour < 17:
        return "Afternoon check-in: You're wonderful and I love you! 🌞❤️"
    elif 17 <= current_hour < 21:
        return "Evening love! Hope you're having a good time! Love you! 🌆💖"
    else:
        return "Late night love from me to you! Sweet dreams soon! 🌙❤️"
