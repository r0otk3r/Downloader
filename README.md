
# Video & Playlist Downloader (Flask + yt-dlp)

A lightweight web application using **Flask** and **yt-dlp** that allows you to download videos or entire playlists from YouTube and other supported platforms.

- No frontend frameworks  
- Simple HTML interface  
- Automatic playlist zipping

---

##  Features

- Download single videos or entire playlists
- Playlists are zipped for easy download
- Supports multiple platforms (YouTube, TikTok, Vimeo, SoundCloud, etc.)
- Minimal dependencies, no CSS/JS
- Works via browser or local network

---

## Requirements

- Python 3.8+
- `ffmpeg` (for best quality merging)
- `pip` packages:
```bash
pip install flask yt-dlp
```
## Supported Platforms

yt-dlp supports hundreds of platforms automatically. Examples:

-    YouTube

-    Vimeo

-    TikTok

-    SoundCloud

-    Facebook

-    Dailymotion

-    Twitch

-    Instagram

-    Twitter / X

For the full list:

👉 https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

## How to Run
```bash
python3 app.py
```
#### Then open your browser and go to:
```bash
http://localhost:5000
```
## Usage

1.    Enter the full video or playlist URL.

2.    Select the platform from the dropdown (optional).

3.   Click "Download".

4.   Wait for download and file will automatically start downloading (single video) or be zipped (playlist).
 
 ## Project Structure
 ```bash
 .
├── app.py              # Main Flask application
├── downloads/          # Folder where videos/playlists are stored
└── README.md
```

<img width="1366" height="357" alt="1" src="https://github.com/user-attachments/assets/bfc66e25-a684-4477-a002-9ce63ab4b9e6" />

----

<img width="1351" height="478" alt="2" src="https://github.com/user-attachments/assets/3206366f-c6b7-4144-bf4d-dc358bc0792a" />



## ⚠️ Notes

-    The platform selector is optional  yt-dlp detects platform automatically from the URL.

-    You can later add format selectors (e.g., MP3, 720p) or platform-specific logic (e.g., TikTok login).

-    This uses Flask's development server — for production, use Gunicorn or uWSGI.

## Production Usage

Install Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```
## License

MIT License

---

## Official Channels

- [YouTube @rootctf](https://www.youtube.com/@rootctf)
- [X @r0otk3r](https://x.com/r0otk3r)
