import asyncio
from EdgeGPT import Chatbot, ConversationStyle

async def main():
    bot = Chatbot(cookiePath='cookies.json')
    print(await bot.ask(prompt="Hello World", conversation_style=ConversationStyle.creative))
    await bot.close()

if __name__ == '__main__':
    asyncio.run(main())

    