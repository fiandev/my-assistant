import pyttsx3, speech_recognition, subprocess, gtts, playaudio
from application.constants.paths import ROOT_PATH
from application.utilities.input_parser import input_parser
from application.helpers.path import find_exe_files, path_exist
from application.helpers.string import create_slug
from application.controllers.ChromeController import ChromeController
from application.libraries.State import State

class Bot (State):
    def __init__(self) -> None:
        super().__init__()
        
        self.microPhone = speech_recognition.Recognizer()
        self.ttsEngine = pyttsx3.init()
        self.gttsEngine = gtts
    
    def speak (self, text: str) -> None:
        self.ttsEngine.say(text)
        self.ttsEngine.runAndWait()
    
    def gtts_speak (self, text: str) -> None:
        cacheAudioPath = f"{ ROOT_PATH }/assets/caches/{ create_slug(text) }.mp3"
        
        if not path_exist(cacheAudioPath):
            tts = self.gttsEngine.gTTS(text, lang=self.language)
            tts.save(cacheAudioPath)
        
        playaudio.playaudio(cacheAudioPath)
    
    def listen (self) -> None:
        with speech_recognition.Microphone() as source:
            print("Adjusting noise...")
            self.microPhone.adjust_for_ambient_noise(source, duration=1)
            print("microphone on")
            recorded_audio = self.microPhone.listen(source, timeout=5)
            print("microphone off")
            
            prompt = self.microPhone.recognize_google(recorded_audio, language=self.language)
            actions = input_parser(prompt)
            
            for action in actions:
                self.run(*action)
        
    def run (self, action_name: str, prompt: str, objective: str) -> None:
        if action_name == "open.application":
            """
            try open any external application first
            """
            try:
                exeFiles = map(lambda x: x.lower(),find_exe_files("C:/Program Files (x86)/**/*.exe"))
                
                for file in exeFiles:
                    fileName = file.split('\\').pop()
                    
                    if file.find(objective) > -1:
                        print (f"found { file }")
                        self.gtts_speak(f"membuka aplikasi { objective }")
                        subprocess.Popen(file)
                        break
                else:
                    self.gtts_speak(f"maaf aplikasi { objective } tidak ditemukan")
            except Exception as err:
                raise err
                pass
            finally:
                pass