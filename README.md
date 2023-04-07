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

![Screenshot 2023-04-02 212118](https://user-images.githubusercontent.com/39462161/229371432-0c484338-42a4-4fc1-9cbc-f01b6bf80125.png)
![Screenshot 2023-04-02 212217](https://user-images.githubusercontent.com/39462161/229371472-9d4ae2c1-d3b7-47ce-81c6-5247b83f64f2.png)


## Video


https://user-images.githubusercontent.com/39462161/229372739-1fd7d308-9db4-48ba-8a40-51f573695d50.mp4



