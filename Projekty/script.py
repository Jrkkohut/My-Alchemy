# import knižnice na prácu s json formátom
import json

# otvorenie súboru príkazom open("cesta ku súboru", "mód otvorenia: r->read, w->write") 
with open("E:\VS CODE\data.json", "r") as json_file:
    # načítanie dát zo súboru do premennej, premenná je typu dictionary(slovník)
    data = json.load(json_file)

# vypísanie kľúčov prvej úrovne dát
print(data.keys()) 
print("=========================")

# vypísanie kľúčov druhej úrovne
print(data["frinx-uniconfig-topology:configuration"].keys()) 
print("=========================")

# vypísanie hodnôť druhej úrovne
print(data["frinx-uniconfig-topology:configuration"].values()) 
print("=========================")

# vypísanie prvého rozhrania
print(data["frinx-uniconfig-topology:configuration"]["openconfig-lldp:lldp"]["interfaces"]["interface"][0])
print("=========================")