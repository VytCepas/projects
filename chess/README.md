# DS.v3.1.2.5
# Calculator Project

## Overview

This project implements a simple calculator in Python, capable of performing arithmetic operations. The calculator uses a memory value to store the result of the last operation, allowing for sequential calculations.

## Requirements

- Python 3.12 or higher
- Jupyter Notebook (for Jupyter support)

## Installation

To run this project, you need Python installed on your system. The project depends on several external packages, which are listed in the `requirements.txt` file.

### Steps to Install and Run:

1. **Clone the Repository**

    First, clone this repository to your local machine using Git:

    `git clone <repository-url>`


2. **Create a Virtual Environment (Optional)**

    It's recommended to create a virtual environment to keep dependencies required by the project separate from your global Python environment:

    `python3 -m venv venv` install virtual environment.

    `source venv/bin/activate` to activate venv for current shell.


3. **Install Dependencies**

    Install the project dependencies by running:

    `pip install -r requirements.txt`

    For Jupyter Notebook support, also ensure Jupyter is installed: (Most probably installed with the command above)

    `pip install notebook`


4. **Run the Calculator**

    Start the calculator by running (from project root directory):

    `python3 -m app`

    For Jupyter Notebook users, launch Jupyter Notebook:

    `jupyter notebook`

    Navigate to the notebook file (.ipynb) within the project directory to interact with the calculator.


5. **Run the unit tests**

    To execute unit tests run:

    `pytest`

