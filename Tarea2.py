import math
import matplotlib.pyplot as plt

def obtener_fuerza_por_componentes():
    x = float(input("Ingrese el componente en X: "))
    y = float(input("Ingrese el componente en Y: "))
    return x, y

def obtener_fuerza_por_magnitud_direccion():
    magnitud = float(input("Ingrese la magnitud de la fuerza: "))
    angulo_grados = float(input("Ingrese la dirección (grados): "))
    angulo_radianes = math.radians(angulo_grados)
    x = magnitud * math.cos(angulo_radianes)
    y = magnitud * math.sin(angulo_radianes)
    return x, y

def obtener_angulo(fx, fy):
    angulo = math.degrees(math.atan2(fy, fx))
    if angulo < 0:
        angulo += 360
    return angulo

while True:
    try:
        total_fuerza = int(input("¿Cuántas fuerzas desea ingresar?: "))
        break
    except ValueError:
        print("Ingrese un número valido")
suma_x = 0
suma_y = 0
fuerzas_info = []

for i in range(total_fuerza):
    print(f"\nFuerza #{i+1}")
    while True:
        metodo = input("¿Quiere ingresar por 'componentes' o 'magnitud y dirección'? (c/m): ")
        if metodo == 'c':
            x, y = obtener_fuerza_por_componentes()
            break
        elif metodo == 'm':
            x, y = obtener_fuerza_por_magnitud_direccion()
            break
        else:
            print("Opción no válida. Por favor ingrese 'c' o 'm'.")

    suma_x += x
    suma_y += y

    angulo = obtener_angulo(x, y)
    magnitud = math.hypot(x, y)
    fuerzas_info.append((x, y, angulo, magnitud))

peso_bloque = float(input("\nIngrese la masa del bloque en kilogramos: "))

fuerza_magnitud = math.hypot(suma_x, suma_y)
fuerza_angulo = obtener_angulo(suma_x, suma_y)
aceleracion_ejex = suma_x / peso_bloque
aceleracion_ejey = suma_y / peso_bloque
aceleracion_magnitud = math.hypot(aceleracion_ejex, aceleracion_ejey)

print("\n--- Resultados ---")
print(f"Fuerza neta en X: {suma_x:.2f} N")
print(f"Fuerza neta en Y: {suma_y:.2f} N")
print(f"Magnitud de la fuerza neta: {fuerza_magnitud:.2f} N")
print(f"Dirección de la fuerza neta: {fuerza_angulo:.2f}°")
print(f"Aceleración en X: {aceleracion_ejex:.2f} m/s²")
print(f"Aceleración en Y: {aceleracion_ejey:.2f} m/s²")
print(f"Magnitud de la aceleración: {aceleracion_magnitud:.2f} m/s²")

plt.figure()
plt.title("Diagrama de Cuerpo Libre")
plt.xlabel("Eje X (N)")
plt.ylabel("Eje Y (N)")
plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')

circle = plt.Circle((0, 0), 4, color='gray', fill=False, linestyle='dotted')
plt.gca().add_patch(circle)

for angulo_ref in range(0, 360, 45):
    x_ref = 4 * math.cos(math.radians(angulo_ref))
    y_ref = 4 * math.sin(math.radians(angulo_ref))
    plt.arrow(0, 0, x_ref, y_ref,
              head_width=0.15, head_length=0.15, fc='gray', ec='gray', length_includes_head=True, alpha=0.4)
    plt.text(x_ref*1.1, y_ref*1.1, f"{angulo_ref}°", fontsize=8, ha='center', color='gray')

plt.plot(0, 0, 'ks', markersize=10, label='Bloque')

for i, (fx, fy, angulo, magnitud) in enumerate(fuerzas_info):
    if i == 0:
        plt.arrow(0, 0, fx, fy, head_width=0.7, head_length=0.7, fc='blue', ec='blue', length_includes_head=True, label='Fuerzas Aplicadas')
    else:
        plt.arrow(0, 0, fx, fy, head_width=0.7, head_length=0.7, fc='blue', ec='blue', length_includes_head=True)
    texto = f"F{i+1}\n({fx:.1f}, {fy:.1f}) N\n{angulo:.1f}°"
    plt.text(fx*1.07, fy*1.07, texto, fontsize=8, color='blue')

plt.arrow(0, 0, suma_x, suma_y, head_width=0.7, head_length=0.7, fc='red', ec='red', length_includes_head=True, label='Fuerza Neta')
texto_neta = f"F neta\n({suma_x:.1f}, {suma_y:.1f}) N\n{fuerza_angulo:.1f}°"
plt.text(suma_x*1.05, suma_y*1.05, texto_neta, fontsize=9, color='red')

plt.legend(loc='upper left')
plt.axis('equal')

max_range = max([abs(max([fx for fx, _, _, _ in fuerzas_info] + [fy for _, fy, _, _ in fuerzas_info] + [suma_x, suma_y, 4])),
                 abs(min([fx for fx, _, _, _ in fuerzas_info] + [fy for _, fy, _, _ in fuerzas_info] + [suma_x, suma_y, -4]))])
plt.xlim(-max_range-1, max_range+1)
plt.ylim(-max_range-1, max_range+1)

plt.show()
