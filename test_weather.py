'''
Abdirizak Duale
CS302
08-26-2023
The file has all the declarations and implementation for the pytest of my hierarchy functions
'''
from weather import forecast 
from weather import happy 
from weather import lazy
from weather import mad 
from interface import application 
import pytest

# Setup funtion for happy
@pytest.fixture
def setup1() : 
    test = happy()
    return test 

# Setup funtion for lazy 
@pytest.fixture
def setup2() :
    test = lazy()
    return test

# Setup funtion for mad 
@pytest.fixture
def setup3() :
    test = lazy()
    return test

# Setup funtion for forecast 
@pytest.fixture
def setup4() :
    test = forecast(None, None, None, None, None, None)
    return test
    

# Test funtion for happy 
def test_happy(setup1 : happy) :
    high_temp = forecast(90, None, None, None, None, None)
    mid_temp = forecast(70, None, None, None, None, None)
    low_temp = forecast(30, None, None, None, None, None)
    assert setup1.high(high_temp) == True
    assert setup1.mid(mid_temp) == True
    assert setup1.low(low_temp) == True 

# Test funtion for lazy 
def test_lazy(setup2 : lazy) :
    high_temp = forecast(90, None, None, None, None, None)
    mid_temp = forecast(70, None, None, None, None, None)
    low_temp = forecast(30, None, None, None, None, None)
    assert setup2.high(high_temp) == True
    assert setup2.mid(mid_temp) == True
    assert setup2.low(low_temp) == True 

# Test funtion for mad 
def test_mad(setup3 : mad) :
    high_temp = forecast(90, None, None, None, None, None)
    mid_temp = forecast(70, None, None, None, None, None)
    low_temp = forecast(30, None, None, None, None, None)
    assert setup3.high(high_temp) == True
    assert setup3.mid(mid_temp) == True
    assert setup3.low(low_temp) == True 
    
# Testing load python list for forecast funtion 
def test_load_list(setup4 : forecast) :
    file_path = 'weather.txt'
    test1 = forecast(None, None, None, None, None, None)
    loaded_data = test1.load_list(file_path)
    
    assert len(setup4.load_list(file_path)) == len(loaded_data)
    
    for i in range(len(loaded_data)):
        assert setup4.load_list(file_path)[i]._avg_temp == loaded_data[i]._avg_temp
        assert setup4.load_list(file_path)[i]._date == loaded_data[i]._date
        assert setup4.load_list(file_path)[i]._day == loaded_data[i]._day
        assert setup4.load_list(file_path)[i]._highs == loaded_data[i]._highs
        assert setup4.load_list(file_path)[i]._lows == loaded_data[i]._lows
        assert setup4.load_list(file_path)[i]._conditions == loaded_data[i]._conditions
    
# Testing load numpy list for forecast funtion 
def test_load_numpy(setup4 : forecast) :
    file_path = 'weather.txt'
    test1 = forecast(None, None, None, None, None, None)
    loaded_data = test1.load_numpy(file_path)
    
    assert len(setup4.load_list(file_path)) == len(loaded_data)
    
    for i in range(len(loaded_data)):
        assert setup4.load_list(file_path)[i]._avg_temp == loaded_data[i]._avg_temp
    
# Testing display forecast funtion 
def test_display(setup4 : forecast) :
    test1 = forecast(None, None, None, None, None, None)
    assert setup4.display(test1) == True 