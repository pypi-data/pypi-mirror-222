from koalak.iterpaths import iterpaths


def test_import():
    from koalak.all import iterpaths as _iterpaths

    assert _iterpaths is iterpaths
