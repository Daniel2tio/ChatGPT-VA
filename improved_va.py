import asyncio
import whisper 
import speech_recognition as sr #for capturing audio
from EdgeGPT import Chatbot, ConversationStyle
import re #deals with unwanted text formatting

#Creating the wake word
recognizer = sr.Recognizer() 
wake_word = "bing"

def get_wake_word(phrase):
    if wake_word in phrase.lower():
        return wake_word
    else:
        return None

#Function that retrieves responses from Bing AI
async def main():
    while True:
        bot = Chatbot(cookiePath='cookies.json')
        response = await bot.ask(prompt=input("Ask Bing AI a question..."), conversation_style=ConversationStyle.creative)
        # Select only the bot response from the response dictionary
        for message in response["item"]["messages"]:
            if message["author"] == "bot":
                bot_response = message["text"]
        #Removes citations from responses
        bot_response = re.sub('\[\^\d+\^\]', '', bot_response)
        print("Bot's response:", bot_response)
        await bot.close()

#Function that responds to an audio wake up word using whisper

if __name__ == '__main__':
    asyncio.run(main())

    