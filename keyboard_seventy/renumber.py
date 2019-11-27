import io

with open("keyboard_seventy.kicad_pcb", "r") as file:
    data = file.readlines()
    
count = 120
for l in range(len(data)):
    if " D1 " in data[l]:
        data[l] = data[l].replace(" D1 ", " D" + str(count) + " ")
        print(data[l])
        count -= 1
        
with open("keyboard_seventy.kicad_pcb", "w") as file:
    file.writelines(data)
