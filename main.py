from interface import user
from interface import weather_app 
from interface import application 
from node import AVLNode
from node import AVL 
from weather import forecast
from weather import happy 
from weather import lazy 
from weather import mad 

# Minimal main implementation
if __name__ == "__main__":
    app = weather_app()
    app.run()