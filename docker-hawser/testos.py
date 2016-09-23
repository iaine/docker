from nose.tools import assert_true, assert_false

import os

from operating_sys import OS_Environment

def test_found_os_name():
    _os = OS_Environment().get_os_name()
    assert_true(_os == "Linux")

def test_found_os_build():
    _os = OS_Environment().get_os_build()
    assert_true("Ubuntu" in _os)

def test_not_found_os_build():
    _os = OS_Environment().get_os_build()
    assert_false("OSX" in _os)

def test_expect_generic_os_kernel():
    _os = OS_Environment().get_os_kernel()
    assert_true("generic" in _os)

def test_os_kernel_is_not_none():
    _os = OS_Environment().get_os_kernel()
    assert_false(_os is None)

def test_os_architecture_x86():
    _os = OS_Environment().get_os_arch()
    assert_true(_os == "x86_64")
