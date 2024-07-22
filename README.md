# Virtual-Ayurveda☘️:
Virtual Ayurveda is a Python application designed to provide Ayurvedic solutions for common symptoms. It integrates local Ayurvedic remedies with Wikipedia's API to offer comprehensive information about various symptoms and their treatments.

# Features:
1. Local Ayurvedic Remedies: Provides quick solutions based on a predefined list of common symptoms.

2. Wikipedia Integration: Fetches detailed information and additional remedies from Wikipedia if local data is not available.

3. Usage Details: Extracts and displays a brief explanation of the symptom from Wikipedia.

# Installation:
To get started with the Ayurveda Assistant, you'll need to have Python installed on your machine. You also need to install the required libraries. You can do this using pip:

pip install wikipedia-api requests beautifulsoup4

Run the Application:

After installing the dependencies, you can run the application using:

bash

python virtual_ayurveda.py

Enter a Symptom:

When prompted, enter a symptom you are experiencing. The application will provide a recommended Ayurvedic solution based on the symptom.

Get Detailed Information:

In addition to the recommended remedy, the application will also fetch a brief explanation of the symptom from Wikipedia

# Code Overview:
AyurvedaAssistant Class:  Contains methods for:

get_local_solution(symptom): Retrieves solutions from a predefined list.

get_api_solution(symptom): Fetches additional information from Wikipedia.

get_ayurvedic_solution(symptom): Determines the solution by first checking local data and then Wikipedia.

get_detailed_usage(symptom): Extracts usage details from Wikipedia.

run(): Main method to interact with the user.

# Dependencies Used:

wikipediaapi: For accessing Wikipedia content.

requests: For making HTTP requests.

beautifulsoup4: For parsing HTML content.

Contributing
Contributions are welcome! If you have suggestions or improvements, please feel free to fork the repository and submit a pull request.

# Contributors:

The following project is fully contributed by only Parkhi Rastogi.

# Language Provisioned:

The following project is fully being implemented in Python only.


