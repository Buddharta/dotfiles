import os
from libqtile.command import lazy
# from libqtile.command_client import InteractiveCommandClient


class Functions:

    @lazy.function
    def window_to_prev_group(qtile):
        if qtile.currentWindow is not None:
            i = qtile.groups.index(qtile.currentGroup)
            qtile.currentWindow.togroup(qtile.groups[i - 1].name)
    
    @lazy.function
    def window_to_next_group(qtile):
        if qtile.currentWindow is not None:
            i = qtile.groups.index(qtile.currentGroup)
            qtile.currentWindow.togroup(qtile.groups[i + 1].name)
    
##### KILL ALL WINDOWS #####
    
    @staticmethod
    def kill_all_windows():
        @lazy.function
        def __inner(qtile):
            for window in qtile.current_group.windows:
                window.kill()
    
            return __inner
    
    @staticmethod
    def kill_all_windows_minus_current():
        @lazy.function
        def __inner(qtile):
            for window in qtile.current_group.windows:
                if window != qtile.current_window:
                    window.kill()
    
            return __inner


class PWA:
    def __init__(self):
        pass

    @staticmethod
    def notion():
        return "firefox --profile-directory=Default --app=https://notion.so"

    @staticmethod
    def music():
        return "firefox --profile-directory=Default --app=https://music.youtube.com/"

    @staticmethod
    def spotify():
        return "firefox --profile-directory=Default --app=https://open.spotify.com/"

    @staticmethod
    def youtube():
        return "firefox --user-data-dir=Default --app=https://www.youtube.com"

    @staticmethod
    def calendar():
        return "firefox --profile-directory=Default --app=https://calendar.google.com/calendar/"

    @staticmethod
    def habitica():
        return "firefox --profile-directory=Default --app=https://habitica.com/"


if __name__ == "__main__":
    print("This is an utilities module")
