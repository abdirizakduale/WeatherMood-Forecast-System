# WeatherMood Forecast System

## Project Overview
The WeatherMood Forecast System is a Python application that combines weather forecasting with mood predictions. It utilizes weather data to predict moods like happiness, laziness, or anger and represents this information in a user-friendly interface.

## File Descriptions

### `interface.py`
- Contains the `application` class, managing mood prediction functions based on weather data.
- Imports mood-related functions from `weather` and AVL tree structures from `node`.

### `main.py`
- Entry point of the application.
- Initializes and runs the weather application, importing necessary modules and classes.

### `node.py`
- Defines `AVLNode` and `AVL` classes for AVL trees, used for data organization and processing.

### `test_weather.py`
- Contains test cases for the application, using the `pytest` framework.
- Tests functionalities including mood predictions and weather forecasting.

### `weather.py`
- Defines the `forecast` class, representing weather forecasts.
- Includes attributes like average temperature, date, highs, lows, and weather conditions.

### `weather.txt`
- Text file containing weather data in a structured format.
- Used as a data source for weather forecasting and mood predictions.

## How to Run
- Ensure Python is installed on your system.
- Run `main.py` to start the application: 
  ```shell
  python main.py
  ```

## Dependencies
  - Python 3.x
  - `numpy` for numerical operations
  - `pytest` for running test

## Testing
  - Run tests using  `pytest`
    ```shell
    pytest test_weather.py
    
