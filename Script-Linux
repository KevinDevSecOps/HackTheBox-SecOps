#!/bin/bash

echo "Analizando configuraciones sudo..."
sudo -l

echo "Buscando archivos con permisos SUID..."
find / -perm -4000 -type f 2>/dev/null

echo "Analizando procesos en ejecución..."
ps aux
