from koalak.iterpaths.iterpaths import (
    EndswithNameFilter,
    RegexNameFilter,
    SearchNameFilter,
    StartswithNameFilter,
)


def test_plugin_search():
    plugin = SearchNameFilter("abc")
    assert plugin.filter("something_abc")
    assert not plugin.nofilter("something_abc")

    assert not plugin.filter("bc")
    assert plugin.nofilter("bc")

    # Insensitive: note it's the responsability of the core to lowercase the argument in filter
    #   and the responsability of the filters to lowercase the args in the init
    plugin = SearchNameFilter("ABC", insensitive=True)
    assert plugin.filter("something_abc")
    assert not plugin.nofilter("something_abc")

    assert not plugin.filter("bc")
    assert plugin.nofilter("bc")

    # Multiple keywords
    plugin = SearchNameFilter(["key1", "key2"])
    assert plugin.filter("something_key1_key2")
    assert not plugin.nofilter("something_key1_key2")

    assert not plugin.filter("something_key1")
    assert plugin.nofilter("something_key1")

    assert not plugin.filter("something")
    assert plugin.nofilter("something")

    # Multiple insensitive
    plugin = SearchNameFilter(["key1", "KEY2"], insensitive=True)
    assert plugin.filter("something_key1_key2")
    assert not plugin.nofilter("something_key1_key2")

    assert not plugin.filter("something_key1")
    assert plugin.nofilter("something_key1")

    assert not plugin.filter("something")
    assert plugin.nofilter("something")

    # Check details
    plugin = SearchNameFilter("abc")
    found, details = plugin.filter_with_details("something_abc", details=True)
    assert found is True
    assert details["positions"] == [(10, 13)]

    plugin = SearchNameFilter("abc")
    found, details = plugin.filter_with_details("something_abc_abc", details=True)
    assert found is True
    assert details["positions"] == [(10, 13), (14, 17)]

    plugin = SearchNameFilter(["key1", "k2"])
    found, details = plugin.filter_with_details("key1_k2", details=True)
    assert found is True
    assert details["positions"] == [(0, 4), (5, 7)]


def test_plugin_startswith():
    plugin = StartswithNameFilter("abc")
    assert plugin.filter("abc_something")
    assert not plugin.nofilter("abc_something")

    assert not plugin.filter("something_abc")
    assert plugin.nofilter("something_abc")

    assert not plugin.filter("nothing")
    assert plugin.nofilter("nothing")

    assert not plugin.filter("bla_abc_bla")
    assert plugin.nofilter("bla_abc_bla")

    # Insensitive: note it's the responsability of the core to lowercase the argument in filter
    #   and the responsability of the filters to lowercase the args in the init
    plugin = StartswithNameFilter("ABC", insensitive=True)
    assert plugin.filter("abc_something")
    assert not plugin.nofilter("abc_something")

    assert not plugin.filter("something_abc")
    assert plugin.nofilter("something_abc")

    assert not plugin.filter("nothing")
    assert plugin.nofilter("nothing")

    assert not plugin.filter("bla_abc_bla")
    assert plugin.nofilter("bla_abc_bla")

    # Multiple keywords
    plugin = StartswithNameFilter(["key1", "key2"])
    assert plugin.filter("key1_something")
    assert not plugin.nofilter("key1_something")

    assert plugin.filter("key2_something")
    assert not plugin.nofilter("key2_something")

    assert not plugin.filter("something_key1")
    assert plugin.nofilter("something_key1")

    assert not plugin.filter("nothing")
    assert plugin.nofilter("nothing")

    assert not plugin.filter("bla_key2_bla")
    assert plugin.nofilter("bla_key2_bla")

    # Multiple insensitive
    plugin = StartswithNameFilter(["key1", "KEY2"], insensitive=True)
    assert plugin.filter("key1_something")
    assert not plugin.nofilter("key1_something")

    assert plugin.filter("key2_something")
    assert not plugin.nofilter("key2_something")

    assert not plugin.filter("something_key1")
    assert plugin.nofilter("something_key1")

    assert not plugin.filter("nothing")
    assert plugin.nofilter("nothing")

    assert not plugin.filter("bla_key2_bla")
    assert plugin.nofilter("bla_key2_bla")

    # Check details
    plugin = StartswithNameFilter("abc")
    found, details = plugin.filter_with_details("abc_something", details=True)
    assert found is True
    assert details["positions"] == [(0, 3)]

    plugin = StartswithNameFilter(["key", "key_long"])
    found, details = plugin.filter_with_details("key_long", details=True)
    assert found is True
    assert details["positions"] == [(0, 3), (0, 8)]


