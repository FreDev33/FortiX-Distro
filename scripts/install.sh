# scripts/install.sh
#!/bin/bash
echo "Este script instalará paquetes y configurará FortiX."
# Aquí va tu lógica personalizada

# scripts/update.sh
#!/bin/bash
sudo apt update && sudo apt upgrade -y

# scripts/cleanup.sh
#!/bin/bash
sudo apt autoremove -y && sudo apt clean

# scripts/hardening.sh
#!/bin/bash
echo "Aplicando hardening básico..."
sudo apt install ufw -y
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing
