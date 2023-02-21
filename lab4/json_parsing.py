import json

with open('sample_date.json') as f:
    data = json.load(f)

interfaces = data['imdata']

print("Interface Status")
print("="*80)
print("DN".ljust(51), "Description".ljust(22), "Speed".ljust(9), "MTU")
print("--------------------------------------------------  --------------------   ------   ------")

for interface in interfaces:
    dn = interface['l1PhysIf']['attributes']['dn']
    desc = interface['l1PhysIf']['attributes']['descr']
    speed = interface['l1PhysIf']['attributes']['speed']
    mtu = interface['l1PhysIf']['attributes']['mtu']

    print(dn.ljust(51), desc.ljust(22), speed.ljust(9), mtu)
