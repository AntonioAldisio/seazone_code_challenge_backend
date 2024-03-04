#!/bin/bash
echo "Irei esperar 50 segundos"
sleep 50

python manage.py makemigrations
python manage.py migrate api

echo "Iniciando loaddata"
python manage.py loaddata seeder.json

if [ $? -eq 0 ]; then
echo "Inicaindo API"
python manage.py runserver 0.0.0.0:8000
else
    echo "Erro ao iniciar API"
fi
