
Test 1 : PC-IT to the ERP server

Command : ping 10.42.18.50 from PC-IT
Result : connectivity to the ERP server successful


Test 2 : Guest to the ERP server

Command : ping 10.42.18.50 after moving PC-IT's port to VLAN 40 for guests
Result : request timed out


Test 3 : PC-IT to a PLC

Command : ping 10.42.64.50 from PC-IT
Result : connectivity to a PLC failed


Test 4 : Supervision to a PLC, building A isolated

Command : ping 10.42.64.50 from PC-SUP after shutting down CC-A and FW-A
Result : connectivity to a PLC successful and local routing by CC-B

Test 5 : SSH to CC-A from VLAN 20, then from an authorised workstation

Command : ssh 10.42.0.2 from PC-IT, then from 10.42.18.20
Result : connectivity denied for the first command and successful for the second command

Test 6 : Rogue DHCP server on an access port

Command : starting a DHCP service on a test workstation
Result : DHCP offers dropped

Test 7 : Third MAC address on a limited port

Command : changing the port-security maximum to 1 and manually changing the workstation's MAC address
Result : Security Violation Count > 0, before the restoration of the maximum to 2

Test 8 : Loss of CC-A alone

Command : CC-A(config)# interface Gi0/0
          shutdown
Result : routes and gateways transfered from CC-A to CC-B


Test 9 : Complete loss of building A

Command : CC-A, FW-A and ACC-A-01 shut down
Result : connectivity from PC-SUP to the PLCs successful and connectivity to PC-IT failed

Test 10 : Guest to an administration interface

Command : ssh 10.42.0.2 from VLAN 40
Result : access denied 

Test 11 : Loss of CC-B alone s

Command : CC-B shut down
Result : CC-A masters all the VLANs of B and the routing through the inter-building fiber continues
