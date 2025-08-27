import os
import argparse
import whisper
from tqdm import tqdm

def transcribe_audio(audio_path: str, model) -> str:
    """
    Transcribe a single audio file and write the output to a .txt file.
    Returns the path to the generated .txt file.
    """
    # Perform transcription
    result = model.transcribe(audio_path)
    text = result.get("text", "").strip()

    # Create output filename with .txt extension, same basename as audio
    base, _ = os.path.splitext(audio_path)
    output_path = f"{base}.txt"

    # Write the transcript
    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write(text)

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Batch transcribe multiple audio files to text with a progress bar"
    )
    parser.add_argument(
        "audio_files", nargs="+",
        help="Paths to one or more audio files (mp3, wav, m4a, etc.)"
    )
    parser.add_argument(
        "--model", choices=["small", "medium", "large"], default="medium",
        help="Size of the Whisper model to use"
    )
    args = parser.parse_args()

    # Validate and collect existing files
    audio_paths = []
    for path in args.audio_files:
        if os.path.isfile(path):
            audio_paths.append(path)
        else:
            print(f"Warning: file not found: {path}")

    if not audio_paths:
        print("No valid audio files provided. Exiting.")
        return

    # Load model once
    print(f"Loading Whisper '{args.model}' model...")
    model = whisper.load_model(args.model)

    # Process each file with a terminal progress bar
    for audio in tqdm(audio_paths, desc="Transcribing files", unit="file"):
        try:
            txt_path = transcribe_audio(audio, model)
            tqdm.write(f"✅ '{audio}' → '{txt_path}'")
        except Exception as e:
            tqdm.write(f"❌ Error on '{audio}': {e}")

if __name__ == "__main__":
    main()
