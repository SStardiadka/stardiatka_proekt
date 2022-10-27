from moviepy.editor import *

clip = (VideoFileClip(r'C:\Users\user\Desktop\Видеоряд 2.avi'))
        #  .subclip((1,22.65),(1,23.2))
        # .resize(0.3)))
        
clip.write_gif("use_your_head.gif")