Setup: 2+ switches, 2+ connections between switches

enable
conf t
interface gigabitEthernet \[interface/1]
switchport mode trunk
channel-group 1 mode on
copy run start