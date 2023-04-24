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

To run the application, navigate to the project directory where this Readme file is located and run the following command:
  
    - python script.py
  

## File Structure
- `script.py`: This is the main script that runs the application.
- `gui_app`: Main folder containing the GUI application.
  - `static`: Folder containing static files such as CSS and JavaScript.
    - `css`: Folder containing CSS files.
      - `index.style.css`:  This is a CSS-style file used by index.html. It  contains instructions for how index.html elements should be displayed on the page.
    - `js`: Folder containing JavaScript files.
      - `script.js`: This is a JavaScript file used by index.html. It contains instructions for how index.html elements should be displayed on the page.
  - `templates`: Folder containing HTML templates.
    - `index.html`: This is the base HTML template that other templates extend.
    - `pageOne.html`: This is the HTML template for Page 1 of the application, which includes the form for configuring settings on Page 1.
    - `pageTwo.html`: This is the HTML template for Page 2 of the application, which includes the form for configuring settings on Page 2.
    - `sharedFormElements.html`: This is the HTML template for the shared form elements between Page 1 and Page 2.
    - `finishPage.html`: This is the HTML template for the finish page, which is displayed after the user clicks the "Finish" button.
  - `tests`: Folder containing test files.
      - `test.py`: This is a test file that contains a test function that tests the application.
  - `app.py`: This file contains the GUI application object and the main function that runs the application.
  - `routes.py`: This file contains the route functions that handle HTTP requests to different URLs within the application.
  - `forms.py`: This file contains the form classes used in the application, including PageOneForm, PageTwoForm, and UserForm.
  - `utils.py`: This file contains utility functions for reading and writing the YAML configuration file, generating a random configuration, validating email, and logging messages.


## Screenshot

![gui_page1_screenshot](https://user-images.githubusercontent.com/39462161/233947547-8ddb9da4-85e2-4679-a7b0-693c29e2d81f.png)
![gui_page2_screenshot](https://user-images.githubusercontent.com/39462161/233947565-603a2152-8ba9-4050-97a0-b5e87c26993c.png)




## Video



https://user-images.githubusercontent.com/39462161/233947664-189e538e-7c16-4e73-b84e-a384d7a64fc6.mp4


