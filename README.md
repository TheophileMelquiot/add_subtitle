# add_subtitle


using the whisper model, you, first, do speech recognition from the video you want to add subtitles too, add the language of the video you want to subtitle for faster and better result. The whisper function will write, create a txt file with the sentences and the timing of the sentences. 

And after you use the ffmpeg package to add the subtitles to the video, you can choose the size, placement even the policy of the words you want to implment.

You can use, for example, a tokeniser model to modify the txt to seprate sentences to sentences for the subtitles, cause for now, the subtitles will show the full line that the seapker is saying
