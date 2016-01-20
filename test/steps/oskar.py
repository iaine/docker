from behave import given, when, then
import os

import steps.docker

dirname = "/home/iain/git/docker/oskar/"
fname = "Dockerfile"
imagename = "oskar"
package = "oskar"

@given(u'that I have a build directory "{directory}"')
def step_impl(context, directory):
    pass

@when(u'I create "{dfile}"')
def step_impl(context, dfile):
    pass

@then(u'I have the base installation file')
def step_impl(context):
    assert os.path.isfile(dirname + fname) is True  

@given(u'that I have a Docker image called "{imagename}"')
def step_impl(context, imagename):
    pass

@when(u'I have installed the "{package}" package')
def step_impl(context, package):
    pass

@then(u'I can query the image to see that it is loaded')
def step_impl(context):
    bdd = steps.docker.BDDDocker(imagename)
    assert bdd.system_package(package) is True
