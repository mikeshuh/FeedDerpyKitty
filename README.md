# FeedDerpyKitty: Your Personal Message Service 💕
Sending scheduled affectionate messages to Derpy Kitty (my girlfriend) for sustenance.
<div align="center">
  <img src="https://64.media.tumblr.com/d6dfa59fa507e1de71f610b2551e1dce/53a0528a42b8151f-6f/s540x810/313f2d2292dba7be3f3eb6723f668eead64cf57e.gifv" width="150" height="150" alt="Derpy Kitty">
</div>

Hey! 

So I built you something - an automated text service that sends you messages throughout the day. It's basically a way for me to check in with you regularly, even when I'm busy.

## What This Is ✨

An automated messaging system that sends you sweet messages every hour from 6 AM to 11 PM. It's a reminder system that I'm thinking about you, powered by cloud technology.

## How It Works 🤖

Built using some cool technology:
- **AWS Lambda**: A serverless function that runs the messaging code
- **Twilio**: SMS service for message delivery
- **EventBridge**: Scheduler that triggers messages every hour
- **15 different messages**: Rotates through various messages

Sample messages include:
- "Hey! Just wanted to remind you that I love you ❤️"
- "Hope you're having a great day! 💕"
- "Thinking of you 😊"
- Plus many other variations

## Your Controls 🎛️

You have complete control over this service:

**To Stop Messages:** Text `STOP` to the number
- System automatically pauses and sends confirmation
- Useful for meetings, sleep, or when you need a break

**To Start Again:** Text `START` to the same number
- Messages resume with a confirmation
- Reactivates the service whenever you want

**To Check Status:** Text `STATUS` to see if messages are currently active

## Why I Built This 💝

Our schedules get pretty hectic, and I don't always text as consistently as I'd like. This system ensures you get regular check-ins from me, even during busy periods.

This is just a consistent way to let you know I'm thinking about you throughout the day.

## The Technical Stuff (For the Curious) 🛠️

If you're wondering about the behind-the-scenes magic:

- **Cost**: About $6-7 per month
- **Reliability**: Runs on Amazon's cloud, so it's super reliable
- **Compliance**: Fully registered with all the telecom regulations (A2P 10DLC compliant)
- **Privacy**: Only you and I have access to this system
- **Delivery**: Messages go through professional SMS routes for guaranteed delivery

The whole system is written in Python and deployed to AWS. Here's what happens:
1. EventBridge triggers the function every hour
2. Lambda function checks if messages are enabled
3. Randomly selects a message from the pool
4. Sends via Twilio's SMS API

Pretty straightforward, but it gets the job done reliably.

## A Little Note 💌

Hope these messages brighten your day, especially during stressful times. And if they ever get annoying, just text STOP - no worries at all!

## Questions? 🤔

If anything stops working, or if you want me to modify the messages, timing, or any other features - just let me know! It's all configurable.

If you're curious about the technical implementation, I'm happy to walk through how it all works.

---

*Built with ❤️ and AWS Lambda*

*P.S. - Yes, I built cloud infrastructure just to send you regular texts. Seemed like a good use of my programming skills.*