def test_plugin_endswith():
    plugin = EndswithNameFilter("abc")
    assert plugin.filter("something_abc")
    assert not plugin.nofilter("something_abc")

    assert not plugin.filter("abc_something")
    assert plugin.nofilter("abc_something")

    assert not plugin.filter("nothing")
    assert plugin.nofilter("nothing")

    assert not plugin.filter("bla_abc_bla")
    assert plugin.nofilter("bla_abc_bla")

    # Insensitive: note it's the responsability of the core to lowercase the argument in filter
    #   and the responsability of the filters to lowercase the args in the init
    plugin = EndswithNameFilter("ABC", insensitive=True)
    assert plugin.filter("something_abc")
    assert not plugin.nofilter("something_abc")

    assert not plugin.filter("abc_something")
    assert plugin.nofilter("abc_something")

    assert not plugin.filter("nothing")
    assert plugin.nofilter("nothing")

    assert not plugin.filter("bla_abc_bla")
    assert plugin.nofilter("bla_abc_bla")

    # Multiple keywords
    plugin = EndswithNameFilter(["key1", "key2"])
    assert plugin.filter("something_key1")
    assert not plugin.nofilter("something_key1")

    assert plugin.filter("something_key2")
    assert not plugin.nofilter("something_key2")

    assert not plugin.filter("key1_something")
    assert plugin.nofilter("key1_something")

    assert not plugin.filter("nothing")
    assert plugin.nofilter("nothing")

    assert not plugin.filter("bla_key2_bla")
    assert plugin.nofilter("bla_key2_bla")

    # Multiple insensitive
    plugin = EndswithNameFilter(["key1", "KEY2"], insensitive=True)
    assert plugin.filter("something_key1")
    assert not plugin.nofilter("something_key1")

    assert plugin.filter("something_key2")
    assert not plugin.nofilter("something_key2")

    assert not plugin.filter("key1_something")
    assert plugin.nofilter("key1_something")

    assert not plugin.filter("nothing")
    assert plugin.nofilter("nothing")

    assert not plugin.filter("bla_key2_bla")
    assert plugin.nofilter("bla_key2_bla")

    # Check details
    plugin = EndswithNameFilter("abc")
    found, details = plugin.filter_with_details("_abc", details=True)
    assert found is True
    assert details["positions"] == [(1, 4)]

    plugin = EndswithNameFilter(["key", "long_key"])
    found, details = plugin.filter_with_details("_long_key", details=True)
    assert found is True
    assert details["positions"] == [(6, 9), (1, 9)]


def test_plugin_regex_simple():
    plugin = RegexNameFilter("abc")
    assert plugin.filter("something_abc")
    assert not plugin.nofilter("something_abc")

    assert not plugin.filter("bc")
    assert plugin.nofilter("bc")

    # Insensitive: note it's the responsability of the core to lowercase the argument in filter
    #   and the responsability of the filters to lowercase the args in the init
    plugin = RegexNameFilter("ABC", insensitive=True)
    assert plugin.filter("something_abc")
    assert not plugin.nofilter("something_abc")

    assert not plugin.filter("bc")
    assert plugin.nofilter("bc")

    # Multiple keywords
    plugin = RegexNameFilter(["key1", "key2"])
    assert plugin.filter("something_key1_key2")
    assert not plugin.nofilter("something_key1_key2")

    assert not plugin.filter("something_key1")
    assert plugin.nofilter("something_key1")

    assert not plugin.filter("something")
    assert plugin.nofilter("something")

    # Multiple insensitive
    plugin = RegexNameFilter(["key1", "KEY2"], insensitive=True)
    assert plugin.filter("something_key1_key2")
    assert not plugin.nofilter("something_key1_key2")

    assert not plugin.filter("something_key1")
    assert plugin.nofilter("something_key1")

    assert not plugin.filter("something")
    assert plugin.nofilter("something")

    # Check details
    plugin = RegexNameFilter("abc")
    found, details = plugin.filter_with_details("something_abc", details=True)
    assert found is True
    assert details["positions"] == [(10, 13)]

    plugin = RegexNameFilter("abc")
    found, details = plugin.filter_with_details("something_abc_abc", details=True)
    assert found is True
    assert details["positions"] == [(10, 13), (14, 17)]

    plugin = RegexNameFilter(["key1", "k2"])
    found, details = plugin.filter_with_details("key1_k2", details=True)
    assert found is True
    assert details["positions"] == [(0, 4), (5, 7)]


def test_plugin_regex_with_regex():
    plugin = RegexNameFilter("k1|k2")
    assert plugin.filter("something_k1")
    assert not plugin.nofilter("something_k1")

    assert plugin.filter("something_k2")
    assert not plugin.nofilter("something_k2")

    assert plugin.filter("something_k1_k2")
    assert not plugin.nofilter("something_k1_k2")

    plugin = RegexNameFilter("k1|k2")
    found, details = plugin.filter_with_details("k1_k2", details=True)
    assert found is True
    assert details["positions"] == [(0, 2), (3, 5)]


# TODO: test Duplicates
