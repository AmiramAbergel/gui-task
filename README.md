# gui-task


This application is built using Python and allows users to run a GUI on demand, returning data from the GUI to be used in a script.</br>
Detail-wise, this is a flask web application consisting of two pages, Page 1 and Page 2.</br>
It is possible to configure settings on these pages and save them as a YAML file.</br>
Settings include mode, tests, users, a background image for reports, and hardware acceleration.</br>
You can also add and remove rows from the users' table and check and uncheck the checkboxes for the tests.</br>
You can also upload a new report background image, and you can also select which test checkbox is checked.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)


## Installation
  
1. Make sure you have **Python 3.6.2** or later installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
2. Ensure you have the latest stable version of [pip](https://pypi.org/project/pip/). To check your pip version,</br> 
   run `pip --version `. To update pip, run `python -m pip install --upgrade pip`.
3. Clone this repository to your local machine:
   - git clone https://github.com/AmiramAbergel/gui-task.git
4. Install the required dependencies:
   -  `pip install -r requirements.txt`
  
  
## Usage

To run the application, navigate to the project directory and run the following command:
  
    - python app.py
  
This will launch the GUI in your default web browser, allowing you to interact with it and return data to your script.
<br><br>
 - This project can be used as an external library. Here's an example of how to import and run the app from another Python script:
```
from my_gui_app import main

def process_yaml_data(yaml_data):
    print("YAML data received:")
    print(yaml_data)

if __name__ == "__main__":
    main(callback=process_yaml_data)

```
Replace `my_gui_app` with the name of the directory containing app.py file of this project.
 This is the directory that converted into a package by creating the `__init__.py` file. 
When you import the package in another Python script, you can run the GUI app and process the YAML data after the app is closed.


## File Structure

- `app.py`: The main script that initializes the application and launches the GUI.
- `routes.py`: This file contains the route functions that handle HTTP requests to different URLs within the application.
- `forms.py`: This file contains the form classes used in the application, including PageOneForm, PageTwoForm, and UserForm.
- `utils.py`: This file contains utility functions for reading and writing the YAML configuration file, generating a random configuration, validating email, and logging messages.
- `index.html`: This is the base HTML template that other templates extend.
- `pageOne.html`: This is the HTML template for Page 1 of the application, which includes the form for configuring settings on Page 1.
- `pageTwo.html`: This is the HTML template for Page 2 of the application, which includes the form for configuring settings on Page 2.
- `index.style.css`:  This is a CSS-style file used by index.html. It  contains instructions for how index.html elements should be displayed on the page.


## Screenshot

![Screenshot 2023-04-08 203032](https://user-images.githubusercontent.com/39462161/230735257-496f1562-1603-46b1-ab51-9db061d68c35.png)
![Screenshot 2023-04-08 203207](https://user-images.githubusercontent.com/39462161/230735268-c8182aac-9ec2-4365-8440-f8182fa7d067.png)



## Video




https://user-images.githubusercontent.com/39462161/230986059-4bfddda8-7570-49c1-9914-27d8d548701d.mp4





