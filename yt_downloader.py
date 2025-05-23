import streamlit as st
from youtubesearchpython import VideosSearch
from pathlib import Path
import yt_dlp
import random
import os
import string
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

st.set_page_config(page_title="YouTube MP4 Downloader", layout="wide")
st.title("🎬 YouTube Video Downloader with yt-dlp")

if "query" not in st.session_state:
    st.session_state.query = ""
if "refresh_key" not in st.session_state:
    st.session_state.refresh_key = 0

query_input = st.text_input("Search a video or paste URL", value=st.session_state.query)
limit = st.slider("Number of results", 1, 5, 10)
download_folder = st.text_input("Download folder", str(Path.home() / "Videos"))

# Save updated query to session state
if query_input:
    st.session_state.query = query_input

def get_random_query_seed():
    return ''.join(random.choices(string.ascii_lowercase, k=3))

if st.session_state.query:
    # Use refresh_key to randomize request
    videos_search = VideosSearch(st.session_state.query, limit=limit)
    results = videos_search.result()['result']

    for vid in results:
        st.markdown("---")
        col1, col2 = st.columns([1, 3])

        with col1:
            st.image(vid['thumbnails'][0]['url'], width=200)

        with col2:
            st.subheader(vid['title'])
            st.write(f"📺 Duration: {vid['duration']} | 👁 Views: {vid['viewCount']['short']}")
            st.write(f"[🔗 Watch on YouTube]({vid['link']})")

            if st.button(f"⬇️ Download: {vid['title']}", key=vid['id']):
                try:
                    if not os.path.isdir(download_folder):
                        st.error("⚠️ Invalid folder path")
                        continue

                    ydl_opts = {
                        'outtmpl': str(Path(download_folder) / f'%(title)s-{timestamp}.%(ext)s'),
                        'format': 'best[ext=mp4]/best',
                        'merge_output_format': 'mp4',
                        'quiet': True,
                        'verbose': True, 
                        'noplaylist': True,
                        'overwrites': True,
                        'ignore_no_formats_error': True
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([vid['link']])
                    st.success(f"✅ Downloaded to: {download_folder}")
                except Exception as e:
                    st.error(f"❌ Failed to download: {e}")

if st.button("🔄 Do not like the results?"):
    st.session_state.refresh_key += 1