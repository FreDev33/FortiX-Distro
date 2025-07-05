# Guía de instalación de FortiX

Bienvenido a FortiX Distro.  
Sigue estos pasos para instalar FortiX de forma segura.

## Requisitos mínimos
- CPU: x86 (32-bit) o superior
- RAM: 512 MB mínimo (1 GB recomendado)
- Disco: 4 GB libres

## Pasos de instalación

1. Descarga la ISO desde la web oficial.
2. Graba la ISO en un USB:
   ```bash
   sudo dd if=fortix-alpha.iso of=/dev/sdX bs=4M status=progress
