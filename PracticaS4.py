from pathlib import Path 
ROOT = Path(__file__).resolve().parents[0]  # sube desde src/ a la raíz del proyecto C:\Users\BP_motta\python_UTP\UTP_Py
TXT  = ROOT / "DATOS"/"mediciones_200_mixto.txt"
print(ROOT)
valores = []
with open(TXT,'r', encoding="utf-8", newline="") as f:
    for linea in f: #lee linea por linea
        s = linea.strip()
        if not s or s.startswith("#"):
            continue
        if not s or s.startswith("!"):
            continue
        s= s.replace(",",".")#cambia la coma por punto
        try:
            valores.append(float(s)) #convierte a float y agrega a la lista
        except ValueError:
            pass #si no puede convertir, ignora la linea

Vmayor=[]
Vmenor=[]        
        
for i in valores:
    if  i >= 5:
        Vmayor.append(i)
    else:
        Vmenor.append(i)
print("ESTE ES EL LISTADO DE MAYOR ")
print(Vmayor)
print("ESTE ES EL LISTADO DE MENOR ")
print(Vmenor)
print("Son estos los conteos de mayor y menor") 
print(len(Vmayor))
print(len(Vmenor))