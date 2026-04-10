# Mini-LLM-Security-Gateway
Project Setup and Environment Configuration
The following steps were followed to set up the development environment for the project:
1. Development Environment Setup :
Installed Visual Studio Code (VS Code) as the primary code editor.
Created a new project folder and opened it in VS Code.
Configured Python by adding the installed Python interpreter to VS Code.
2. Virtual Environment Setup :
To isolate project dependencies, a virtual environment was created:
Installed virtual environment tool:
pip install virtualenv
Created a virtual environment:
virtualenv env
3. Activating Virtual Environment (Windows) :
Before activation, PowerShell execution policy was configured to allow script execution:
Execution Policy Setup:
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
If required, permissions were adjusted to allow script execution.
Activate virtual environment:
.\env\Scripts\activate.ps1
After activation, the virtual environment was successfully enabled.
4. Installing Required Dependencies :
The following libraries were installed inside the virtual environment:
Flask (web framework):
pip install flask
Presidio Analyzer (PII detection library):
pip install presidio-analyzer presidio_anonymizer
6. Frontend Integration :
A templates folder was created inside the main project directory.
An HTML file (template1.html) was added inside it.
