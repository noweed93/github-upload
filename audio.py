import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import commander

running = True

def say(text):

    subprocess.call('PowerShell -Command "Add-Type –AssemblyName System.Speech; ' +
                    '(New-Object System.Speech.Synthesis.SpeechSynthesizer).' +
                    "Speak('" + text + "'" + ');"', shell = True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format= pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()
cmd = commander()

def initspeech():
    print("listening")
    play_audio('./audio/Game-Show-Buzzer.wav')
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)

    play_audio('./audio/Game-Show-Buzzer.wav')

    command = ''

    try:
        command = r.recognize_google(audio)
    except:
        print("couldnt understand you")

    print("your command", command)
    global running
    if command in ['exit', 'quit', 'bye'] :
        running = False

    cmd.discover(command)


while running == True:
    initspeech()





'''import pyglet

file = pyglet.resource.media("audio/that-was-quick.mp3")

file.play()

pyglet.app.run()

'''