import pytest
from koalak.relationaldb import Conceptor, field


def test_feed_errors(standalone_persons):
    db, Person = standalone_persons
    db.persons.insert_one("John", "Smith")
    with pytest.raises(ValueError):
        db.persons.feed("John", "Smith")
