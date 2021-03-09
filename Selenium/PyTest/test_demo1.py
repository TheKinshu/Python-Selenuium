# Any pytest file should start with test_
# pytest function names should start with test

# You can run only 1 test at a time using the terminal command:
# py.test -k <function name> -v -s
# -k stands for function name execution
# -s logs in output
# -v stands for more info metadata

# You can mark certain functions and run only the mark tests
# @pytest.mark.<tag name>  
# -m
# py.test -m <tag name> -v -s

import pytest

@pytest.mark.xfail
def test_firstProgram():
    print('Hello')

@pytest.mark.smoke
def test_secondProgram():
    print('Morning')



def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])
