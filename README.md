# Setting Up the Project `venv`

Using a virtual environment in Python is recommended for package management. It creates an isolated environment, allowing you to work on a specific project without affecting others. Here's how to set up a virtual environment using `venv` on macOS, Windows, and Linux.

## Requirements

- Python 3.10 or newer

## Instructions

### macOS & Linux

1. **Install `venv` (if necessary)**:

    ```bash
    python3 -m ensurepip --default-pip
    ```

2. **Create a Virtual Environment**:

    Navigate to your project directory or the directory where you want to create the virtual environment. Then, run:

    ```bash
    python3 -m venv venv
    ```

    This will create a virtual environment named `venv` in the current directory.

3. **Activate the Virtual Environment**:

    ```bash
    source venv/bin/activate
    ```

    Once activated, your terminal or shell prompt will change to show the name of the activated environment.

4. **Deactivate the Virtual Environment**:

    When you're done, you can deactivate the virtual environment and return to the global Python environment by simply running:

    ```bash
    deactivate
    ```

### Windows

1. **Install `venv` (if necessary)**:

    ```bash
    python -m ensurepip --default-pip
    ```

2. **Create a Virtual Environment**:

    Navigate to your project directory or the directory where you want to create the virtual environment. Then, run:

    ```bash
    python -m venv venv
    ```

    This will create a virtual environment named `venv` in the current directory.

3. **Activate the Virtual Environment**:

    ```bash
    .\venv\Scripts\activate
    ```

    Once activated, your command prompt will change to show the name of the activated environment.

4. **Deactivate the Virtual Environment**:

    When you're done, you can deactivate the virtual environment and return to the global Python environment by simply running:

    ```bash
    deactivate
    ```

## Setting Up the Project

With the virtual environment activated:

1. **Install the Necessary Packages**:

    If you have a `requirements.txt` file in your project directory, install the necessary packages using:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Project**:

    Start the project using the following command:

    ```bash
    reflex run
    ```

    The project will run on `localhost:3000`.
