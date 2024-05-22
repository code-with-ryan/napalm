import unittest
from napalm.ios import IOSDriver
from napalm.base.test.double import BaseTestDouble

class TestIOSDHCPServerInfo(unittest.TestCase):
    def setUp(self):
        self.device = IOSDriver('hostname', 'username', 'password', timeout=60)
        self.device.device = BaseTestDouble()
        self.device.open = self.mock_open
        self.device.close = self.mock_close

    def mock_open(self):
        # Mock the open method to avoid actual device connection
        pass

    def mock_close(self):
        # Mock the close method to avoid actual device disconnection
        pass

    def test_get_dhcp_server_info(self):
        expected_output = {
            'bindings': [
                {'ip': '192.168.0.10', 'mac': '0011.2233.4455', 'lease_expiry': '01:23:45', 'type': 'Automatic', 'state': 'Active', 'interface': 'GigabitEthernet0/1'}
            ],
            'pools': [
                {'name': 'POOL1', 'address_range': '192.168.0.1 - 192.168.0.254', 'leases': '10', 'allocated': '5', 'remaining': '5'}
            ]
        }
        # Mock the CLI method to return predefined outputs
        self.device.cli = lambda x: {
            'show ip dhcp binding': '192.168.0.10    0011.2233.4455    01:23:45    Automatic    Active    GigabitEthernet0/1\n',
            'show ip dhcp pool': 'Pool POOL1 :\n  Address range 192.168.0.1 - 192.168.0.254\n  Leases 10\n  Allocated 5\n  Remaining 5\n'
        }
        result = self.device.get_dhcp_server_info()
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
