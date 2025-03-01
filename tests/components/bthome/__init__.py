"""Tests for the BThome integration."""

from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

from homeassistant.components.bluetooth import BluetoothServiceInfoBleak

TEMP_HUMI_SERVICE_INFO = BluetoothServiceInfoBleak(
    name="ATC 8D18B2",
    address="A4:C1:38:8D:18:B2",
    device=BLEDevice("A4:C1:38:8D:18:B2", None),
    rssi=-63,
    manufacturer_data={},
    service_data={
        "0000181c-0000-1000-8000-00805f9b34fb": b"#\x02\xca\t\x03\x03\xbf\x13"
    },
    service_uuids=["0000181c-0000-1000-8000-00805f9b34fb"],
    source="local",
    advertisement=AdvertisementData(local_name="Not it"),
    time=0,
    connectable=False,
)

TEMP_HUMI_ENCRYPTED_SERVICE_INFO = BluetoothServiceInfoBleak(
    name="TEST DEVICE 8F80A5",
    address="54:48:E6:8F:80:A5",
    device=BLEDevice("54:48:E6:8F:80:A5", None),
    rssi=-63,
    manufacturer_data={},
    service_data={
        "0000181e-0000-1000-8000-00805f9b34fb": b'\xfb\xa45\xe4\xd3\xc3\x12\xfb\x00\x11"3W\xd9\n\x99'
    },
    service_uuids=["0000181e-0000-1000-8000-00805f9b34fb"],
    source="local",
    advertisement=AdvertisementData(local_name="Not it"),
    time=0,
    connectable=False,
)

PM_SERVICE_INFO = BluetoothServiceInfoBleak(
    name="TEST DEVICE 8F80A5",
    address="54:48:E6:8F:80:A5",
    device=BLEDevice("54:48:E6:8F:80:A5", None),
    rssi=-63,
    manufacturer_data={},
    service_data={
        "0000181c-0000-1000-8000-00805f9b34fb": b"\x03\r\x12\x0c\x03\x0e\x02\x1c"
    },
    service_uuids=["0000181c-0000-1000-8000-00805f9b34fb"],
    source="local",
    advertisement=AdvertisementData(local_name="Not it"),
    time=0,
    connectable=False,
)

INVALID_PAYLOAD = BluetoothServiceInfoBleak(
    name="ATC 565384",
    address="A4:C1:38:56:53:84",
    device=BLEDevice("A4:C1:38:56:53:84", None),
    rssi=-56,
    manufacturer_data={},
    service_data={
        "0000181c-0000-1000-8000-00805f9b34fb": b"0X[\x05\x02\x84\x53\x568\xc1\xa4\x08",
    },
    service_uuids=["0000181c-0000-1000-8000-00805f9b34fb"],
    source="local",
    advertisement=AdvertisementData(local_name="Not it"),
    time=0,
    connectable=False,
)

NOT_BTHOME_SERVICE_INFO = BluetoothServiceInfoBleak(
    name="Not it",
    address="00:00:00:00:00:00",
    device=BLEDevice("00:00:00:00:00:00", None),
    rssi=-63,
    manufacturer_data={3234: b"\x00\x01"},
    service_data={},
    service_uuids=[],
    source="local",
    advertisement=AdvertisementData(local_name="Not it"),
    time=0,
    connectable=False,
)


def make_advertisement(address: str, payload: bytes) -> BluetoothServiceInfoBleak:
    """Make a dummy advertisement."""
    return BluetoothServiceInfoBleak(
        name="Test Device",
        address=address,
        device=BLEDevice(address, None),
        rssi=-56,
        manufacturer_data={},
        service_data={
            "0000181c-0000-1000-8000-00805f9b34fb": payload,
        },
        service_uuids=["0000181c-0000-1000-8000-00805f9b34fb"],
        source="local",
        advertisement=AdvertisementData(local_name="Test Device"),
        time=0,
        connectable=False,
    )


def make_encrypted_advertisement(
    address: str, payload: bytes
) -> BluetoothServiceInfoBleak:
    """Make a dummy encrypted advertisement."""
    return BluetoothServiceInfoBleak(
        name="ATC 8F80A5",
        address=address,
        device=BLEDevice(address, None),
        rssi=-56,
        manufacturer_data={},
        service_data={
            "0000181e-0000-1000-8000-00805f9b34fb": payload,
        },
        service_uuids=["0000181e-0000-1000-8000-00805f9b34fb"],
        source="local",
        advertisement=AdvertisementData(local_name="ATC 8F80A5"),
        time=0,
        connectable=False,
    )
