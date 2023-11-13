'''
Abdirizak Duale
CS302
08-26-2023
The file has all the declarations and implementation for my hierarchy including the applications class that has my run functions 
'''
from node import AVL
import numpy as np
import pdb
import os 
from abc import ABC, abstractmethod

# Base class for my hierarchy
class forecast() :
    
    # Constructor for forecast base class
    def __init__(self, avg_temp, date, day, highs, lows, conditions) :
        self._avg_temp = avg_temp
        self._date = date
        self._day = day
        self._highs = highs
        self._lows = lows
        self._conditions = conditions
        
    
    # Load function to read from my weather.txt file onto a python list 
    def load_list(self, file_path) :
        weather_data = []
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                avg_temp, date, day, highs, lows, conditions = parts
                avg_temp = int(avg_temp)
                data_instance = forecast(avg_temp, date, day, highs, lows, conditions)
                weather_data.append(data_instance)
        return weather_data
    
    # Load function to read from my weather.txt file onto a numpy list 
    def load_numpy(self, filepath) : 
        forecasts = []

        with open(filepath, 'r') as file:
            lines = file.readlines()

        average_temp = [int(line.split('|')[0]) for line in lines]

        nparr = np.array(average_temp, dtype=int)

        for avg_tmp in nparr:
            forecast_obj = forecast(avg_tmp, None, None, None, None, None)  # Initialize other attributes accordingly
            forecasts.append(forecast_obj)

        return forecasts

    
    # Display function to display the average weather forecast, for numpy list
    def display(self, obj) :
        if obj : 
            print('-' * 100)
            print(f"The average is for today is: {obj._avg_temp}")
            return True
        else :
            return False
    
    # < operator overload
    def __lt__(self, other) :

        try : 
            if isinstance(other, forecast) :
                return self._avg_temp < other.avg_temp
        except AttributeError :
            return "ERROR UNSUPPORTED ENTRIES"

    # > operator overload
    def __gt__(self, other) :

        try : 
            if isinstance(other, forecast) :
                return self._avg_temp > other.avg_temp

        except AttributeError :
            return "ERROR UNSUPPORTED ENTRIES"

# Happy derived class that has happy tones for weather forecast
class happy(forecast) : 
    
    # Derived class constructor
    def __init__(self) : 
        pass
    
    # High temperature output for derived class
    def high(self, obj) : 
        if obj : 
            print('-' * 100)
            print(f"Good morning everyone, it is the first week of August 2016, and todays date is {obj._date}")
            print(f"it is a beautiful {obj._day} we're having today. You can expect awesome highs of {obj._highs}, and lows of {obj._lows}")
            print(f"Go out and enjoy this beautiful day by going to a lake with you family!!")
            return True
        else :
            return False
        

    # Mid temperature output for derived class
    def mid(self, obj) :
        if obj :
            print('-' * 100)
            print(f"Good morning everyone, it is the first week of August 2016, and todays date is {obj._date}")
            print(f"it is a beautiful {obj._day} we're having today. You can expect awesome highs of {obj._highs}, and lows of {obj._lows}")
            print(f"It's not too hot nor is too cold so go out and enjoy this weather by going on hike in one of our beauftiful national parks!")
            return True
        else : 
            return False
        

    # Low temperature output for derived class
    def low(self, obj) :
        if obj :
            print('-' * 100)
            print(f"Good morning everyone, it is the first week of August 2016, and todays date is {obj._date}")
            print(f"it is a beautiful {obj._day} we're having today. You can expect awesome highs of {obj._highs}, and lows of {obj._lows}")
            print(f"It's on the colder end today so I suggest staying inside and sitting around the fireplace with some hot cocoa!")
            return True
        else : 
            return False

# Lazy derived class that outputs lazy forecasts
class lazy(forecast) : 
    
    # Derived class constructor
    def __init__(self) : 
        pass
    
    # High temperature output for derived class
    def high(self, obj) : 
        if obj : 
            print('-' * 100)
            print(f"the date is {obj._date}")
            print(f"it is a burning hot {obj._day} today. The highs {obj._highs}, and the lows {obj._lows}")
            print(f"It's soo hot mannn, I really hate sweating why would you ever leave your air conditioned rooom in this weather")
            return True
        else : 
            return False

    # Mid temperature output for derived class
    def mid(self, obj) :
        if obj :
            print('-' * 100)
            print(f"the date is {obj._date}")
            print(f"it is a mildly warm {obj._day} today. The highs {obj._highs}, and the lows {obj._lows}")
            print(f"I hate days like this when its not hot or cold, everyones always trying to do something outside, just stay inside")
            return True
        else : 
            return False

    # Low temperature output for derived class
    def low(self, obj) :
        if obj :
            print('-' * 100)
            print(f"the date is {obj._date}")
            print(f"it is a cold {obj._day} today. The highs {obj._highs}, and the lows {obj._lows}")
            print(f"It's freezing out, I can't even talk my lips froze from the walk over here, why'd I ever leave my house")
            return True
        else : 
            return False
        

# Mad derived class that outputs angry forecasts
class mad(forecast) : 
    
    # Derived class constructor
    def __init__(self) : 
        pass
    
    # High temperature output for derived class
    def high(self, obj) : 
        if obj :
            print('-' * 100)
            print(f"Morning, the date is {obj._date}")
            print(f"{obj._day}, has some hot weather. The highs for today is {obj._highs}, the lows are {obj._lows}")
            print(f"The weather… GOSH-DARNIT STOP TALKING IN MY EAR SO LOUD")
            return True
        else :
            return False

    # Mid temperature output for derived class
    def mid(self, obj) :
        if obj :
            print('-' * 100)
            print(f"Morning, the date is {obj._date}")
            print(f"{obj._day}, has some hot weather. The highs for today is {obj._highs}, the lows are {obj._lows}")
            print(f"The weather today is really nice out… FUDGE I WISH  I WAS OUT THERE INSTEAD OF HERE")
            return True
        else : 
            return False

    # Low temperature output for derived class
    def low(self, obj) :
        if obj : 
            print('-' * 100)
            print(f"Morning, the date is {obj._date}")
            print(f"{obj._day}, has some hot weather. The highs for today is {obj._highs}, the lows are {obj._lows}")
            print(f"We have black ice on the road, so make sure to pay attention… DAMN IT MY CAR GOT HIT BY SOMEONE NOT PAYING ATTENTION")
            return True
        else :
            return False

