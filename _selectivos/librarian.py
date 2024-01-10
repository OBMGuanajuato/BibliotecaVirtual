year = "2022-2023"

diccionario_level = {
    1: ("4to y 5to de Primaria", "Prim4,5"),
    2: ("6to de Primaria", "Prim6"),
    3: ("1ro de Secundaria", "Sec1"),
    4: ("2do de Secundaria", "Sec2"),
    5: ("3ro de Secundaria", "Sec3")
}


for i in range(1,4):
    for j in range(1,6):
       with open(f"{year}-S{i}.{diccionario_level[j][1]}.md", 'w') as f:
        f.write(f"""---
year: "{year}"
exam-number: {i}
level: "{diccionario_level[j][0]}"
thumbnail: "assets/img/Logo.png"
file: "assets/pdf/Selectivos/{year} S{i}.{diccionario_level[j][1]}.pdf"
---""")