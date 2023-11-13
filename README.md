# WeatherMood-Forecast-System

Project Overview

The WeatherMood Forecast System is a Python application that combines weather forecasting with mood predictions. It utilizes weather data to predict moods like happiness, laziness, or anger and represents this information in a user-friendly interface.
File Descriptions

    interface.py
        This file contains the application class, which manages the mood prediction functions based on weather data.
        It imports mood-related functions from the weather module and AVL tree structures from node.

    main.py
        The entry point of the application.
        Initializes and runs the weather application, importing necessary modules and classes.

    node.py
        Defines the AVLNode and AVL classes for implementing AVL trees, used for data organization and processing.

    test_weather.py
        Contains test cases for the application, using the pytest framework.
        Tests various functionalities, including mood predictions and weather forecasting.

    weather.py
        Defines the forecast class, representing weather forecasts.
        Includes attributes like average temperature, date, highs, lows, and weather conditions.

    weather.txt
        A text file containing weather data in a structured format.
        Used as a data source for weather forecasting and mood predictions.

How to Run

    Ensure you have Python installed on your system.
    Run main.py to start the application: python main.py
    The application will utilize data from weather.txt and mood functions from weather to provide forecasts and mood predictions.

Dependencies

    Python 3.x
    numpy for numerical operations
    pytest for running tests

Testing

    Run tests using pytest: pytest test_weather.py
