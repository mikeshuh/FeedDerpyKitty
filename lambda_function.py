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
    
    twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
    twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
    girlfriend_phone_number = os.environ['GIRLFRIEND_PHONE_NUMBER']
    
    client = Client(twilio_account_sid, twilio_auth_token)
    
    messages = [
        # Classic love messages
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
        "Just because I love you and wanted you to know! 💖",
        
        # Thinking of you messages
        "Can't stop thinking about your beautiful smile 😊",
        "You've been on my mind all day ❤️",
        "Daydreaming about you right now 💭💕",
        "Your laugh is stuck in my head and I love it 😄❤️",
        "Thinking about how lucky I am to have you 🍀💖",
        "You popped into my thoughts and made me smile 😊",
        "Missing your voice right now 💕",
        "Wishing I could give you a hug right now 🤗",
        "You're always in my thoughts ❤️",
        "Can't wait to see you again! ❤️",
        
        # Compliment messages
        "You're absolutely stunning inside and out 💖",
        "Your kindness amazes me every day 🌟",
        "You have the most beautiful heart ❤️",
        "Your intelligence is so attractive 🧠💕",
        "You light up every room you enter ✨",
        "Your sense of humor is the best! 😂❤️",
        "You're stronger than you know 💪💖",
        "Your creativity inspires me daily 🎨❤️",
        "You're perfectly imperfect and I love it all 💕",
        "Your passion for life is contagious 🌟",
        
        # Encouragement messages
        "You've got this! I believe in you 💪❤️",
        "Remember how amazing you are! 🌟",
        "You're capable of incredible things 💫",
        "Sending you strength and love 💪💕",
        "You're handling everything so well ❤️",
        "I'm proud of you every single day 🥰",
        "You're doing better than you think! 💖",
        "Keep being your awesome self! ⭐",
        "You inspire me to be better 🌟❤️",
        "Your resilience is beautiful 💪💕",
        
        # Fun and playful messages
        "You're my favorite weirdo 🤪❤️",
        "Still can't believe you chose me! 😁💕",
        "You're stuck with me forever! 😘",
        "Warning: thinking about you again! ⚠️💖",
        "You're my person and I'm your person 👫❤️",
        "Plot twist: I love you even more today! 📈💕",
        "You make my heart do backflips 🤸‍♀️❤️",
        "Currently obsessed with you (as usual) 😍",
        "You're my favorite notification 📱💕",
        "Still falling for you every day 🍂❤️",
        
        # Sweet and romantic
        "You're my forever and always 💍❤️",
        "In a world of chaos, you're my peace 🕊️💕",
        "You're my happy place 🏡❤️",
        "With you, everything feels right 💖",
        "You're my greatest adventure 🗺️❤️",
        "Home is wherever you are 🏠💕",
        "You're my safe haven 🌊❤️",
        "Every love song reminds me of you 🎵💖",
        "You're my dream come true ✨❤️",
        "Forever grateful you're mine 🙏💕",
        
        # Random sweet messages
        "You're my favorite human ever! 👫❤️",
        "Still can't get over how amazing you are! 🤯💕",
        "You make ordinary moments magical ✨❤️",
        "Thank you for being you! 🙏💖",
        "You're the reason I smile so much 😊❤️",
        "Lucky doesn't even begin to cover it! 🍀💕",
        "You're my greatest blessing 🙌❤️",
        "Life is so much better with you in it! 🌈💖",
        "You're worth every star in the sky! ⭐💕",
        "My heart is so full because of you! ❤️",
        
        # Appreciation messages
        "Grateful for your beautiful soul! 🙏💕",
        "Thank you for being my rock! 🪨❤️",
        "Appreciate everything you do! 💖",
        "You make everything better! ⬆️❤️",
        "So thankful you're in my life! 🙏💕",
        "Your love means everything to me! 💯❤️",
        "Couldn't ask for anyone better! 💖",
        "You're a gift I treasure daily! 🎁💕",
        "Grateful for your patient heart! ❤️",
        "Thank you for loving me! 🙏💖",
        
        # More variety
        "You're absolutely incredible ⭐❤️",
        "Sending virtual hugs your way! 🤗💕",
        "You're my heart's favorite rhythm 💓",
        "Still amazed by your awesomeness! 🤩❤️",
        "You're my definition of perfect 💯💖",
        "Can't help but adore you! 🥰💕",
        "You're my source of happiness 😊❤️",
        "Feeling grateful for you right now 🙏💖",
        "You're simply amazing! ✨💕",
        "Love you more than words can say! 💬❤️"
    ]
    
    try:
        message = random.choice(messages)
        
        current_time = datetime.now(timezone.utc)
        time_str = current_time.strftime("%I:%M %p")
        
        message_instance = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=girlfriend_phone_number
        )
        
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