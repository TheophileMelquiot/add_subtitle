import whisper
from nltk.tokenize import sent_tokenize
import subprocess
import os 

def format_time(seconds):
    millisec = int((seconds - int(seconds)) * 1000)
    total_seconds = int(seconds)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{millisec:03}"

def generate_subtitles(audio_path, output_srt="subtitles2.srt", model_size="base.en"):

    model = whisper.load_model(model_size)
    
    result = model.transcribe(audio_path, language="en", word_timestamps=True)
    
    all_words = []
    for segment in result["segments"]:
        all_words.extend(segment["words"])
    
    full_text = result["text"]
    sentences = sent_tokenize(full_text)
    
    subtitles = []
    current_word = 0
    
    for sentence in sentences:
        words_in_sentence = []
        sentence_words = sentence.split()
        
        while current_word < len(all_words):
            current_word_text = all_words[current_word]["word"].strip()
            
            if current_word_text == sentence_words[len(words_in_sentence)]:
                words_in_sentence.append(all_words[current_word])
                
                if len(words_in_sentence) == len(sentence_words):
                    start = words_in_sentence[0]["start"]
                    end = words_in_sentence[-1]["end"]
                    subtitles.append({
                        "text": sentence,
                        "start": start,
                        "end": end
                    })
                    current_word += 1
                    break
            current_word += 1
    
    with open(output_srt, "w") as srt_file:
        for i, sub in enumerate(subtitles, start=1):
            start_time = format_time(sub["start"])
            end_time = format_time(sub["end"])
            srt_file.write(f"{i}\n")
            srt_file.write(f"{start_time} --> {end_time}\n")
            srt_file.write(f"{sub['text']}\n\n")

def add_the_subtitle(directory_path,subtitles_path,video_name):
        os.chdir(directory_path)
        command = f'ffmpeg -i {video_name} -vf "subtitles={subtitles_path}:force_style=\'FontSize=15\'" output_with_subtitles.mp4'
 
        subprocess.run(command, shell=True, check=True)





Audio_file_to_modify ="segment_001.mp4"


if __name__ == "__main__":
   generate_subtitles(Audio_file_to_modify)  # Remplacez par votre fichier audio
   add_the_subtitle("C:/Users/","subtitles.srt",Audio_file_to_modify)  # Remplacez par votre fichier audio


