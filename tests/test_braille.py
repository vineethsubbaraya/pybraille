import pathlib
import pytest
from pybraille.main import convertText, convertFile

SAMPLE_TXT = pathlib.Path(__file__).parent / "sample.txt"

# --- convertText: basic ---

def testConvertText():
  assert convertText("hello") == "⠓⠑⠇⠇⠕"

def testEmptyString():
  assert convertText("") == ""

def testSingleLetter():
  assert convertText("a") == "⠁"

# --- convertText: uppercase ---

def testUppercaseAddsCapIndicator():
  # 'A' should be caps indicator + braille 'a'
  assert convertText("A") == "⠠⠁"

def testMixedCase():
  # Each uppercase letter gets its own caps indicator
  assert convertText("Hi") == "⠠⠓⠊"

# --- convertText: numbers ---

def testSingleDigit():
  # num indicator + braille cell for '1' (same cell as 'a')
  assert convertText("1") == "⠼⠁"

def testMultiDigitNumber():
  # num indicator appears only once at the start
  assert convertText("123") == "⠼⠁⠃⠉"

def testNumberModeResetOnLetter():
  # After a non-number-punctuation char, number mode resets
  # so the second digit gets a new num indicator
  assert convertText("1a2") == "⠼⠁⠁⠼⠃"

def testNumberPunctuationKeepsNumberMode():
  # Comma inside a number keeps number mode — second digit gets no new num indicator
  assert convertText("1,2") == "⠼⠁⠂⠃"

# --- convertText: punctuation ---

def testPeriod():
  assert convertText(".") == "⠲"

def testComma():
  assert convertText(",") == "⠂"

def testExclamation():
  assert convertText("!") == "⠖"

def testQuestion():
  assert convertText("?") == "⠦"

def testOpenParen():
  assert convertText("(") == "⠷"

def testCloseParen():
  assert convertText(")") == "⠾"

def testParensDistinct():
  assert convertText("(") != convertText(")")

def testDollarDistinctFromPeriod():
  assert convertText("$") != convertText(".")

# --- convertText: escape characters ---

def testNewlinePassthrough():
  assert convertText("a\nb") == "⠁\n⠃"

def testTabPassthrough():
  assert convertText("a\tb") == "⠁\t⠃"

# --- convertText: unsupported characters ---

def testUnsupportedCharSkipped():
  # '@' is not in the mapping — should be silently skipped
  assert convertText("@") == ""

def testUnsupportedCharMidString():
  assert convertText("a@b") == "⠁⠃"

# --- convertText: type errors ---

def testNonStringRaisesTypeError():
  with pytest.raises(TypeError):
    convertText(123)

def testNoneRaisesTypeError():
  with pytest.raises(TypeError):
    convertText(None)

def testListRaisesTypeError():
  with pytest.raises(TypeError):
    convertText(["hello"])

# --- convertFile ---

def testConvertFile():
  assert convertFile(str(SAMPLE_TXT)) == "⠠⠞⠓⠊⠎ ⠙⠊⠗⠑⠉⠞⠕⠗⠽ ⠉⠕⠝⠞⠁⠊⠝⠎ ⠞⠑⠎⠞ ⠋⠊⠇⠑⠎⠲"

def testConvertFileNonStringRaisesTypeError():
  with pytest.raises(TypeError):
    convertFile(42)
