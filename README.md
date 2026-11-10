\# Atlas Industrie –- network architecture repository

&#x20;

Design of the Atlas Industrie network, the fictitious company of the

"Advanced Network Architectures" course. One folder per object type;



the addressing plan is authoritative in `data/vlans.yml`. 

Localcheck: `python3 scripts/check\_vlans.py` from the repository root.



Local IPv6 prefix : c684828955a0

• It checks character strings, not the effective configuration: passive-interface default does 
not prove that only the intended interfaces are active. 
• Regular expressions give false positives and false negatives: an SSH line does not prove that 
Telnet is closed. 
• Syntax differs between device families: rules are needed per family, otherwise the check finds 
nothing and reports it as a success. 
• It validates nothing of the network's behaviour: the eleven tests of step 5 remain indispensable. 
A configuration can be right on paper and produce a broken network. 
