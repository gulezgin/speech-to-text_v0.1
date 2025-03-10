import speech_recognition as sr
from pydub import AudioSegment
from tkinter import Tk, filedialog, Button, Label

# Ses dosyasını seçme
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Ses Dosyaları", "*.wav;*.mp3;*.m4a")])
    if file_path:
        convert_to_wav(file_path)

# Ses dosyasını WAV'e dönüştürme (SpeechRecognition sadece WAV destekler)
def convert_to_wav(file_path):
    if file_path.endswith(".mp3"):
        sound = AudioSegment.from_mp3(file_path)
        file_path = file_path.replace(".mp3", ".wav")
        sound.export(file_path, format="wav")
    elif file_path.endswith(".m4a"):
        sound = AudioSegment.from_file(file_path, format="m4a")
        file_path = file_path.replace(".m4a", ".wav")
        sound.export(file_path, format="wav")
    recognize_audio(file_path)

# Ses dosyasını metne çevirme
def recognize_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        print("Ses dosyası okunuyor...")
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio, language="tr-TR")
            print("Çözümlenen Metin:")
            print(text)
            with open("konusma_metni.txt", "w", encoding="utf-8") as f:
                f.write(text)
            Label(root, text="Metin başarıyla kaydedildi!", fg="green").pack()
        except Exception as e:
            print("Hata:", e)
            Label(root, text="Ses dosyası çözümlenemedi.", fg="red").pack()

# Arayüz Oluşturma
root = Tk()
root.title("Ses Kaydı Çevirici")
root.geometry("400x200")
Label(root, text="Ses dosyasını seçin").pack(pady=20)
Button(root, text="Dosya Seç", command=select_file).pack()

root.mainloop()

#pip install speechrecognition pydub googletrans tkinter
