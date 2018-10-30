import os
import time
import vlc



import pyglet
song = pyglet.media.load('/home/pi/Downloads/analog-watch-alarm.mp3')
song.play()
pyglet.app.run()

#import pygame
#pygame.init()
#song = pygame.mixer.Sound('cvlc /home/pi/Downloads/analog-watch-alarm.mp3')
#clock = pygame.time.Clock()
#song.play()
#while True:
#    clock.tick(2)
#pygame.quit()

#player = vlc.MediaPlayer("/home/pi/Downloads/analog-watch-alarm.mp3")
#player.play()
#time.sleep(2)
#player.stop

#os.startfile(r'/home/pi/Downloads/analog-watch-alarm.mp3')
#os.system('vlc /home/pi/Downloads/analog-watch-alarm.mp3')
#time.sleep(2)
#os.system.close('cvlc /home/pi/Downloads/analog-watch-alarm.mp3')

#os.system('cvlc /home/pi/Downloads/alarm_song.mp3' )


#while True:
#	os.system('timeout {} cvlc /home/pi/Downloads/alarm_song.mp3'.format(x) )

            

#if button is not pressed, then play the song
#else button is pressed then set up timeout for 2ms.

	
#os.system('timeout {} cvlc /home/pi/Downloads/alarm_song.mp3'.format(x) )


#with os.system('cvlc /home/pi/Downloads/alarm_song.mp3' ) as qq:
#	time.sleep(2)
#	qq.close()

#os.system('cvlc /home/pi/Downloads/alarm_song.mp3' )
#time.sleep(2)
#os.system.close('/home/pi/Downloads/alarm_song.mp3')


#pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load(file_song)
#print("song loaded {}".format(file_song))
#pygame.mixer.music.play(loops=-1, start=0.0)

#if input_state == False:
#	pygame.mixer.music.get_busy()
#else:
#	pygame.mixer.music.stop()
	

#while pygame.mixer.music.get_busy():
#	if input_state == False:
#		break
#	pygame.mixer.music.stop()