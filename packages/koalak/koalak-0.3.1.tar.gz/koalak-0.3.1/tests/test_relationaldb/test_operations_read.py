def test_first_entity(standalone_service):
    db, Service = standalone_service

    db.Service.new("1.1.1.1", 21, "tcp")
    service = db.Service.first()

    assert isinstance(service, Service)
    assert service.ip == "1.1.1.1"
    assert service.port == 21
    assert service.protocol == "tcp"

    db.Service.new("2.2.2.2", 22, "tcp")
    service = db.Service.first()
    assert isinstance(service, Service)
    assert service.ip == "1.1.1.1"
    assert service.port == 21
    assert service.protocol == "tcp"

    service = db.Service.first(port=22)
    assert isinstance(service, Service)
    assert service.ip == "2.2.2.2"
    assert service.port == 22
    assert service.protocol == "tcp"


def test_first_asdict_entity(standalone_service):
    db, Service = standalone_service

    db.Service.new("1.1.1.1", 21, "tcp")
    service = db.Service.first_asdict()

    assert isinstance(service, dict)
    assert service["ip"] == "1.1.1.1"
    assert service["port"] == 21
    assert service["protocol"] == "tcp"

    db.Service.new("2.2.2.2", 22, "tcp")
    service = db.Service.first_asdict()
    assert isinstance(service, dict)
    assert service["ip"] == "1.1.1.1"
    assert service["port"] == 21
    assert service["protocol"] == "tcp"

    service = db.Service.first_asdict(port=22)
    assert isinstance(service, dict)
    assert service["ip"] == "2.2.2.2"
    assert service["port"] == 22
    assert service["protocol"] == "tcp"


def test_length_of_entity(standalone_service):
    db, Service = standalone_service

    assert len(db.Service) == 0

    db.Service.new("1.1.1.1", 21, "tcp")
    assert len(db.Service) == 1

    db.Service.new("1.1.1.1", 22, "tcp")
    assert len(db.Service) == 2


def test_indexing_list_asdict_entity(standalone_service):
    db, Service = standalone_service

    db.Service.new("1.1.1.1", 21, "tcp")
    db.Service.new("2.2.2.2", 22, "tcp")

    service = db.Service.index_asdict(0)

    assert isinstance(service, dict)
    assert service["ip"] == "1.1.1.1"
    assert service["port"] == 21
    assert service["protocol"] == "tcp"

    service = db.Service.index_asdict(1)

    assert isinstance(service, dict)
    assert service["ip"] == "2.2.2.2"
    assert service["port"] == 22
    assert service["protocol"] == "tcp"


def test_indexing_list_entity(standalone_service):
    db, Service = standalone_service

    db.Service.new("1.1.1.1", 21, "tcp")
    db.Service.new("1.1.1.1", 22, "tcp")

    service = db.Service[0]

    assert isinstance(service, Service)
    assert service.ip == "1.1.1.1"
    assert service.port == 21
    assert service.protocol == "tcp"

    service = db.Service[1]

    assert isinstance(service, Service)
    assert service.ip == "1.1.1.1"
    assert service.port == 22
    assert service.protocol == "tcp"


def test_iter_entity(standalone_service):
    db, Service = standalone_service

    db.Service.new("1.1.1.1", 21, "tcp")
    db.Service.new("1.1.1.1", 22, "tcp")

    services = list(db.Service)

    service = services[0]
    assert isinstance(service, Service)
    assert service.ip == "1.1.1.1"
    assert service.port == 21
    assert service.protocol == "tcp"

    service = services[1]

    assert isinstance(service, Service)
    assert service.ip == "1.1.1.1"
    assert service.port == 22
    assert service.protocol == "tcp"


# ======= #
# FILTERS #
# ======= #


def test_filter_by_attribute(standalone_service):
    db, Service = standalone_service

    for port in range(10, 20):
        db.Service.new("1.1.1.1", port, "tcp")
        db.Service.new("1.1.1.1", port, "udp")

    assert len(db.Service) == 20

    tcp_services = list(db.Service.find_asdict(protocol="tcp"))
    assert len(tcp_services) == 10
    for service in tcp_services:
        assert service["protocol"] == "tcp"

    port_12_services = list(db.Service.find_asdict(port=12))
    assert len(port_12_services) == 2
    for service in port_12_services:
        assert service["port"] == 12

    assert len(list(db.Service.find_asdict(port=10, protocol="tcp"))) == 1


# =========== #
# ONE TO MANY #
# =========== #
def test_read_detailed_find_asdict(service_host):
    db, Service, Host = service_host

    assert len(db.Service) == 0
    assert len(db.Host) == 0

    # First create the host
    db.Service.feed("1.1.1.1", 21, "tcp")
    db.Service.feed("2.2.2.2", 22, "tcp")

    detailed_services = list(db.Service.detailed_find_asdict())
    assert len(detailed_services) == 2

    detailed_service = detailed_services[0]
    assert isinstance(detailed_service, dict)
    assert detailed_service["port"] == 21
    assert detailed_service["protocol"] == "tcp"
    host_dict = detailed_service["host"]
    assert host_dict["ip"] == "1.1.1.1"

    detailed_service = detailed_services[1]
    assert isinstance(detailed_service, dict)
    assert detailed_service["port"] == 22
    assert detailed_service["protocol"] == "tcp"
    host_dict = detailed_service["host"]
    assert host_dict["ip"] == "2.2.2.2"

    # Search with port
    detailed_services = list(db.Service.detailed_find_asdict(port=22))
    assert len(detailed_services) == 1

    detailed_service = detailed_services[0]
    assert isinstance(detailed_service, dict)
    assert detailed_service["port"] == 22
    assert detailed_service["protocol"] == "tcp"
    host_dict = detailed_service["host"]
    assert host_dict["ip"] == "2.2.2.2"
