a = "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/<NetworkAdapter-Id>/NetworkDeviceFunctions/<NetworkDevice-Id>"
b = "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/<NetworkAsdapter-Id>/NetworkPorts/<NetworkPort-Id>"
if "<NetworkAdapter-Id>" in b and ("<NetworkDevice-Id>" in b or "<NetworkPort-Id>" in b):
        print True
