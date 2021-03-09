# Any pytest file should start with test_
# pytest function names should start with test

# You can run only 1 test at a time using the terminal command:
# py.test -k <function name> -v -s
# -k stands for function name execution
# -s logs in output
# -v stands for more info metadata

# You can mark certain functions and run only the mark tests
# @pytest.mark.<tag name>  This creates a custom mark
# -m
# py.test -m <tag name> -v -s

# There are pre-existing marks, Ex:
# @pytest.mark.skip This skips the marked test
# @pytest.mark.xfail

import pytest

@pytest.mark.smoke
@pytest.mark.xfail
def test_thirdProgram():
    msg = 'Hello'
    # Create your own assertion message by using a comma
    assert msg == 'Hi', 'Tetst failed because strings do not match'

@pytest.mark.skip
def test_fourthProgram():
    a = 4
    b = 2
    assert a + b == 6, 'Addition does not match'

def test_fixtureDemo(setup):
    print('I will execute steps in fixture demo function')
