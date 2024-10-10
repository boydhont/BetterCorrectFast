# BetterCorrectFast
Simplified BIM Collaboration Format (BCF) generation for project leaders and managers

## Building the package
Setting up a virtual environment:
```
python -m venv venv
```

Activating the virtual environment:
```
:: Windows CMD
env\Scripts\activate.bat
```
```
# Windows PowerShell
env\Scripts\Activate.ps1
```
```
# macOS/Linux
source venv/bin/activate
```

Installing required libraries:
```
pip install -r requirements.txt
```

Running tests:
```
python -m unittest discover -s tests
```

Building the package:
```
python setup.py sdist bdist_wheel
```