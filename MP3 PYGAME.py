from pygame import mixer
mixer.init()
mixer.music.load('EXE21.mp3')
mixer.music.play()
x = input('Digite algo para parar a música...')
