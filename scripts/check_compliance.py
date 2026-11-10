import pathlib 
import re 
import sys 
import yaml 
 
try: 
    with open('data/compliance.yml', encoding='utf-8') as f: 
        rules = yaml.safe_load(f) 
    required, forbidden = rules['required'], rules['forbidden'] 
except (OSError, yaml.YAMLError, KeyError, TypeError) as exc: 
    print(f'Check impossible: cannot read data/compliance.yml ({exc})') 
    sys.exit(2) 
 
files = sorted(pathlib.Path('configs').glob('*.cfg')) 
if not files: 
    print('Check impossible: no configuration in configs/, nothing was checked.') 
    sys.exit(2) 
 
errors = [] 
for cfg in files: 
    text = cfg.read_text(encoding='utf-8') 
    for pattern in required: 
        if not re.search(pattern, text, re.M): 
            errors.append(f'{cfg.name}: required pattern missing: {pattern}') 
    for pattern in forbidden: 
        if re.search(pattern, text, re.M): 
                  errors.append(f'{cfg.name}: forbidden pattern present: {pattern}') 

for e in errors: 
    print(e) 
print(f'{len(files)} configuration(s) checked, {len(errors)} discrepancy(ies)') 
sys.exit(1 if errors else 0) 
