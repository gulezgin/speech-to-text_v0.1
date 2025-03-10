# Ses Kaydı Metin Dönüştürücü / Speech to Text Converter

## 🇹🇷 Türkçe

Ses Kaydı Metin Dönüştürücü

Bu uygulama, ses kayıtlarını metne dönüştürmek için geliştirilmiş kullanıcı dostu bir araçtır. Google'ın güçlü konuşma tanıma teknolojisini kullanarak WAV, MP3 ve M4A formatlarındaki ses dosyalarını Türkçe metne dönüştürür.

Temel Özellikler:
- Çoklu ses formatı desteği (WAV, MP3, M4A)
- Türkçe dil desteği
- Basit ve kullanıcı dostu arayüz
- Otomatik metin dosyası oluşturma
- Hızlı ve doğru ses tanıma

Kullanım Alanları:
- Toplantı kayıtlarının yazıya dökülmesi
- Sesli notların metne çevrilmesi
- Röportaj kayıtlarının deşifresi
- Sesli mesajların metne dönüştürülmesi
- Eğitim materyallerinin hazırlanması

Bu uygulama, özellikle ses kayıtlarını metin formatına dönüştürmek isteyen öğrenciler, gazeteciler, araştırmacılar ve profesyoneller için idealdir. 

### Proje Açıklaması
Bu proje, ses kayıtlarını (WAV, MP3, M4A formatlarında) metne dönüştüren basit bir Python uygulamasıdır. Google Speech Recognition API kullanarak Türkçe ses kayıtlarını yazıya çevirir ve sonucu bir metin dosyasına kaydeder.

### Özellikler
- WAV, MP3 ve M4A formatlarını destekler
- Türkçe dil desteği
- Kullanıcı dostu grafiksel arayüz
- Otomatik metin dosyası oluşturma
- Çoklu format desteği

### Gereksinimler
```bash
pip install speechrecognition pydub
```

Ayrıca sisteminizde FFmpeg kurulu olmalıdır. Windows için FFmpeg kurulumu:
1. [FFmpeg'i indirin](https://github.com/BtbN/FFmpeg-Builds/releases)
2. Zip dosyasını çıkartın
3. bin klasörünü C:\ffmpeg konumuna kopyalayın
4. Sistem ortam değişkenlerine C:\ffmpeg\bin yolunu ekleyin

### Kullanım
1. Uygulamayı başlatın:
```bash
python main.py
```
2. "Dosya Seç" butonuna tıklayın
3. Dönüştürmek istediğiniz ses dosyasını seçin
4. Dönüştürülen metin otomatik olarak konusma_metni.txt dosyasına kaydedilecektir

---

## 🇬🇧 English

### Project Description
This project is a simple Python application that converts audio recordings (in WAV, MP3, M4A formats) to text. It uses Google Speech Recognition API to transcribe Turkish audio recordings and saves the result to a text file.

### Features
- Supports WAV, MP3, and M4A formats
- Turkish language support
- User-friendly graphical interface
- Automatic text file generation
- Multiple format support

### Requirements
```bash
pip install speechrecognition pydub
```

You also need FFmpeg installed on your system. For Windows FFmpeg installation:
1. [Download FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases)
2. Extract the zip file
3. Copy the bin folder to C:\ffmpeg
4. Add C:\ffmpeg\bin to system environment variables

### Usage
1. Start the application:
```bash
python main.py
```
2. Click the "Select File" button
3. Choose the audio file you want to convert
4. The converted text will be automatically saved to konusma_metni.txt 