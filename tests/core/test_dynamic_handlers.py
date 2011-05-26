#!/usr/bin/env python

import pytest

from circuits import handler, Component, Event, Manager

class Foo(Event):
    """Foo Event"""

@handler("foo")
def on_foo(self):
    return "Hello World!"

def test_addHandler():
    m = Manager()
    m.start()

    m.addHandler(on_foo)

    x = m.fire(Foo())

    pytest.wait_event(m, "foo")

    s = x.value[0]
    assert s == "Hello World!"

    m.stop()


def test_removeHandler():
    m = Manager()
    m.start()

    m.addHandler(on_foo)

    x = m.fire(Foo())

    pytest.wait_event(m, "foo")

    s = x.value[0]
    assert s == "Hello World!"

    m.removeHandler(on_foo)

    x = m.fire(Foo())

    pytest.wait_event(m, "foo")

    assert x.value is None

    assert on_foo not in dir(m)
    assert len(m._handlers["foo"]) == 0

    m.stop()
