# Script para revertir el cifrado de main1
encrypted_hex = "9E89846A786585866A977D797C8463807C7F6B67848BAB907B698370896B997C797C8D6C6F7E81AE866AB36D7B7F669D7E6A7F96678F9382898263B474"
key = "mysecretkey"

# Convertimos el hex a una lista de números (bytes)
cipher_bytes = [int(encrypted_hex[i:i+2], 16) for i in range(0, len(encrypted_hex), 2)]

flag = ""
for i in range(len(cipher_bytes)):
    # Sacamos los caracteres de la llave que el programa usaba en cada paso
    k1 = ord(key[i % len(key)])     # Usado para el XOR
    k2 = ord(key[(i + 1) % len(key)]) # Usado para la Suma
    
    # Aplicamos la lógica inversa: primero restamos k2, luego hacemos XOR con k1
    # Usamos & 0xFF para mantener el resultado dentro del rango de un byte (0-255)
    char_code = (cipher_bytes[i] - k2) ^ k1
    flag += chr(char_code & 0xFF)

print(f"La Flag es: {flag}")
