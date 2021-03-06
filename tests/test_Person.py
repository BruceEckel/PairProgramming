import sys
import pytest
from teamup.Person import Person
from teamup.pairings import People

# with capsys.disabled():


def test_empty(capsys):
    with pytest.raises(AssertionError):
        Person("")
    with pytest.raises(AssertionError):
        Person(" ")


def test_single_name(capsys):
    with pytest.raises(AssertionError):
        Person("Bob")


def test_duplicate_name(capsys):
    with pytest.raises(AssertionError):
        People().add_list(["Bob Dobbs", "Bob Dobbs"])


def test_basic(capsys):
    assert Person("bruce eckel") == Person("Bruce Eckel")
    assert Person("Bruce eckel") == Person("Bruce Eckel")
    assert Person("bruce Eckel") == Person("Bruce Eckel")
    assert Person("bruce eckel") == "Bruce Eckel"
    assert Person("Bruce eckel") == "Bruce Eckel"
    assert Person("bruce Eckel") == "Bruce Eckel"
