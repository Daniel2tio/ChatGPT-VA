import openai #allows the access to gpt api
import pyttsx3 #allows the transcribing of text to speech
import speech_recognition as sr #allows the transcribing of speech to text
import time 

#Setting the OpenAI API Key

openai.api_key = ""

#Setting the text to speech recognition
engine = pyttsx3.init()

"""The following function transcribes voice commands into text using the speech recognition engine"""
def audio_transcript(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source: #the audio file is set as the source file
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio) #we use google's api method however, others such as Amazon, Bing, etc can be used
    except:
        print("Unkown errors to be skipped") #if a speech error is encountered, the function will skip it

"""The following function generates responses from the openai API"""

def gpt_response(prompt):
    response = openai.Completion.create( #the following parameters are based from the OpenAI API reference https://platform.openai.com/docs/api-reference/completions/create
        engine="text-davinci-003"
        prompt=prompt,
        max_tokens=4000, #the limit of characters from a response given (4000 is the max for the gpt-3 engine)
        n=1,
        stop=None,
        temperature = 0.6, #this is the randomness/creativity controller of the engine
    )
    return response["choices"][0]["text"] #the response is returned