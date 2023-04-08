import openai #allows the access to gpt api
import pyttsx3 #allows the transcribing of text to speech
import speech_recognition as sr #allows the transcribing of speech to text

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
        return recognizer.recognize_google(audio) #we use google's api method however, others such as Amazon, Bing, etc can be used (use snowboy)
    except:
        print("Unkown errors to be skipped") #if a speech error is encountered, the function will skip it

"""The following function generates responses from the openai API"""

def gpt_response(prompt):
    response = openai.Completion.create(#the following parameters are based from the OpenAI API reference https://platform.openai.com/docs/api-reference/completions/create
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=4000, #the limit of characters from a response given (4000 is the max for the gpt-3 engine)
        n=1,
        stop=None,
        temperature = 0.6, #this is the randomness/creativity controller of the engine
    )
    return response["choices"][0]["text"] #the response is returned

"""The following function lets the user speak into the VA"""

def speech_text(text): #the function takes a text argument into speech using pyttsx3
    engine.say(text)#specifies the text to be spoken
    engine.runAndWait() #plays the speech

"""The following function controls the logic of how the script is executed"""

def main():
    while True: #the loop will run until it is forced to exit and allowing it to listen for a wake up prompt 
        print("Say 'Genius' to start recording your question...") #instructs the user to prompt for recording
        with sr.Microphone() as source: #accesses the device's microphone to record audio
            recognizer = sr.Recognizer() 
            audio = recognizer.listen(source)#records the audio
            try:
                transcription = recognizer.recognize_google(audio) #transcribes the recorded audio into text using google's method
                if transcription.lower() == "genius": #checks if the transcribed audio matches the wakeup prompt
                    #if the prompt word matches, we can continue recording audio
                    filename = "input.wav" #saves the audio to a waveform audio file
                    print("What is your question?")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 0.8 #provides a brief pause
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None) #parameters that control how long to allow listening 
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                
                    # Transcribing the audio to text using our function
                    text = audio_transcript(filename) #the text variable will hold the transcribed text
                    if text:
                        print(f"You said: {text}")

                        #Generating response from GPT-3
                        response = gpt_response(text)
                        print(f"Sensei says: {response}")

                        #Outputting response using text to speech
                        speech_text(response)
            except Exception as e:
                print("Say that again please".format(e)) #handles an error using exception if the try block fails

if __name__ == "__main__":
    main()
