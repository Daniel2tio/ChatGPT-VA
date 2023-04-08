import asyncio
from EdgeGPT import Chatbot, ConversationStyle
import re #deals with unwanted text formatting

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

if __name__ == '__main__':
    asyncio.run(main())

    