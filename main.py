import os
import sys

def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("ERROR: no se encontró la variable de entorno API_KEY", file=sys.stderr)
        sys.exit(1)

    # --- EJEMPLO SEGURO de uso: hacer una petición a un endpoint ficticio ---
    # NO imprimas el api_key en los logs. Si necesitas depurar, imprime sólo longitud:
    print("API_KEY encontrada. Longitud:", len(api_key))

    # Ejemplo de cómo usarla con requests (descomentar si instalás requests)
    # import requests
    # headers = {"Authorization": f"Bearer {api_key}"}
    # resp = requests.get("https://api.ejemplo.com/me", headers=headers, timeout=10)
    # print("Status code:", resp.status_code)
    # print("Respuesta (primeros 200 chars):", resp.text[:200])

if __name__ == "__main__":
    main()
