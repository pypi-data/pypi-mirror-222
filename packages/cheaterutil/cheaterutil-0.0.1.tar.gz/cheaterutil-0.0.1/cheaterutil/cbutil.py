"""Main module for cheaterutil"""

"""

Logger Util
Used too log info, errors, or warnings

"""
import time
from colorama import Style, Fore
from datetime import datetime


class Logger:

    """
    Defenition for the logger
    :param name :The name of the logger
    :param color :The color of the name in the logger
    :param style :The style of the name in the logger
    
    """


    def __init__(self, name, color, style) -> None:
        self.name = name
        self.color = color 
        self.style = style
        pass

    

    def log(self, message : str):
        """
    
        Main logging function
        :param message :The message the logger sends
    
        """
        print(self.style + "[" + self.name + "]" + "(" + Time.getCurrentTime() + ") INFO: " + Fore.LIGHTGREEN_EX + Style.BRIGHT + message)


    def log_color(self, message : str, color : Fore):
        """
    
        Main logging function but with a color option
        :param message :The message the logger sends
        :param color :The color the logger message is

        """
        print(self.style + "[" + self.name + "]" + "(" + Time.getCurrentTime() + ") INFO: " + color + Style.BRIGHT + message)



    def log_color_style(self, message : str, color : Fore, style : Style):
        """

        Main logging function but with a color option
        :param message :The message the logger sends
        :param color :The color the logger message is
        :param style :The style the logger message is

        """
        print(self.style + "[" + self.name + "]" + "(" + Time.getCurrentTime() + ") INFO: " + color + style + message)

    

    def warning_color(self, message : str):
        """
    
        Main warning function
        :param message :The message the logger sends
        
        """
        print(self.style + "[" + self.name + "]" + "(" + Time.getCurrentTime() + ") WARNING: " + Fore.YELLOW + Style.BRIGHT + message)

    

    def warning_color(self, message : str, color : Fore):
        """
    
        Main warning function but with a color option
        :param message :The message the logger sends
        :param color :The color the logger message is

        """
        print(self.style + "[" + self.name + "]" + "(" + Time.getCurrentTime() + ") WARNING: " + color + Style.BRIGHT + message)

    

    def warning_color_style(self, message : str, color : Fore, style : Style):
        """

        Main warning function but with a color option
        :param message :The message the logger sends
        :param color :The color the logger message is
        :param style :The style the logger message is

        """
        print(self.style + "[" + self.name + "]" + "(" + Time.getCurrentTime() + ") WARNING: " + color + style + message)

   

    def error(self, message : str):
        """
    
        Main error function
        : param message :The message the logger sends
        
        """
        print(self.style + "[" + self.name + "]" + "(" + Time.getCurrentTime() + ") ERROR: " + Fore.RED + Style.BRIGHT + message)

   
    def error_color(self, message : str, color : Fore):
        """
    
        Main error function but with a color option
        :param message :The message the logger sends
        :param color :The color the logger message is

        """

        print(self.style + "[" + self.name + "]" + "(" + Time.getCurrentTime() + ") ERROR: " + color + Style.BRIGHT + message)

   

    def error_color_style(self, message : str, color : Fore, style : Style):

        """
        Main error function but with a color option
        : param message :The message the logger sends
        :param color :The color the logger message is
        :param style :The style the logger message is

        """

        print(self.style + "[" + self.name + "]" + "(" + Time.getCurrentTime() + ") ERROR: " + color + style + message)

    def setName(self, newName : str):

        """
        
        Changes the name of the logger
        :param newName:The new name of the logger 
        
        """

        self.name = newName

    def setColor(self, newColor : Fore):

        """
        
        Changes the color of the name of the logger
        :param newColor:The new color of the logger 
        
        """

        self.color = newColor

    def setStyle(self, newStyle : Style):

        """
        
        Changes the style of the name of the logger
        :param newStyle:The new style of the logger 
        
        """

        self.style = newStyle
        

"""

Time Util
Used to find the current time, and make countdowns

"""
class Time():

    def __init__(self) -> None:
        pass

    def getCurrentTime() -> str:
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        
        return current_time
    
    def countdown(h, m, s) -> bool:
 
    
        total_seconds = h * 3600 + m * 60 + s
    
        
        while total_seconds > 0:
    
            
            timer = datetime.timedelta(seconds = total_seconds)
            
            
            print(timer, end="\r")
    
            
            time.sleep(1)
    
           
            total_seconds -= 1
    
        return True
    