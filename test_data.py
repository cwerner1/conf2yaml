#
# Define the file input and expected output for each test case
#

test_firewall_1 = {
    "input": """package firewall
    config rule
    option name 'Allow-MLD'
    option src 'wan'
    option proto 'icmp'
    option src_ip 'fe80::/10'
    option family 'ipv6'
    option target 'ACCEPT'\n""",
    "output": """---
firewall:
  rule:
  - name: Allow-MLD
    src: wan
    proto: icmp
    src_ip: fe80::/10
    family: ipv6
    target: ACCEPT\n"""
}
test_firewall_2 = {
    "input": """package firewall
config rule
    option name 'Allow-MLD'
    option src 'wan'
    option proto 'icmp'
    option src_ip 'fe80::/10'
    option family 'ipv6'
    option target 'ACCEPT'
config rule
    option name 'DROP-MLsadsdsaD'
    option src 'lan'
    option proto 'tcp'
    option src_ip 'fe80::/10'
    option family 'ipv4'
    option target 'DROP'\n
    \n""",
    "output": """---
firewall:
  rule:
  - name: Allow-MLD
    src: wan
    proto: icmp
    src_ip: fe80::/10
    family: ipv6
    target: ACCEPT
  - name: DROP-MLsadsdsaD
    src: lan
    proto: tcp
    src_ip: fe80::/10
    family: ipv4
    target: DROP\n"""
}


test_firewall_1_with_list = {
    "input": """package firewall
    config rule
    option name 'Allow-MLD'
    option src 'wan'
    option proto 'icmp'
    option src_ip 'fe80::/10'
    list icmp_type '130/0'
    list icmp_type '131/0'
    list icmp_type '132/0'
    list icmp_type '143/0'
    option family 'ipv6'
    option target 'ACCEPT'\n""",
    "output": """---
firewall:
  rule:
  - name: Allow-MLD
    src: wan
    proto: icmp
    src_ip: fe80::/10
    icmp_type:
    - 130/0
    - 131/0
    - 132/0
    - 143/0
    family: ipv6
    target: ACCEPT\n"""
}

test_interface_cdp_status = {
    "input":
"""interface GigabitEthernet1/0/1
 no cdp enable""",
    "output":
"""---
interfaces:
- cdp_disable: true
  name: GigabitEthernet1/0/1\n"""
}

test_interface_switchport_access_vlan = {
    "input": """interface GigabitEthernet1/0/1
 switchport access vlan 4""",
    "output": """---
interfaces:
- name: GigabitEthernet1/0/1
  switchport:
    access_vlan: '4'\n"""
}

test_interface_switchport_mode = {
    "input": """interface GigabitEthernet1/0/1
 switchport mode access""",
    "output": """---
interfaces:
- name: GigabitEthernet1/0/1
  switchport:
    mode: access\n"""
}

test_interface_switchport_port_security = {
    "input": """interface GigabitEthernet1/0/1
 switchport port-security""",
    "output": """---
interfaces:
- name: GigabitEthernet1/0/1
  switchport:
    port_security: true\n"""
}

test_interface_power_inline_police = {
    "input": """interface GigabitEthernet1/0/1
 power inline police""",
    "output": """---
interfaces:
- name: GigabitEthernet1/0/1
  power_inline_police: true\n"""
}

test_interface_spanning_tree = {
    "input": """interface GigabitEthernet1/0/1
 spanning-tree portfast
 spanning-tree guard root""",
    "output": """---
interfaces:
- name: GigabitEthernet1/0/1
  spanning_tree:
    guard_root: true
    portfast: true\n"""
}