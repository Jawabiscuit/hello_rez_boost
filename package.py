# -*- coding: utf-8 -*-

name = "hello_boost"

description = "A rez package which contains a small bit of code from Boost's getting started page for testing a new boost installation or trying out boost for the first time."

help = "https://www.boost.org"

version = "0.1.0"

uuid = "examples.{}-{}".format(name, version)


@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "os-**"]
    return [expand_requires(*requires)]


@early()
def private_build_requires():
    import os

    if os.name == "nt":
        return ["msvc-14+<15"]


def commands():
    import os

    env.PATH.append(os.path.join("{root}"))
