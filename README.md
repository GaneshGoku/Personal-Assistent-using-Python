Personal Assistant
A robust and versatile Python-based personal assistant designed to streamline daily tasks using voice commands. From sending emails to playing music, fetching news, and even controlling system settings, this assistant has you covered!

Features
Voice Interaction: Issue commands via voice for hands-free usage.
Task Automation:
Open applications like Google, YouTube, and VS Code.
Manage system functions (shutdown, restart, lock, volume, brightness, etc.).
Send emails and manage recipients through an intuitive GUI.
Create and update a to-do list.
Information Retrieval:
Search Wikipedia and retrieve news headlines.
Look up words in the dictionary.
Media Handling:
Play music using Spotify integration.
Download YouTube videos effortlessly.
System Utilities:
Take screenshots.
Minimize or maximize windows by app name.
Clear browsing data.
Web Integration:
Search locations on Google Maps.
Fetch and speak your system's public IP address.
Flask-based Web Interface: Execute commands through a web UI.
Installation
Prerequisites
Ensure you have the following installed:

Python 3.x
Pip
Required Libraries
Install the required libraries using:

bash
Copy code
pip install pyttsx3 speechrecognition wikipedia webbrowser psutil pyautogui spotipy flask requests pytube tk pymsgbox  
API Keys
For news retrieval, register for an API key at News API.
Update the news_api_key variable in the code with your key.
Spotify integration requires setup with Spotify Developer API.
Usage
Clone the repository:

bash
Copy code
git clone <repository-link>  
cd <repository-name>  
Run the program:

bash
Copy code
python <script_name>.py  
To use the web interface:

Access the app at http://127.0.0.1:5000/ in your browser.
Voice Commands:

Speak directly to perform actions. Examples include:
"Open YouTube"
"What is the time?"
"Send an email to John."
"Search Google Maps for New York."
File Descriptions
main.py: Contains the primary assistant code.
email_recipients.txt: Stores recipient data for email functionality.
todo_list.txt: Stores tasks for the to-do list.
Future Enhancements
Add support for multi-language voice commands.
Implement AI-based personalized recommendations.
Enhance the GUI for the web interface.
Contribution
Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request
