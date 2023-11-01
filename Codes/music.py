import pygame

# Initialize the pygame mixer
pygame.mixer.init()

# Load the MP3 file
mp3_file = "output.mp3"
pygame.mixer.music.load(mp3_file)

# Play the MP3 file
pygame.mixer.music.play()

# Keep the program running while the audio plays
while pygame.mixer.music.get_busy():
    pass
