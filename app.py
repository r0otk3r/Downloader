#!/usr/bin/env python3

from flask import Flask, request, send_file, render_template_string
import os
import yt_dlp
import zipfile

app = Flask(__name__)

# Ensure the downloads folder exists
if not os.path.exists('downloads'):
    os.makedirs('downloads')

# Minimal HTML form with platform selection
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>📥 Video Downloader</title>
</head>
<body>
    <h2>🎬 Video / Playlist Downloader</h2>
    <form method="POST" action="/download">
        <label>Enter Video or Playlist URL:</label><br>
        <input type="text" name="url" size="60" required><br><br>

        <label>Select Platform:</label><br>
        <select name="platform">
            <option value="youtube">YouTube</option>
            <option value="vimeo">Vimeo</option>
            <option value="tiktok">TikTok</option>
            <option value="facebook">Facebook</option>
            <option value="soundcloud">SoundCloud</option>
            <option value="dailymotion">Dailymotion</option>
            <option value="instagram">Instagram</option>
            <option value="twitch">Twitch</option>
            <option value="twitter">Twitter / X</option>
            <option value="other">Other</option>
        </select><br><br>

        <button type="submit">Download</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')
    platform = request.form.get('platform')

    if not url:
        return "Missing URL."

    # Configure yt-dlp options
    ydl_opts = {
        'outtmpl': 'downloads/%(playlist)s/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': False
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            # Handle playlists
            if 'entries' in info:
                playlist_path = os.path.join('downloads', info['title'])
                zip_file = f'{playlist_path}.zip'

                with zipfile.ZipFile(zip_file, 'w') as zipf:
                    for root, dirs, files in os.walk(playlist_path):
                        for file in files:
                            filepath = os.path.join(root, file)
                            arcname = os.path.relpath(filepath, playlist_path)
                            zipf.write(filepath, arcname)

                return send_file(zip_file, as_attachment=True)

            # Single video
            file_path = ydl.prepare_filename(info)
            return send_file(file_path, as_attachment=True)

    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
