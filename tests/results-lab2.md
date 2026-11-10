Test 1 : PC-IT to the ERP server
Command : ping -c 3 10.42.18.50 from PC-IT 
Result : connectivity to the ERP server successful


Test 2 : Guest to the ERP server
Command : ping -c 3 10.42.18.50 after moving PC-IT's port to VLAN 40 for guests
Result : request timed out


Test 3 : PC-IT to a controller
Command : ping -c 3 10.42.64.50 from PC IT 
Result : connectivity to a PLC failed


Test 4 : Supervision to a PLC, building A isolated
Command : ping -c 10.42.64.50 from PC-SUP after shutting down CC-A and FW-A via node_down cc-a, node_down fw-a
Result : connectivity to a PLC successful and local routing by CC-B

Test 5 : SSH to CC-A from VLAN 20, then from the administration station
Command : nc -w 3 10.42.16.2 22 </dev/null from PC-IT, then nc -w 3 10.42.18.2 22 </dev/null from ADM-A 
Result : connectivity denied for the first command and successful for the second command

Test 6 : Rogue DHCP server on an access port
Command : starting a DHCP service on a test workstation only on the IOS bench
Result : DHCP offers dropped, on containerlab, it's not testable

Test 7 : Third MAC address on a limited port
Command : changing the port-security maximum to 1 and manually changing the workstation's MAC address only on the IOS bench
Result : Security Violation Count > 0, before the restoration of the maximum to 2, on containerlab, it's not testable

Test 8 : Loss of CC-A alone
Command : ping -i 0.2 -c 150 10.42.18.50 from PC-IT, and node_down cc-a during the ping 
Result : routes and gateways transfered from CC-A to CC-B


Test 9 : Complete loss of building A
Command : CC-A, FW-A and ACC-A-01 node_down
Result : connectivity from PC-SUP to the PLCs successful and connectivity to PC-IT failed

Test 10 : Guest to an administration interface
Command : PC-IT as a guest, nc -w 3 10.42.48.2 22 </dev/null 
Result : access denied 

Test 11 : Loss of CC-B alone 
Command : ping -i 0.2 -c 150 10.42.64.50 from PC-SUP, and node_down cc-b during the ping 
Result : CC-A masters all the VLANs of B and the routing through the inter-building fiber continues
