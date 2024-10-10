from setuptools import setup, find_packages

setup(
    name='better_correct_fast',
    version='0.1.0',
    author='Boy d'Hont',
    author_email='contact@bdhont.net',
    description='Simplified BIM Collaboration Format (BCF) generation for project leaders and managers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/boydhont/BetterCorrectFast',
    packages=find_packages(),
    install_requires=[
        'ifcopenshell',  # Add ifcopenshell as a dependency
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change as necessary
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify your Python version compatibility
)