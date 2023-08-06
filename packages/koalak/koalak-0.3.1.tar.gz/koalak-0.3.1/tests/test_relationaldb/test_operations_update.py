def test_feed(standalone_service):
    db, Service = standalone_service

    assert len(db.Service) == 0

    for _ in range(3):
        # Repeating the same feed operation should not change the db state
        db.Service.feed("1.1.1.1", 21, "tcp")
        assert len(db.Service) == 1

        service = db.Service.first_asdict()

        assert isinstance(service, dict)
        assert service["ip"] == "1.1.1.1"
        assert service["port"] == 21
        assert service["protocol"] == "tcp"
        # FIXME: add service and version as None?

    for _ in range(3):
        # Repeating the same upsert operation should not change the db state
        db.Service.feed("1.1.1.1", 21, "tcp", service="ftp")
        assert len(db.Service) == 1

        service = db.Service.first_asdict()

        assert isinstance(service, dict)
        assert service["ip"] == "1.1.1.1"
        assert service["port"] == 21
        assert service["protocol"] == "tcp"
        assert service["service"] == "ftp"

    for _ in range(3):
        # Repeating the same upsert operation should not change the db state
        db.Service.feed("1.1.1.1", 22, "tcp", service="ssh")
        assert len(db.Service) == 2

        service = db.Service.first_asdict()

        assert isinstance(service, dict)
        assert service["ip"] == "1.1.1.1"
        assert service["port"] == 21
        assert service["protocol"] == "tcp"
        assert service["service"] == "ftp"

        service = db.Service.index_asdict(1)

        assert isinstance(service, dict)
        assert service["ip"] == "1.1.1.1"
        assert service["port"] == 22
        assert service["protocol"] == "tcp"
        assert service["service"] == "ssh"


def test_feed_relation_one_to_many(service_host):
    db, Service, Host = service_host

    assert len(db.Service) == 0
    assert len(db.Host) == 0

    # First create the host
    db.Host.feed("1.1.1.1")

    for _ in range(3):
        # Repeating the same feed operation should not change the db state
        db.Service.feed("1.1.1.1", 21, "tcp")

        assert len(db.Service) == 1
        assert len(db.Host) == 1  # will not create another host

        service = db.Service.first_asdict()
        host = db.Host.first_asdict()

        assert isinstance(service, dict)
        assert service["host"]  # Don't know yet what to put here
        assert service["port"] == 21
        assert service["protocol"] == "tcp"

        assert isinstance(host, dict)
        assert host["ip"] == "1.1.1.1"
        # FIXME: add service and version as None?

    for _ in range(3):
        # Repeating the same upsert operation should not change the db state
        db.Service.feed("1.1.1.1", 21, "tcp", service="ftp")
        assert len(db.Service) == 1
        assert len(db.Host) == 1  # will not create another host

        service = db.Service.first_asdict()
        host = db.Host.first_asdict()

        assert isinstance(service, dict)
        assert service["host"]  # Don't know yet what to put here
        assert service["port"] == 21
        assert service["protocol"] == "tcp"
        assert service["service"] == "ftp"

        assert isinstance(host, dict)
        assert host["ip"] == "1.1.1.1"

    for _ in range(3):
        # Adding port in same host
        db.Service.feed("1.1.1.1", 22, "tcp", service="ssh")

        assert len(db.Service) == 2
        assert len(db.Host) == 1  # will not create another host

        service = db.Service.first_asdict()
        service2 = db.Service.first_asdict(service="ssh")
        host = db.Host.first_asdict()

        assert isinstance(service, dict)
        assert service["host"]  # Don't know yet what to put here
        assert service["port"] == 21
        assert service["protocol"] == "tcp"
        assert service["service"] == "ftp"

        assert isinstance(host, dict)
        assert host["ip"] == "1.1.1.1"

        assert isinstance(service2, dict)
        assert service2["host"]  # Don't know yet what to put here
        assert service2["port"] == 22
        assert service2["protocol"] == "tcp"
        assert service2["service"] == "ssh"

    # Testing with none existing host
    # ===============================
    for _ in range(3):
        # Adding port in same host
        db.Service.feed("2.2.2.2", 23, "tcp", service="telnet")

        assert len(db.Service) == 3
        assert len(db.Host) == 2

        service = db.Service.first_asdict()
        service2 = db.Service.first_asdict(service="ssh")
        service3 = db.Service.first_asdict(service="telnet")
        host = db.Host.first_asdict()
        host2 = db.Host.first_asdict("2.2.2.2")

        assert isinstance(service, dict)
        assert service["host"]  # Don't know yet what to put here
        assert service["port"] == 21
        assert service["protocol"] == "tcp"
        assert service["service"] == "ftp"

        assert isinstance(host, dict)
        assert host["ip"] == "1.1.1.1"

        assert isinstance(host2, dict)
        assert host2["ip"] == "2.2.2.2"

        assert isinstance(service2, dict)
        assert service2["host"]  # Don't know yet what to put here
        assert service2["port"] == 22
        assert service2["protocol"] == "tcp"
        assert service2["service"] == "ssh"

        assert isinstance(service3, dict)
        assert service3["host"]  # Don't know yet what to put here
        assert service3["port"] == 23
        assert service3["protocol"] == "tcp"
        assert service3["service"] == "telnet"
