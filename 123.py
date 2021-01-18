import pytest,yaml
def add_function(a,b):
    return a+b
@pytest.mark.parametrize("a,b,expected",
                         [yaml.safe_load(open("./data.yml"))["add"]])
def test_add(a,b,expected):
    assert add_function(a,b) == expected