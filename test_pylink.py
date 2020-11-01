import pylink
jlink = pylink.JLink()

print(jlink.num_connected_emulators())
print(jlink.connected_emulators())

# jlink.open(683585795)
jlink.open(ip_addr="0.0.0.0:19020")

print(jlink.product_name)

if jlink.opened():
    print("jlink.opened")

if jlink.connected():
    print("jlink.connected")

jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
jlink.connect("NRF52840_XXAA", 'auto', True)
print(jlink.core_id())
print(jlink.device_family())

if jlink.target_connected():
    print("jlink.target_connected")


jlink.reset()
jlink.erase()
