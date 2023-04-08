import asyncio
import whisper 
import speech_recognition as sr #for capturing audio
from EdgeGPT import Chatbot, ConversationStyle
import re #deals with unwanted text formatting
import boto3
import pydub
from pydub import playback
#Function to recognize wake up word
recognizer = sr.Recognizer() 
wake_word = "bing"

def get_wake_word(phrase):
    if wake_word in phrase.lower():
        return wake_word
    else:
        return None
    
#Function to output text into speech using Amazon's polly synthesizer
def speech_synth(text, output_filename):
    polly = boto3.client("polly", region_name="eu-west-2")
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat = 'mp3',
        VoiceId = 'Joey',
        Engine='neural' #most natural sounding voice
    )

#Function that plays the synthesized audio
def play(file):
    sound = pydub.AudioSegment.from_file(file, format='mp3')
    playback.play(sound)

#Function that retrieves responses from Bing AI
async def main():
    while True:
        with sr.Microphone() as source: #accesses the device's microphone to record audio
            recognizer.adjust_for_ambient_noise(source)
            print(f"Waiting for wake words 'ok bing' or 'ok chat'...")
            while True:
                audio = recognizer.listen(source)#records the audio
                try:
                    with open ("audio.wav", "wb") as f:
                        f.write(audio.get_wav_data())
                    #using the preloaded "tiny" model
                    model = whisper.load_model("tiny")
                    result = model.transcribe("audio.wav")
                    phrase = result["text"]
                    print(f"You said: {phrase}")

                    wake_word = get_wake_word(phrase)
                    if wake_word is not None:
                        break
                    else:
                        print("Not a wake word. Try again.")
                except Exception as e:
                    print("Say that again please".format(e)) #handles an error using exception if the try block fails

            print("Tell me a prompt...")
            speech_synth("What can I help you with?", "response.mp3")
            play("response.mp3")
            audio = recognizer.listen(source)


        bot = Chatbot(cookiePath='cookies.json')
        response = await bot.ask(prompt=input("Ask Bing AI a question..."), conversation_style=ConversationStyle.creative)
        # Select only the bot response from the response dictionary
        for message in response["item"]["messages"]:
            if message["author"] == "bot":
                bot_response = message["text"]
        #Removes citations from responses
        bot_response = re.sub('\[\^\d+\^\]', '', bot_response)
        print("Bot's response:", bot_response)
        speech_synth(bot_response, 'response.mp3')
        play('response.mp3')
        await bot.close()

#Function that responds to an audio wake up word using whisper

if __name__ == '__main__':
    asyncio.run(main())

    