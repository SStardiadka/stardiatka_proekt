from moviepy.editor import *

clip = (
    #     (
    VideoFileClip(r"C:\Users\user\Desktop\Матросская - У матросов нет вопросов.mp4")
    #     ).subclip((0, 01.45), (0, 01.50))
    #     .resize(0.5)
)

clip.write_gif("use_your_head.gif")
