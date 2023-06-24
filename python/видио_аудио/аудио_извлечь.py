import moviepy.editor as mp
#  из видио достать аудио
clip = mp.VideoFileClip(r'C:\stardiatka_proekt\нарадила.mp4')
clip.audio.write_audiofile(r'wer.mp3')