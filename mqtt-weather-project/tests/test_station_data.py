from stations.station1 import create_data_for_test


def test_create_data_structure():
    data = create_data_for_test("WS-TEST")

    assert data["stationId"] == "WS-TEST"
    assert "temperature" in data
    assert "humidity" in data
    assert "timestamp" in data
