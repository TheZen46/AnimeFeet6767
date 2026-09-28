Setup: 2+ router, clients

Assign IP (Ethernet)
	enable
	conf t
	interface fastEthernet \[interface/0]
	ip address \[IP] \[Subnet mask]
	no shutdown
	exit
	exit
	copy run start

Assign IP (Console)
	enable
	conf t
	interface serial\[interface/0]
	ip address \[IP] \[Subnet mask]
	clock rate \[clock]
	no shutdown
	exit
	exit
	copy run start

Route traffic to serial
	enable					
	conf t			
	interface serial \[interface/0]		
	ip route 0.0.0.0 0.0.0.0 serial \[interface/0]
	exit				
	exit				
	copy run start

Configure static NAT
	enable
	conf t
	ip nat inside source static \[inside IP] \[outside IP] 
	interface Serial \[interface/0]
	ip nat outside
	exit
	interface fastethernet \[interface/0]
	ip nat inside
	exit
	exit
	copy run start

Configure dynamic NAT
	Route traffic to serial
		enable
		conf t
		interface serial \[interface/0]
		ip route 0.0.0.0 0.0.0.0 serial \[interface/0]
		exit
		exit
		copy run start
	enable
	conf t
	access-list \[name] permit \[IP pool] \[Inverse subnet mask]
	ip nat inside source list \[access list name] interface serial \[interface/0] overload
	interface serial \[interface/0]
	ip nat outside
	exit
	interface fastEthernet \[interface/0]
	ip nat inside
	exit
	exit
	copy run start