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
    
    prepend_message = "New Derpy Kitty Mail!:\n"

    messages = [
        "Hey Krissy 🐝 just thinking about you and how lucky I am to have you 🐥💛",
        "Baby Bee 🐝 you make my whole world brighter, like a tiny lantern bug 🐞✨",
        "Stinky 🦊 you're my favorite human and also my favorite weirdo 🐸💕",
        "Bubba 🐻 you make even the most boring days feel like an adventure 🐾💛",
        "Bug Bug 🐞 you're basically my emotional support cutie 🐰🌸",
        "Krissy 🐝 you're the marshmallow to my hot cocoa 🦦☕",
        "Baby Bee 🐝 I hope you know I'd give you the last bite of my fries 🐧🍟",
        "Stinky 🦝 you're my favorite person to be goofy with 🐒💛",
        "Bubba 🐻 if you were a bug, I'd still keep you in my pocket 🐞💖",
        "Bug Bug 🐞 you're my perfect little chaos gremlin 🐈✨",
        "Krissy 🐝 you make me smile like an idiot every single day 🐢🌼",
        "Baby Bee 🐝 you're the best thing since sliced bread (and way cuter) 🐥🍞",
        "Stinky 🐼 I don't know how you put up with me, but I'm so glad you do 🦆💛",
        "Bubba 🐻 you make life feel like a cozy blanket fort 🦔☕",
        "Bug Bug 🐞 just wanted to say you're the cutest bug in the whole bug kingdom 🐛👑",
        "Krissy 🐝 I'd share my snacks with you, even the really good ones 🐸🍪",
        "Baby Bee 🐝 you make my heart do little flips like a silly dolphin 🐬💛",
        "Stinky 🐨 you're the perfect mix of sweet and chaos 🐥✨",
        "Bubba 🐻 you're the peanut butter to my jelly, but way less sticky 🦊🥪",
        "Bug Bug 🐞 you make my brain go 'happy happy happy' 🐢💭",
        "Krissy 🐝 you're my favorite cuddle buddy and life buddy 🐻💛",
        "Baby Bee 🐝 you make even a Tuesday feel special 🐱🌼",
        "Stinky 🐒 you're my silly goose forever 🦢💛",
        "Bubba 🐻 you're the best decision I've ever made 🦦🌸",
        "Bug Bug 🐞 you're basically a walking serotonin dispenser 🐰💛",
        "Krissy 🐝 just a reminder that you're my whole world 🐧🌎",
        "Baby Bee 🐝 you're my best friend and my favorite person 🐶💛",
        "Stinky 🐼 you're the perfect combination of cute and chaos 🐥🌼",
        "Bubba 🐻 I'd give you all my fries and my hoodie 🐸🍟",
        "Bug Bug 🐞 you're my sunshine in human form 🐤🌻",
        "Krissy 🐝 I like you more than coffee, and that's saying a lot ☕🐱",
        "Baby Bee 🐝 you're basically my personal happiness upgrade 🦋💛",
        "Stinky 🐒 you're my forever favorite, even when you're weird 🐸💕",
        "Bubba 🐻 you make life so much better just by being in it 🐾🌼",
        "Bug Bug 🐞 you're my silly little bug and I love it 🐛💛",
        "Krissy 🐝 if you were a snack, you'd be the best one in the pantry 🐼🍪",
        "Baby Bee 🐝 I'm so proud to love you every single day 🦊💛",
        "Stinky 🐨 you make me laugh harder than anyone else 🐥✨",
        "Bubba 🐻 just wanted to say thanks for being my favorite human 🐸🌼",
        "Bug Bug 🐞 you make my brain go ‘✨!!!✨' 🐈💛",
        "Krissy 🐝 you're my perfect mix of cozy and chaos 🐻☕",
        "Baby Bee 🐝 I'd always pick you, every single time 🐢💛",
        "Stinky 🐼 you make my life infinitely better 🐥🌼",
        "Bubba 🐻 you're the cutest thing that's ever happened to me 🦦💖",
        "Bug Bug 🐞 you're basically my happy place 🐰💛",
        "Krissy 🐝 you're the best part of my entire day 🐸☀️",
        "Baby Bee 🐝 you're my forever favorite bug 🐛💛",
        "Stinky 🐨 you're adorable even when you're being a menace 🐒✨",
        "Bubba 🐻 you're the softest part of my life 🐾🌼",
        "Bug Bug 🐞 you're my best friend and partner in chaos 🐈💛",
        "Krissy 🐝 you make my heart all warm and fuzzy 🐻☕",
        "Baby Bee 🐝 you're the best kind of silly 🐥🌸",
        "Stinky 🐼 you're my favorite person to do absolutely nothing with 🐸💛",
        "Bubba 🐻 you're basically the coziest thing in existence 🦊🛏️",
        "Bug Bug 🐞 I just think you're the best, that's all 🐢💛",
        "Krissy 🐝 you're my forever silly goose 🦢🌼",
        "Baby Bee 🐝 I hope you know you're my entire heart 🐰💛",
        "Stinky 🐒 you're my tiny bundle of chaos and I love it 🐥✨",
        "Bubba 🐻 you're basically my favorite comfort food in human form 🐸🍜",
        "Bug Bug 🐞 you're my favorite bug in the entire world 🐛💛",
        "Krissy 🐝 I like you more than all the snacks combined 🐼🍫",
        "Baby Bee 🐝 you're my coziest little human 🐻🛏️",
        "Stinky 🐨 you make life so much sillier and sweeter 🐥💛",
        "Bubba 🐻 you're my daily dose of joy 🦦🌸",
        "Bug Bug 🐞 you're my forever bestie and lovebug 🐛💛",
        "Krissy 🐝 just wanted to say you're my everything 🐧☀️",
        "Baby Bee 🐝 you're the peanut butter to my banana 🐒🍌",
        "Stinky 🐼 you're my personal serotonin factory 🐥💛",
        "Bubba 🐻 you're my cozy little home in human form 🐾🏡",
        "Bug Bug 🐞 you make my life way more fun 🐢💛",
        "Krissy 🐝 you're my silly little partner in crime 🐱✨",
        "Baby Bee 🐝 I wouldn't trade you for all the snacks in the world 🐼🍪",
        "Stinky 🐨 you're my favorite person to annoy forever 🐥💛",
        "Bubba 🐻 you're my warm hug in human form 🦊☕",
        "Bug Bug 🐞 you're my sunshine bug 🐛🌻",
        "Krissy 🐝 you're basically my favorite human-shaped dopamine 🐸💛",
        "Baby Bee 🐝 you're my silly little soul mate 🐥✨",
        "Stinky 🐼 you're my best friend forever 🐢💛",
        "Bubba 🐻 I'm so glad you're mine 🦦💕",
        "Bug Bug 🐞 you're my perfect bug buddy 🐛💛",
        "Krissy 🐝 you're my cozy little human burrito 🐼🌯",
        "Baby Bee 🐝 you're the best part of my life 🐥💛",
        "Stinky 🐨 you're my silly partner forever 🐸✨",
        "Bubba 🐻 you're my favorite thing in the entire world 🐾💛",
        "Bug Bug 🐞 you're my goofy little bug 🐛🌼",
        "Krissy 🐝 just wanted to say I adore you 🐥💛",
        "Baby Bee 🐝 you're my best thing ever 🦋🌸",
        "Stinky 🐼 you're the cutest chaos gremlin 🐒✨",
        "Bubba 🐻 you're my favorite cuddly human 🦊🛏️",
        "Bug Bug 🐞 you're my tiny little sunshine 🐛☀️",
        "Krissy 🐝 you make my life endlessly better 🐻💛",
        "Baby Bee 🐝 I'd always pick you 🐥🌼",
        "Stinky 🐨 you're my silly forever 🐸💛",
        "Bubba 🐻 you're my happiest hello and hardest goodbye 🐾💖",
        "Bug Bug 🐞 you're my best bug 🐛💛"
    ]
    
    try:
        message = prepend_message + random.choice(messages)
        
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
