# Conftest is an utility file to help run pytest.
# It enables you to create a function that can be -
# use in multiple and different files/functions.
# This optimize the code and create less clutter

import pytest

# Fixtures are used as setup
# By using scope you are restricting this -
# fixture to a class level execution
@pytest.fixture(scope='class')
def setup():
    print('I will be executing first')
    yield
    print('I will be executed last')


@pytest.fixture()
def dataLoad():
    print('user profule data is being created')
    return ['Kelvin', 'Cho', 'github.com/TheKinshu/']

# Tuple: A immutable list
# Passing Tuples as a param to other function by passing them as parameters
@pytest.fixture(params=[('Chrome', 'Kelvin'), ('Firefox', 'Cho'), ('IE', 'SS')])
def crossBrowser(request):
    return request.param
