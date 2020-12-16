import unittest
from conf2yaml import convert_to_yaml
from uciparse import uci
from pyfakefs import fake_filesystem_unittest
from test_data import *

class test_suite(unittest.TestCase):
    def test_firwall_1(self):
        with fake_filesystem_unittest.Patcher() as patcher:
            lines = test_firewall_1["input"].split("\n")
            self.assertEqual( test_firewall_1["output"],convert_to_yaml(uci.UciFile.from_lines(lines)))
    def test_firewall_2(self):
        with fake_filesystem_unittest.Patcher() as patcher:
            lines = test_firewall_2["input"].split("\n")
            self.assertEqual( test_firewall_2["output"],convert_to_yaml(uci.UciFile.from_lines(lines)))

    def test_firewall_1_with_list(self):
        with fake_filesystem_unittest.Patcher() as patcher:
            # patcher.fs.create_file('/mock', contents=test_interface_name_identification["input"])

            lines = test_firewall_1_with_list["input"].split("\n")
            self.assertEqual(test_firewall_1_with_list["output"], convert_to_yaml(uci.UciFile.from_lines(lines)))

                # def test_interface_cdp_status(self):
    #     with fake_filesystem_unittest.Patcher() as patcher:
    #         patcher.fs.create_file('/mock', contents=test_interface_cdp_status["input"])
    #         self.assertEqual(convert_to_yaml(CiscoConfParse('/mock')), test_interface_cdp_status["output"])

    # def test_interface_switchport_access_vlan(self):
    #     with fake_filesystem_unittest.Patcher() as patcher:
    #         patcher.fs.create_file('/mock', contents=test_interface_switchport_access_vlan["input"])
    #         self.assertEqual(convert_to_yaml(CiscoConfParse('/mock')), test_interface_switchport_access_vlan["output"])
    #
    # def test_interface_switchport_mode(self):
    #     with fake_filesystem_unittest.Patcher() as patcher:
    #         patcher.fs.create_file('/mock', contents=test_interface_switchport_mode["input"])
    #         self.assertEqual(convert_to_yaml(CiscoConfParse('/mock')), test_interface_switchport_mode["output"])
    #
    # def test_interface_switchport_port_security(self):
    #     with fake_filesystem_unittest.Patcher() as patcher:
    #         patcher.fs.create_file('/mock', contents=test_interface_switchport_port_security["input"])
    #         self.assertEqual(convert_to_yaml(CiscoConfParse('/mock')), test_interface_switchport_port_security["output"])
    #
    # def test_interface_power_inline_police(self):
    #     with fake_filesystem_unittest.Patcher() as patcher:
    #         patcher.fs.create_file('/mock', contents=test_interface_power_inline_police["input"])
    #         self.assertEqual(convert_to_yaml(CiscoConfParse('/mock')), test_interface_power_inline_police["output"])
    #
    # def test_interface_spanning_tree(self):
    #     with fake_filesystem_unittest.Patcher() as patcher:
    #         patcher.fs.create_file('/mock', contents=test_interface_spanning_tree["input"])
    #         self.assertEqual(convert_to_yaml(CiscoConfParse('/mock')), test_interface_spanning_tree["output"])


if __name__ == '__main__':
    unittest.main()