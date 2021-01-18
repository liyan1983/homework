import pytest
import yaml
def add_function(a,b):
    return a+b
def sub_function(a,b):
    return a-b
def mul_function(a,b):
    return a*b
def div_function(a,b):
    return a/b

@pytest.mark.parametrize("a,b,expect",
                         [yaml.safe_load(open("./data.yml"))["add"]],
                         ids=["add"])
def test_add(a,b,expect):
    assert add_function(a,b)==expect
@pytest.mark.parametrize("a,b,expect",
                         [yaml.safe_load(open("./data.yml"))["sub"]],
                         ids=["sub"])
def test_sub(a,b,expect):
    assert sub_function(a,b)==expect
@pytest.mark.parametrize("a,b,expect",
                         [yaml.safe_load(open("./data.yml"))["mul"]],
                         ids=["mul"])
def test_mul(a,b,expect):
    assert mul_function(a,b)==expect
@pytest.mark.parametrize("a,b,expect",
                         [yaml.safe_load(open("./data.yml"))["div"]],
                         ids=["div"])
def test_div(a,b,expect):
    assert div_function(a,b)==expect

