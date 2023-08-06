import pytest
from koalak.list_of_dict import ListOfDict


def test_import_from_all():
    from koalak.all import ListOfDict as _ListOfDict

    assert ListOfDict is _ListOfDict


@pytest.fixture
def list_of_dict():
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
        {"name": "Alice", "age": 40},
        {"name": "Foo", "age": 35},
    ]


@pytest.mark.parametrize(
    "params, expected",
    [
        ({"name": "Alice"}, {"name": "Alice", "age": 30}),
        ({"name": "Bob"}, {"name": "Bob", "age": 25}),
        ({"age": 25}, {"name": "Bob", "age": 25}),
        ({}, {"name": "Alice", "age": 30}),
    ],
)
def test_first(list_of_dict, params, expected):
    data = ListOfDict(list_of_dict)
    assert data.first(params) == expected
    assert data.first(**params) == expected
    if params:
        with pytest.raises(ValueError):
            data.first(params, **params)


def test_first_no_match_found(list_of_dict):
    data = ListOfDict(list_of_dict)
    with pytest.raises(ValueError):
        data.first(name="Eve")
    with pytest.raises(ValueError):
        data.first({"name": "Eve"})


@pytest.mark.parametrize(
    "params, expected",
    [
        (
            {},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {"name": "Alice"},
            [
                {"name": "Alice", "age": 30},
                {"name": "Alice", "age": 40},
            ],
        ),
        (
            {"name": "Bob"},
            [
                {"name": "Bob", "age": 25},
            ],
        ),
        (
            {"age": 25},
            [
                {"name": "Bob", "age": 25},
            ],
        ),
        ({"name": "Eve"}, []),
    ],
)
def test_filter(list_of_dict, params, expected):
    data = ListOfDict(list_of_dict)

    # Test with params
    assert list(data.filter(params)) == expected
    # Test with kwargs
    assert list(data.filter(**params)) == expected
    # Test with both params and kwargs (should raise ValueError)
    if params:
        with pytest.raises(ValueError):
            data.filter(params, **params)


