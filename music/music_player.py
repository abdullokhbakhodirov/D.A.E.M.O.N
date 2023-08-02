import os
import pygame

def play_music_from_folder(folder_path):
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Get a list of all music files in the folder
    music_files = [file for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav'))]

    if not music_files:
        print("No music files found in the folder.")
        return False

    try:
        # Iterate through the music files and play them one by one
        for file in music_files:
            music_path = os.path.join(folder_path, file)
            pygame.mixer.music.load(music_path)
            print(f"Playing: {file}")
            pygame.mixer.music.play()

            # Wait for the music to finish playing before moving to the next file
            while pygame.mixer.music.get_busy():
                continue

        print("All music files have been played.")
    except KeyboardInterrupt:
        print("\nMusic playback stopped by the user.")

    # Clean up Pygame resources
    pygame.mixer.quit()


# ===============================================================================================


import os
import tkinter as tk
from tkinter import filedialog
import pygame

def play_music_from_file_dialog():
    # Initialize Tkinter
    root = tk.Tk()
    root.withdraw()

    # Open file dialog to select a music file
    file_path = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3;*.wav")])

    if not file_path:
        print("No music file selected.")
        return

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Get a list of all music files in the folder of the selected file
    folder_path = os.path.dirname(file_path)
    music_files = [file for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav'))]

    if not music_files:
        print("No music files found in the folder.")
        return

    try:
        # Remove the chosen file from the list
        music_files.remove(os.path.basename(file_path))

        # Load and play the selected music file
        pygame.mixer.music.load(file_path)
        print(f"Playing: {file_path}")
        pygame.mixer.music.play()

        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            continue

        # Continue playing other music files in the folder
        while music_files:
            next_file = music_files.pop(0)
            next_file_path = os.path.join(folder_path, next_file)

            pygame.mixer.music.load(next_file_path)
            print(f"Playing: {next_file_path}")
            pygame.mixer.music.play()

            # Wait for the music to finish playing
            while pygame.mixer.music.get_busy():
                continue

        print("All music files in the folder have been played.")
    except KeyboardInterrupt:
        print("\nMusic playback stopped by the user.")

    # Clean up Pygame resources
    pygame.mixer.quit()


# ====================================================================================================================



