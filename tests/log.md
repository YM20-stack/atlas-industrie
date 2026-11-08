## OSPF detection measurements

##Test 1 : Clean cut (carrier loss)

Commands : 
docker exec clab-atlas-campus-cc-a ip link set eth1 down 
docker exec clab-atlas-campus-cc-b vtysh -c 'show ip ospf neighbor'
docker exec clab-atlas-campus-cc-a ip link set eth1 up 

Result:
The OSPF neighbor link immediately disappears after the interface went down on CC-A.
The fibre is severed and both end cores lose the carrier and withdrew the route without for the dead timer.


##Test 2 : a silent failure

Commands : 
docker exec clab-atlas-campus-cc-b iptables -A INPUT -i eth1 -p ospf -j DROP 
# watch the neighbour on CC-B, and time it 
docker exec clab-atlas-campus-cc-b vtysh -c 'show ip ospf neighbor'
docker exec clab-atlas-campus-cc-b iptables -D INPUT -i eth1 -p ospf -j DROP 

Result:
The physical link remained up, but the OSPF neighbor relationship wasn't severed until
the OSPF dead interval expired after approximately 40 s without hearing the Hello packets.

