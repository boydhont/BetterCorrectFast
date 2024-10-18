# BetterCorrectFast

Simplified BIM Collaboration Format (BCF) generation for project leaders and managers.

![](bettercorrectfast/assets/icon.jpg)

[![PyPI](https://img.shields.io/pypi/v/bcf-client?label=PyPI&color=006dad)](https://pypi.org/project/bettercorrectfast/)

## Usage

Install the library:
```
pip install bettercorrectfast
```

Create and save an issue locally:
```
import bettercorrectfast as bcf

issue = bcf.create("Title", "Description", "Screenshot.png")
bcf.save(issue, "issue.bcf")
```

It is also possible to add a title, description and/or snapshot to the issue:

```
issue_from_text = bcf.create("Title", "Description")

issue_from_title = bcf.create(title="Title)
issue_from_description = bcf.create(description="Description")
issue_from_image = bcf.create(image_filepath="Screenshot.jpg")
```

## Technical Notes

The issue schema conforms to the BCF (BIM Collaboration Format) version 2.0 standard as defined by buildingSMART International.

**Note:** This library currently supports image snapshots exclusively in .png format. Support for .jpg format is in development.

## Building the Package

Setting up a virtual environment:
```
python -m venv env
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
