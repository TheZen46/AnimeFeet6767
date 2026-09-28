Setup: 1 router

enable
conf t

hostname \[name]
username \[name] privilege \[0-15] password \[password]

assign IP to interface
	interface \[interface]
	ip address \[IP] \[subnet mask]
	no shutdown 

configure from console
	line \[line]
	login local

configure from telnet
	line \[line]
	login local
	transport input telnet

copy run start

to connect \[CMD]
	telnet \[IP]

