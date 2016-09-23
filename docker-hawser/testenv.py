from nose.tools import assert_true, assert_false

from operating_sys import Container_Environment

def test_found_Dokcer_version():
    _dock = Container_Environment().get_docker_version
    assert_true(_dock, '1.12.1')
