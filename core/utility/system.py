import os
import platform

class System:

    @staticmethod
    def Run(cmd: str):
        os.system(cmd)

    @staticmethod
    def SetTitle(title: str):
        print(platform.system())
        if platform.system() == "Windows":
            System.Run(f'title {title}')

    @staticmethod
    def Pause():
        if platform.system() == "Windows":
            System.Run('pause')

    @staticmethod
    def Sleep(secs: float):
        from time import sleep
        return sleep(secs)

