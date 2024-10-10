from setuptools import setup, find_packages # type: ignore

# Read the contents of the README file for the long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='better_correct_fast',
    version='0.1.0',
    author='Boy d\'Hont',  # Escape the single quote in the name
    author_email='contact@bdhont.net',
    description='Simplified BIM Collaboration Format (BCF) generation for project leaders and managers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/boydhont/BetterCorrectFast',
    packages=find_packages(),  # Automatically find package directories
    install_requires=[
        'ifcopenshell',  # Required dependency
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the required Python version
    license='MIT',  # Specify your license type
)
