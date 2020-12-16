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

test_firewall_3_with_comment = {
    "input": """package firewall
    config rule
    option name 'Allow-MLD' #some Comment
    option target 'ACCEPT'\n""",
    "output": """---
firewall:
  rule:
    # some Comment      
  - name: Allow-MLD
    target: ACCEPT\n"""
}

test_firewall_4_network_named = {
    "input": """package network
    config interface 'loopback'
    option ifname 'lo'
    option proto 'static'
    option ipaddr '127.0.0.1'
    option netmask '255.0.0.0'

config interface 'lan'
    option ifname 'eth1.1'
    option type 'bridge'
    option proto 'static'
    option ipaddr '192.168.15.1'
    option netmask '255.255.255.0'
    option ip6assign '32'\n""",
    "output": """---
network:
  interface:
  - interface: loopback
    ifname: lo
    proto: static
    ipaddr: 127.0.0.1
    netmask: 255.0.0.0
  - interface: lan
    ifname: eth1.1
    type: bridge
    proto: static
    ipaddr: 192.168.15.1
    netmask: 255.255.255.0
    ip6assign: '32'\n"""
}

test_beardropper = {
    "input":
        """package bearDropper
        
config bearDropper
option defaultMode 'entire'
list firewallHookChain 'input_wan_rule:1'
list firewallHookChain 'forwarding_wan_rule:1'
list firewallHookChain 'input_lan_rule:1'
list firewallHookChain 'forwarding_lan_rule:1'
option firewallTarget 'DROP'

list logRegex '/has invalid shell, rejected$/d'
option attemptCount '5'
option banLength '100w'""",
    "output":
        """---
bearDropper:
  bearDropper:
  - defaultMode: entire
    firewallHookChain:
    - input_wan_rule:1
    - forwarding_wan_rule:1
    - input_lan_rule:1
    - forwarding_lan_rule:1
    firewallTarget: DROP
    logRegex:
    - /has invalid shell, rejected$/d
    attemptCount: '5'
    banLength: 100w\n"""
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
