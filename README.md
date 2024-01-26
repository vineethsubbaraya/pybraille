# PyBraille

A simple library in Python to convert text to 6-dots pattern braille (Grade 1)

## Installation

Run the following to install the package

```python
pip install pybraille
```

## Usage

```python
from pybraille import convertText

print(convertText("hello"))
>>> ⠓⠑⠇⠇⠕

print(convertFile("filename.txt")) #eg: tests/sample.txt
>>> ⠠⠞⠓⠊⠎ ⠙⠊⠗⠑⠉⠞⠕⠗⠽ ⠉⠕⠝⠞⠁⠊⠝⠎ ⠞⠑⠎⠞ ⠋⠊⠇⠑⠎⠲
```

## Testing

This library needs is tested against python 3.6 and 3.7. Both interpreters need to be available to tox

Running tests:

```tox``` or ```pytest```

#### Support
Any python 3.x version should work.
