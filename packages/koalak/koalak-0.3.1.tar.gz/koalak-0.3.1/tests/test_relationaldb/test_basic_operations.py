def test_simple_dbobjects_with_name_have_alias_named_with_clsname(standalone_services):
    db, Service = standalone_services
    assert db.Service is db.services
    assert db.Service is not Service
