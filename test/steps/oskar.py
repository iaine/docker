from behave import given, when, then
import os

dirname = "/home/iain/git/docker/oskar/"
fname = "Dockerfile"
@given(u'that I have a build directory "{directory}"')
def step_impl(context, directory):
    pass

@when(u'I create "{dfile}"')
def step_impl(context, dfile):
    pass

@then(u'I have the base installation file')
def step_impl(context):
    assert os.path.isfile(dirname + fname) is True    
