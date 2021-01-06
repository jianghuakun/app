import bluetooth
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print(nearby_devices)
for addr,name in nearby_devices:
    print(addr,name)
    if name=="红米手机":
        print(addr)
        services=bluetooth.find_service(name="红米手机",address=addr)
        for i in services:
            print(i)

