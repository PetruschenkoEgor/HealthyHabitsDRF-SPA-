FROM nginx:latest

# Создаем директорию для статичных файлов
RUN mkdir -p /app/staticfiles

# Копируем конфигурационный файл Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Копируем HTML-файлы в каталог Nginx
COPY html/ /usr/share/nginx/html/

# Копируем скрипт обновления known_hosts
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

# Указываем порт для внешнего доступа
EXPOSE 8080

# Устанавливаем точку входа
ENTRYPOINT ["/entrypoint.sh"]

# Основной процесс (в данном случае, запуск Nginx)
CMD ["nginx", "-g", "daemon off;"]