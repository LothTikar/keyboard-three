import io

with open("keyboard_seventy.kicad_pcb", "r") as file:
    data = file.readlines()
    
count = 121
for l in range(len(data)):
    if "SW2" in data[l]:
        data[l] = data[l].replace("SW2", "SW" + str(count))
        print(data[l])
        count -= 1
        
with open("keyboard_seventy.kicad_pcb", "w") as file:
    file.writelines(data)
