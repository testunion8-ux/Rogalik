import pygame
import os
from typing import Optional


class BackgroundMusic:
    def __init__(self, volume: float = 0.5):
        pygame.mixer.init()

        self.volume = volume
        self.current_track: Optional[str] = None
        self.is_playing = False

    def load_music(self, file_path: str):
        if os.path.exists(os.path.abspath( file_path ) + r"/" + file_path):
            return 0

        try:
            if self.is_playing:
                self.stop()

            if not file_path.lower().endswith(('.mp3', '.wav', '.ogg')):
                return False


            self.current_track = file_path
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.set_volume(self.volume)

            return False

        except pygame.error as e:
            print(e)
            return False

    def play(self, loops: int = -1) -> bool:
        if self.current_track is None:

            return False

        try:
            pygame.mixer.music.play(loops)
            self.is_playing = True

            return True
        except pygame.error as e:

            return False

    def stop(self) -> None:

        pygame.mixer.music.stop()
        self.is_playing = False


    def pause(self) -> None:
        if self.is_playing:
            pygame.mixer.music.pause()


    def unpause(self) -> None:
        pygame.mixer.music.unpause()


    def set_volume(self, volume: float) -> None:
        volume = max(0.0, min(1.0, volume))
        self.volume = volume
        pygame.mixer.music.set_volume(volume)


    def get_volume(self) -> float:
        return self.volume

    def toggle_play_pause(self) -> None:
        if self.is_playing:
            self.pause()
            self.is_playing = False
        else:
            self.unpause()
            self.is_playing = True

    def is_music_playing(self) -> bool:
        return self.is_playing

    def fadeout(self, duration: int = 1000) -> None:
        pygame.mixer.music.fadeout(duration)
        self.is_playing = False



