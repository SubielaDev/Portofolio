# -----------------------------------------------------------------------------
# Documentación del Dockerfile para Sitio Web Estático
# -----------------------------------------------------------------------------
# 1. Imagen base: Usamos Nginx versión Alpine (una distribución Linux ultraligera)
FROM nginx:alpine

# 2. Copia de archivos: Copiamos todo el contenido del repositorio actual (.)
#    hacia la carpeta predeterminada desde donde Nginx sirve páginas web.
COPY . /usr/share/nginx/html

# 3. Exposición de puerto: Informamos a Docker que el servidor escuchará en el puerto 80.
EXPOSE 80

# 4. Comando de inicio: Ejecutamos Nginx en primer plano para mantener el contenedor activo.
CMD ["nginx", "-g", "daemon off;"]
