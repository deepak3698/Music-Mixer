import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

print("hello deepak--It is an Music Mixer App")

def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('yaara_song.mp3')
    # First_Part #1
    start = 1000
    finish = 5000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1s.mp3", format="mp3")
# First_Part #2
    start = 5000
    finish = 10000
    audioProcessed = audio[start:finish]
    audioProcessed.export("2s.mp3", format="mp3")
# First_Part #3
    start = 10000
    finish = 13000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3s.mp3", format="mp3")
# First_Part #4
    start = 13000
    finish = 17000
    audioProcessed = audio[start:finish]
    audioProcessed.export("4s.mp3", format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    for index,item in df.iterrows():
        # 2 - Generate Name
        textToSpeech(item['name'], '1d.mp3')

        # 4 - Generate Bs Kya
        textToSpeech(item['cp1'], '2d.mp3')

#         # 6 - Generate Badhiya
        textToSpeech(item['cp2'], '3d.mp3')

        dt1=["1s","1d","2s","2d","3s","3d","4s"]
        audios = [f"{i}.mp3" for i in dt1]

        announcement = mergeAudios(audios)
        announcement.export("final.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Voices...")
    generateSkeleton()
    print("Final Song...")
    generateAnnouncement("myVoice.xlsx")
    


