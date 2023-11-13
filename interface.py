from weather import forecast
from weather import happy 
from weather import lazy 
from weather import mad 
from node import AVLNode
from node import AVL 

# Application class that handles my run functions for happy, mad, and lazy
class application : 

    # Application class constructor
    def __init__(self, weather_data) : 
        self.weather_data = weather_data
    
    # Run for happy functions for list 
    def run_happy(self) :
        if self.weather_data :
            happy1 = happy()
            for obj in self.weather_data:
                forecast1 = forecast(obj._avg_temp, obj._date, obj._day, obj._highs, obj._lows, obj._conditions)
                if 85 <= obj._avg_temp <= 95:
                    happy1.high(obj)
                    forecast1.display(obj)
                elif 65 <= obj._avg_temp <= 84:
                    happy1.mid(obj)
                    forecast1.display(obj)
                else:
                    happy1.low(obj)
                    forecast1.display(obj)
            return True 
        else :
            return False
    
    # Run for lazy functions for list 
    def run_lazy(self) : 
        if self.weather_data :
            lazy1 = lazy()
            for obj in self.weather_data:
                forecast1 = forecast(obj._avg_temp, obj._date, obj._day, obj._highs, obj._lows, obj._conditions)
                if 85 <= obj._avg_temp <= 95:
                    lazy1.high(obj)
                    forecast1.display(obj)
                elif 65 <= obj._avg_temp <= 84:
                    lazy1.mid(obj)
                    forecast1.display(obj)
                else:
                    lazy1.low(obj)
                    forecast1.display(obj)
            return True
        else :
            return False

    # Run for mad functions for list 
    def run_mad(self) : 
        if self.weather_data :
            mad1 = mad()
            for obj in self.weather_data:
                forecast1 = forecast(obj._avg_temp, obj._date, obj._day, obj._highs, obj._lows, obj._conditions)
                if 85 <= obj._avg_temp <= 95:
                    mad1.high(obj)
                    forecast1.display(obj)
                elif 65 <= obj._avg_temp <= 84:
                    mad1.mid(obj)
                    forecast1.display(obj)
                else:
                    mad1.low(obj)
                    forecast1.display(obj)
                    
            return True
        else :
            return False 


# User class that handles and displays the User data
class user:

    # Constructor for user class
    def __init__(self, username):
        self.username = username
        self.choices = []

    # Add choice funtion that adds on to choices list
    def add_choice(self, choice):
        self.choices.append(choice)
        
    # Print function that prints the choices list
    def print(self) :
        print("The choices you made were:", ", ".join(self.choices))
        #print("Your choices are: ", self.choices)

# Weather app function that handles all the interactions with my client while loops
class weather_app:

    # Default constructor for weather app class
    def __init__(self):
        self.user_tree = AVL()

    # Function that runs the outer while loop of my client interface 
    def run(self):
        while True:
            print('-' * 100)
            print("1. Create User")
            print("2. Display Users")
            print("3. Search Users")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.user_tree.display()
            elif choice == '3':
                print('-' * 100)
                search = input("Enter your choice: ")
                found = self.user_tree.retrieve(search)
                if found == None :
                    print('-' * 100)
                    print(f"The username you were looking for couldn't be found")
                else :
                    print('-' * 100)
                    print(f"Username {found} was found!")
            elif choice == '4':
                break
            else:
                print("Please choose 1, 2, 3, or 4")

    # Function that runs the inner while loop of my client interface 
    def create_user(self):
        file_path = 'weather.txt'
        #pdb.set_trace()  # Set a breakpoint
        test1 = forecast(None, None, None, None, None, None)
        weather_data = test1.load_list(file_path)

        average_data = test1.load_numpy(file_path)

        app = application(weather_data)
        print('-' * 100)
        username = input("Enter a username: ")
        new_user = user(username)
        self.user_tree.insert(username, new_user)  # Insert the user into the AVL tree

        while True:
            print('-' * 100)
            print("1. Happy weather forecast")
            print("2. Lazy weather forecast")
            print("3. Mad Weather forecast")
            print("4. Log Out")

            choice = input("Enter your choice: ")

            if choice in ['1']:
                new_user.add_choice("Happy weather forecast")
            elif choice in ['2']:
                new_user.add_choice("Lazy weather forecast")
            elif choice in ['3']:
                new_user.add_choice("Mad weather forecast")

            if choice == '1' :
                app.run_happy()
                pass
            elif choice == '2' :
                app.run_lazy()
            elif choice == '3' :
                app.run_mad()
            #elif choice == '4' :
            #   print(weather_data[0] < weather_data[1])
            #elif choice == '4' :
            #    test = happy()
            #    print(weather_data[0] > test)
            elif choice == '4' :
                break
            else :
                print('-' * 100)
                print("Choose 1, 2, 3 or 4")