# Decision note- architecture of the Atlas Industrie campus


## 1. Context and requirements
## 2. Technical targets retained
## 3. The two architectures compared
        Between S2 and S1, S1 is more expensive than S2 by 2 462 400 - 1 717 200 = 745 200 MAD over 5 years.
        Between S2 and S3, S2 is more expensive than S3 by 1 717 200 - 1 684 800 = 32 400 MAD over 5 years.
## 4. Five-year costing
     Computations :
            For S1 three tiers, we have : 
                1- 10 access : 10 x 27 000 MAD/access switch = 270 000 MAD
                2- 2 modular cores : 2 x 162 000 MAD/L3 core = 324 000 MAD
                3- 4 distribution switches : 4 × 54 000 = 216 000 MAD
                4- 2 Firewalls : 216 000 MAD
                5- Optics and fibre : 129 600 MAD
            Therefore :
                CAPEX = 270 000 MAD + 324 000 MAD + 216 000 MAD + 216 000 MAD + 129 600 MAD = 1 155 600 MAD
                TCO(5 years) = CAPEX + (10% of CAPEX + (10+2+4+2) x 1.5d x 5 400 MAD) = 2 462 400 MAD

            For S2 collapsed core, we have :
                1- 10 access : 10 x 27 000 MAD/access switch = 270 000 MAD
                2- 2 modular cores : 2 x 86 400 MAD/L3 core = 172 800 MAD
                3- 2 Firewalls : 216 000 MAD
                4- Optics and fibre : 108 000 MAD
            Therefore :
                CAPEX = 270 000 + 172 800 + 216 000 + 108 000 = 766 800 MAD
                TCO(5 years) = CAPEX + (10% of CAPEX + (10+2+2) x 1.5d x 5 400 MAD) = 1 717 200 MAD
            
            For S3 single-site, we have :
                1- 10 access : 10 x 27 000 MAD/access switch = 270 000 MAD
                2- 2 modular cores : 2 x 86 400 MAD/L3 core = 172 800 MAD
                3- 2 Firewalls : 216 000 MAD
                4- Optics and fibre : 86 400 MAD
            Therefore :
                CAPEX = 270 000 + 172 800 + 216 000 + 86 400 = 745 200 MAD 
                TCO(5 years) = CAPEX + (10% of CAPEX + (10+2+2) x 1.5d x 5 400 MAD) = 1 684 800 MAD

## 5. Decision and justification
From the computations and the comparisons between S1 and S2 on one hand and S2 and S3 on the other, S2 ccollapsed core distributed between A and B is retained.
Why ? Well simply put S2 is cheaper in terms of its five-year TCO than S1 while keeping redundancy between sites A and B and more expensive than S3 in terms of 
the five-year TCO due to the improved resilience by distributing the core between the two rooms. Additionally, with the assumption of 108 000 MAD per hour of outage,
the additional cost of 32 400 MAD over 5 years over S1 is recovered if it prevents a number of hours of outage in the architecture H such that : H   = 32 400/108 000 = 0.3 h or around 18 min. Also, S3 contains two cores in the same building A, which means that an incident in A could have a negative impact on the whole campus, that's why S3 wasn't chosen not because it is an equivalent cheap solution, but because it is a different solution.
             
## 6. Risks and points of failure
## 7. Assumptions and limits

All prices are expressed in MAD excluding tax.
Conversion rate used: 1 € = 10.8 MAD.
Analysis period: five years.
Vendor support equals 10% of CAPEX per year.
Operational effort equals 1.5 days per device per year at 5,400 MAD/day.
Power and cooling costs are excluded.
Inflation is excluded.
Building works and civil engineering costs are excluded.
No cybersecurity incident costs are included.
No equipment replacement during the five-year period is assumed.
