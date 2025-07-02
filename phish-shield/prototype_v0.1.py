#!/usr/bin/env python3
"""
🛡️ FortiX phish-shield - Innovación ética en detección de amenazas
Características clave:
1. Análisis heurístico de URLs/emails
2. Sin dependencias corporativas
3. Optimizado para hardware antiguo
"""

def analizar_phishing(contenido):
    """Detecta patrones de phishing sin vender datos"""
    # Capa 1: Dominios sospechosos (ej: "paypa1.com")
    dominios_falsos = ["paypa1", "micros0ft", "banc0"]
    
    return any(dominio in contenido.lower() for dominio in dominios_falsos)

if __name__ == "__main__":
    print("🔥 phish-shield v0.1 - Ética > Corporaciones")
    prueba = "Confirme su cuenta en paypa1.com"
    print(f"¿Es phishing? {analizar_phishing(prueba)}")
