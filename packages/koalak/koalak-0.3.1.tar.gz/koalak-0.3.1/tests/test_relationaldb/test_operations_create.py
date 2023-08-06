import pytest


def test_insert_one(standalone_service):
    db, Service = standalone_service

    assert len(db.Service) == 0

    db.Service.insert_one("1.1.1.1", 21, "tcp")

    assert len(db.Service) == 1
    service = db.Service.first_asdict()

    assert isinstance(service, dict)
    assert service["ip"] == "1.1.1.1"
    assert service["port"] == 21
    assert service["protocol"] == "tcp"
    # FIXME: add service and version as None?

    db.Service.insert_one("1.1.1.1", 21, "tcp")

    assert len(db.Service) == 2
    service, service2 = list(db.Service.find_asdict())

    assert isinstance(service, dict)
    assert service["ip"] == "1.1.1.1"
    assert service["port"] == 21
    assert service["protocol"] == "tcp"

    assert isinstance(service2, dict)
    assert service2["ip"] == "1.1.1.1"
    assert service2["port"] == 21
    assert service2["protocol"] == "tcp"


def test_insert_one_with_entity_name(standalone_services):
    db, Service = standalone_services

    assert len(db.services) == 0
    # Service in db always exists?
    assert db.services is db.Service

    db.services.insert_one("1.1.1.1", 21, "tcp")

    assert len(db.services) == 1
    service = db.services.first_asdict()

    assert isinstance(service, dict)
    assert service["ip"] == "1.1.1.1"
    assert service["port"] == 21
    assert service["protocol"] == "tcp"
    # FIXME: add service and version as None?

    db.services.insert_one("1.1.1.1", 21, "tcp")

    assert len(db.services) == 2
    service, service2 = list(db.services.find_asdict())

    assert isinstance(service, dict)
    assert service["ip"] == "1.1.1.1"
    assert service["port"] == 21
    assert service["protocol"] == "tcp"

    assert isinstance(service2, dict)
    assert service2["ip"] == "1.1.1.1"
    assert service2["port"] == 21
    assert service2["protocol"] == "tcp"


def test_insert_one_one_to_many(service_host):
    db, Service, Host = service_host

    assert len(db.Service) == 0
    assert len(db.Host) == 0

    # Create host
    db.Host.insert_one("1.1.1.1")
    host_obj = db.Host.first()

    assert len(db.Host) == 1

    # Create New service with host (Will not insert a new host)
    db.Service.insert_one(host_obj, 21, "tcp")
    assert len(db.Host) == 1
    assert len(db.Service) == 1

    service = db.Service.first_asdict()
    host = db.Host.first_asdict()

    assert isinstance(service, dict)
    assert service["host"]  # Don't know yet what to put here
    assert service["port"] == 21
    assert service["protocol"] == "tcp"

    assert isinstance(host, dict)
    assert host["ip"] == "1.1.1.1"

    # Create new service with same host do nothing to host
    db.Service.insert_one(host_obj, 21, "tcp")
    assert len(db.Host) == 1
    assert len(db.Service) == 2

    service, service2 = list(db.Service.find_asdict())
    host = db.Host.first_asdict()

    assert isinstance(service, dict)
    assert service["host"]  # Don't know yet what to put here
    assert service["port"] == 21
    assert service["protocol"] == "tcp"

    assert isinstance(service2, dict)
    assert service2["host"]  # Don't know yet what to put here
    assert service2["port"] == 21
    assert service2["protocol"] == "tcp"

    assert isinstance(host, dict)
    assert host["ip"] == "1.1.1.1"

    with pytest.raises(TypeError):
        # Insert must be with the object not the String
        db.Service.insert_one("1.1.1.1", 21, "tcp")
