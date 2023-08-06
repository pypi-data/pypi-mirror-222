def test_delete_first(standalone_service):
    db, Service = standalone_service

    db.Service.new("1.1.1.1", 21, "tcp")
    assert len(db.Service) == 1

    db.Service.delete_first("1.1.1.1")
    assert len(db.Service) == 0

    db.Service.new("1.1.1.1", 21, "tcp")
    db.Service.new("2.2.2.2", 21, "tcp")

    db.Service.delete_first("2.2.2.2")

    assert len(db.Service) == 1
    assert db.Service.first_asdict()["ip"] == "1.1.1.1"


def test_delete_many(standalone_service):
    db, Service = standalone_service

    db.Service.new("1.1.1.1", 22, "tcp")
    db.Service.new("2.2.2.2", 21, "tcp")
    db.Service.new("3.3.3.3", 21, "tcp")

    assert len(db.Service) == 3

    db.Service.delete_many(port=21)
    assert len(db.Service) == 1
    assert db.Service.first_asdict()["ip"] == "1.1.1.1"
