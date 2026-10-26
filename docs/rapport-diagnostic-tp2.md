# Diagnostic report - Lab 2

## 1. What was implemented 

1.OSPF Deployment between CC-A and CC-B
2.VRF-Lite Segmentation
3.VRRP High Availability
4.Inter-VRF Connectivity Through Firewalls
5.Secure Management Services
6.Layer-2 Security
7.Testing the flows through 11 tests
8.Investigation of the 3 faults

## 2. The eleven tests and their results 

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

## 3. The fault diagnosed 
Fault A : ACL blocking OSPF

Observed symptom : OSPF changed from FULL to Down after some 40 seconds
Command that gave the answer: show access-lists revealed OSPF traffic being denied when an ACL applied inbound on the inter-core link.
Cause: ACL on Gi0/0 denied OSPF protocol 89 packets.
Fix: Add "permit ospf any any" to the ACL to permit protocol 89 between the two router addresses.
Result: OSPF adjacency returned to FULL and routes were restored.

Fault B : the MTU

Observed symptom : OSPF neighbor stuck at ExStart or Exchange and never goes to FULL.
Command that gave the answer : show ip ospf neighbor
Cause : Multiple MTUs on both interfaces of CC-A and CC-B.
Fix : Aligning the MTUs then "clear ip ospf process"
Result : OSPF neighbor finally went to FULL.

Fault C : the interface left passive

Observed Symptom : Neighbor down and no Hellos receives despite the correct address and the up state of the interface
Command that gave the answer : "show ip ospf neighbor" and "show ip interface brief"
Cause : only "passive-interface default" is present, but "no passive-interface" for the inter-core link is missing
Fix : no passive-interface GigabitEthernet0/0 under router ospf 1
Result : the OSPF neighbor finally went FULL according to the data given via the show ip ospf neighbor command and the OSPF routes reappeared.

## 4. Measurements, and what they really measure 
1. For Fault A, the 40 s measurement is related to the OSPF fault detection and there's no reconvergence to measure because of the only path between the two cores
2. For Fault B, there's on measurement related to the detection of the OSPF neighbor stuck at ExStart or Exchange and who never goes to FULL.
3. For Fault C, the measure that gave 0 OSPF neighbor formed is only for the capability for an adjacency to be formed, no convergence time measured. 

## 5. Accepted limits
1.Behaviour of the firewall pair not tested
2.Absence of the deployment of 802.1X 
3.MAC filtering on the OT ports accepted depite the weakness of that measure
4.Compliance check compares character strings and does not validate the behaviour of the network




