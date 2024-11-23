Personal Assistant
A comprehensive Python-based personal assistant that simplifies daily tasks through voice commands and a user-friendly web interface. Perform tasks like sending emails, managing applications, fetching news, and much more, all seamlessly integrated into one program.
🚀 Features
🎙️ Voice Commands
Open popular applications (Google, YouTube, VS Code, Discord, etc.).
Perform system-level tasks (shutdown, restart, lock, adjust volume, brightness, etc.).
Search Wikipedia for quick information.
Fetch top news headlines using a public API.
Look up words and their definitions in a dictionary.
📧 Email Management
Send emails effortlessly with voice input.
Manage email recipients using an interactive GUI.
🎵 Media Control
Play music with Spotify integration.
Download YouTube videos directly via URL.
🌐 Web Integration
Search locations on Google Maps.
Fetch and announce your public IP address.
🖥️ System Utilities
Create and manage a to-do list.
Take and save screenshots.
Minimize or maximize application windows.
🖥️ Web-Based Interface
Access and control the assistant via a Flask-powered web application.
🛠️ Installation
Prerequisites
Ensure you have the following installed:

Python 3.x
Pip
Dependencies
Install the required libraries by running:
pip install pyttsx3 speAPI Keys
News API:

Register for an API key at News API.
Replace the news_api_key variable in the code with your key.
Spotify Integration:

Set up Spotify Developer credentials and configure the API key for Spotify functionality.
🖥️ Usage
Clone the Repository:

bash
Copy code
git clone <repository-link>  
cd <repository-name>  
Run the Application:

bash
Copy code
python <script_name>.py  
Access Web Interface:

Open your browser and go to:
arduino
Copy code
http://127.0.0.1:5000/  
💻 Supported Commands
Example Voice Commands:
Applications:
"Open YouTube"
"Search Wikipedia for Python programming"
Utilities:
"Create a to-do list"
"What is my IP address?"
Media Control:
"Play music on Spotify"
"Download a YouTube video"
System Management:
"Shutdown the computer"
"Minimize all windows"
📂 File Structure
File Name	Description
main.py	Main program for the personal assistant.
email_recipients.txt	Stores email recipients for quick access.
todo_list.txt	Saves tasks for the to-do list feature.
🌟 Future Enhancements
Multi-language Support: Enable commands in multiple languages.
Advanced AI Features: Provide personalized recommendations using AI.
Improved Web Interface: Add a full-featured GUI for easier interaction.
🤝 Contribution
Contributions are welcome! If you have ideas for improvements:

Fork the repository.
Create a new feature branch.
Submit a pull request.echrecognition wikipedia webbrowser psutil pyautogui spotipy flask requests pytube tk pymsgbox  
