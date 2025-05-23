# 🎬 YouTube MP4 Downloader with Streamlit + yt-dlp

A sleek and interactive web app to search and download YouTube videos as MP4s using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) and [`Streamlit`](https://streamlit.io). Built for simplicity. Runs locally. No ads. No BS.

## 🚀 Features

- 🔍 Search YouTube videos using `youtubesearchpython`
- 🎞 View thumbnails, titles, duration, views, and video links
- ⬇️ Download the highest quality MP4 video to your chosen folder
- 🔄 “Refresh Results” button gives you new videos for the same query
- 🖥️ Cross-platform and super lightweight


## 🧠 Tech Stack

- [Streamlit](https://streamlit.io)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [YouTube Search Python](https://github.com/alexmercerind/youtube-search-python)

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/SuzanTurner/YouTube-Video-Downloader.git
cd YouTube-Video-Downloader
```

Create a virtual environment and activate it:

```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

```Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```
Run the app:

```
streamlit run app.py
```

## 📝 Usage
 - Enter a YouTube search query.
 - Choose how many results you want.
 - Select your download folder (defaults to Downloads).
 - Click ⬇️ Download to get your MP4 video.
 - Don’t like the results? Hit 🔄 to shuffle things up.

## 📁 Requirements
 - Python 3.8+
 - Internet connection (yeah bro)
 - Permissions to write in the chosen download folder
---
