# AudioToTextAI
A tiny Python tool that batch-transcribes audio (mp3/wav/m4a/…) to plain text using OpenAI Whisper

Check the docs at https://github.com/openai/whisper

# Features
🎧 Batch transcribe multiple audio files via terminal

⚡ Loads Whisper model once for speed

📄 Outputs <audio_basename>.txt next to each file

📊 Neat progress bar with per-file success/error logs

🔁 Choose model size: small, medium, large

# Requirements
Python 3.9+

ffmpeg installed and on your PATH

macOS: brew install ffmpeg

Ubuntu/Debian: sudo apt-get install ffmpeg

Windows (PowerShell): winget install Gyan.FFmpeg (or use Chocolatey)

Python packages: openai-whisper, tqdm (and PyTorch for GPU)

# Install
<code> 
# clone your repo, then:
pip install -U openai-whisper tqdm
</code>
(Optional, for GPU) Install PyTorch following instructions from pytorch.org for your OS/CUDA

# Usage
<code>
# Single file
python transcribe.py path/to/audio.mp3
# Multiple files (shell globbing)
python transcribe.py path/to/folder/*.mp3
# Mix formats
python transcribe.py foo.mp3 bar.wav baz.m4a
# Choose model size (default: medium)
python transcribe.py --model small foo.mp3
python transcribe.py --model large foo.mp3 bar.wav
</code>
Output: for each input like meeting.mp3, you’ll get meeting.txt in the same directory containing the transcript.

# In short... How to:
- Create a folder and place the audio file inside it.
- Open CMD (Command Prompt) and locate the folder you created earlier.
- Type “pybatch_transcribe.py” and press Enter.
At the end of the process (you can check in the task manager to see if it is working based on CPU usage), a .txt file of the audio will be created.
<img width="612" height="292" alt="Screenshot 2025-08-27 212235" src="https://github.com/user-attachments/assets/8defd3ec-4794-4271-b992-76ff661d5393" />

# Notes
Larger models (large) are more accurate but need more RAM/VRAM and time.
If shell globbing (*.mp3) doesn’t expand on your system, use PowerShell or list files explicitly.
Language is auto-detected by Whisper unless you customize the code for a fixed language.
