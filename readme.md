# Part 2 - Final Project

## Overview
This document provides an overview of Part 2 of the final project for the course 4200.

```plaintext
Part2/
├── main.py                  # Entry point for the program
├── modules/                 # Contains all the modules used in the project
│   ├── __init__.py          # Initializes the package
│   ├── config.py            # Contains configuration data
│   ├── file_sorter.py       # Handles file sorting and moving them to directories
│   └── logger.py            # Handles logging of events
├── files/                   # Directory for the files to be sorted
├── readme.md                # Documentation (this file)
├── setup.py                 # Installation script for the project
├── test_part2.py            # Test script to validate the functionalities
└── logs.txt                 # Log file for recording operations
```

## How to use
### Option 1. Clone the repository 
    1. Clone the repository
    2. Install the required dependency
    3. Run the program 
    

### Option 2. Download the ZIP file
    1. Download the zip file containing the project
    2. extract the zip file to a directory
    3. navigate to the project folder in a terminal
    4. Install dependencies
   
        ```bash
        pip install -r requirements.txt
        ```
    5. Run the program 

    ```bash
    python main.py
    ```

## Testing
To run the tests, use the following command:
```bash
python test_part2.py
```

## License
This project is licensed under the MIT License.