@pytest.mark.parametrize(
    "filter_query, update_query, expected",
    [
        (
            {"name": "Alice"},
            {"age": 50},
            [
                {"name": "Alice", "age": 50},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 50},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {"name": "Alice", "age": 30},
            {"age": 50},
            [
                {"name": "Alice", "age": 50},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {"age": 25},
            {"name": "John"},
            [
                {"name": "Alice", "age": 30},
                {"name": "John", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {"name": "Eve"},
            {"age": 50},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {"name": "Alice"},
            {},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
    ],
)
def test_update(list_of_dict, filter_query, update_query, expected):
    data = ListOfDict(list_of_dict)
    data.update(filter_query, update_query)
    assert data.data == expected


def test_count(list_of_dict):
    data = ListOfDict(list_of_dict)

    # Test with params
    tests = [
        ({}, 5),
        ({"name": "Alice"}, 2),
        ({"name": "Bob"}, 1),
        ({"age": 25}, 1),
        ({"name": "Eve"}, 0),
    ]

    for params, expected in tests:
        # Test with params
        assert data.count(params) == expected
        # Test with kwargs
        assert data.count(**params) == expected
        # Test with both params and kwargs (should raise ValueError, but not for an empty dictionary)
        if params:
            with pytest.raises(ValueError):
                data.count(params, **params)
    # Test with invalid kwargs
    with pytest.raises(ValueError):
        data.count({"name": "Alice"}, age=30)


def test_sum(list_of_dict):
    data = ListOfDict(list_of_dict)
    assert data.sum("age") == 165
    assert data.sum("age", name="Alice") == 70
    assert data.sum("age", name="Eve") == 0


@pytest.mark.parametrize(
    "filter_query, update_query, expected",
    [
        (
            {"name": "Alice", "age": 40},
            {"age": 31},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 31},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {"name": "Alice"},
            {"age": 31},
            [
                {"name": "Alice", "age": 31},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {"age": 35},
            {"age": 36},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 36},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {"name": "Eve"},
            {"age": 31},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
    ],
)
def test_update_first(list_of_dict, filter_query, update_query, expected):
    data = ListOfDict(list_of_dict)
    data.update_first(filter_query, update_query)
    assert data.data == expected


@pytest.mark.parametrize(
    "params,expected",
    [
        (
            {"name": "Alice"},
            [
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {"name": "Foo"},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
            ],
        ),
        (
            {"age": 35},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {"name": "Eve"},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {},
            [
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
    ],
)
def test_delete_first(list_of_dict, params, expected):
    data = ListOfDict(list_of_dict, deepcopy=True)

    # Test with params
    data.delete_first(params)
    assert data.data == expected

    # Test with kwargs
    data = ListOfDict(list_of_dict, deepcopy=True)
    data.delete_first(**params)
    assert data.data == expected

    # Test with both params and kwargs (should raise ValueError)
    if params:
        with pytest.raises(ValueError):
            data.delete_first(params, **params)


@pytest.mark.parametrize(
    "filter_query, expected_result",
    [
        (
            {"name": "Alice"},
            [
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Foo", "age": 35},
            ],
        ),
        (
            {"name": "Foo"},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
            ],
        ),
        (
            {"age": 35},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Alice", "age": 40},
            ],
        ),
        (
            {"name": "Eve"},
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35},
                {"name": "Alice", "age": 40},
                {"name": "Foo", "age": 35},
            ],
        ),
    ],
)
def test_delete(filter_query, expected_result, list_of_dict):
    data = ListOfDict(list_of_dict, deepcopy=True)
    data.delete(**filter_query)
    assert data.data == expected_result

    data = ListOfDict(list_of_dict, deepcopy=True)
    data.delete(filter_query)
    assert data.data == expected_result

    if filter_query:
        with pytest.raises(ValueError):
            data.delete_first(filter_query, **filter_query)


def test_sort(list_of_dict):
    data = ListOfDict(list_of_dict)
    data.sort("age")
    assert data.data == [
        {"name": "Bob", "age": 25},
        {"name": "Alice", "age": 30},
        {"name": "Charlie", "age": 35},
        {"name": "Foo", "age": 35},
        {"name": "Alice", "age": 40},
    ]
    data.sort("name", "age", reverse=True)
    assert data.data == [
        {"name": "Foo", "age": 35},
        {"name": "Charlie", "age": 35},
        {"name": "Bob", "age": 25},
        {"name": "Alice", "age": 40},
        {"name": "Alice", "age": 30},
    ]


def test_group_by(list_of_dict):
    data = ListOfDict(list_of_dict)
    result = data.group_by("name")
    assert len(result) == 4
    assert set(result.keys()) == {("Alice",), ("Bob",), ("Charlie",), ("Foo",)}
    assert len(result[("Alice",)]) == 2
    assert result[("Alice",)][0] == {"name": "Alice", "age": 30}
    assert result[("Alice",)][1] == {"name": "Alice", "age": 40}
    assert len(result[("Bob",)]) == 1
    assert result[("Bob",)][0] == {"name": "Bob", "age": 25}
    assert len(result[("Charlie",)]) == 1
    assert result[("Charlie",)][0] == {"name": "Charlie", "age": 35}
    assert len(result[("Foo",)]) == 1
    assert result[("Foo",)][0] == {"name": "Foo", "age": 35}


def test_merge(list_of_dict):
    data1 = ListOfDict(list_of_dict[:2])
    data2 = ListOfDict(list_of_dict[2:])
    result = data1.merge(data2)
    assert isinstance(result, ListOfDict)
    assert len(result.data) == 5
    assert result.data[0] == {"name": "Alice", "age": 30}
    assert result.data[1] == {"name": "Bob", "age": 25}
    assert result.data[2] == {"name": "Charlie", "age": 35}
    assert result.data[3] == {"name": "Alice", "age": 40}
    assert result.data[4] == {"name": "Foo", "age": 35}


def test_count_values(list_of_dict):
    data = ListOfDict(list_of_dict)
    result = data.count_values("name")
    assert len(result) == 4
    assert result["Alice"] == 2
    assert result["Bob"] == 1
    assert result["Charlie"] == 1
    assert result["Foo"] == 1


def test_unique():
    list_of_dict = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},  # duplicate
        {"name": "Charlie", "age": 35},
        {"name": "Alice", "age": 40},
        {"name": "Foo", "age": 35},
        {"name": "Bob", "age": 25},  # duplicate
        {"name": "Charlie", "age": 35},  # duplicate
        {"name": "Bar", "age": 30},
        {"name": "Baz", "age": 25},
    ]

    data = ListOfDict(list_of_dict)
    result = data.unique()
    assert isinstance(result, ListOfDict)
    assert len(result) == 7
    assert result.data == [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},  # duplicate
        {"name": "Charlie", "age": 35},
        {"name": "Alice", "age": 40},
        {"name": "Foo", "age": 35},
        {"name": "Bar", "age": 30},
        {"name": "Baz", "age": 25},
    ]


def test_len(list_of_dict):
    data = ListOfDict(list_of_dict)
    assert len(data) == 5


def test_getitem(list_of_dict):
    data = ListOfDict(list_of_dict)
    assert data[0] == {"name": "Alice", "age": 30}
    assert data[1] == {"name": "Bob", "age": 25}
    assert data[-1] == {"name": "Foo", "age": 35}


def test_iter(list_of_dict):
    data = ListOfDict(list_of_dict)
    assert list(data) == list_of_dict


def test_eq(list_of_dict):
    data1 = ListOfDict(list_of_dict)
    data2 = ListOfDict(list_of_dict)
    assert data1 == data2

    data3 = ListOfDict([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}])
    assert data1 != data3


def test_repr(list_of_dict):
    data = ListOfDict(list_of_dict)
    assert (
        repr(data)
        == "ListOfDict([{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}, {'name': 'Alice', 'age': 40}, {'name': 'Foo', 'age': 35}])"
    )


def test_str(list_of_dict):
    data = ListOfDict(list_of_dict)
    assert (
        str(data)
        == "[{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}, {'name': 'Alice', 'age': 40}, {'name': 'Foo', 'age': 35}]"
    )
