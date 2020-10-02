from pybraille.main import convertText, convertFile

def testConvertText():
  assert convertText("hello") == "⠓⠑⠇⠇⠕"

def testConvertFile():
  assert convertFile("tests/sample.txt") == "⠠⠞⠓⠊⠎ ⠙⠊⠗⠑⠉⠞⠕⠗⠽ ⠉⠕⠝⠞⠁⠊⠝⠎ ⠞⠑⠎⠞ ⠋⠊⠇⠑⠎⠲"