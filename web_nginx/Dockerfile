FROM nginx:latest 
RUN mkdir /usr/share/nginx/html/css /usr/share/nginx/html/js /usr/share/nginx/html/fonts /usr/share/nginx/html/images /usr/share/nginx/html/scss
COPY * /usr/share/nginx/html/
COPY css/* /usr/share/nginx/html/css/
COPY js/* /usr/share/nginx/html/js/
COPY fonts/* /usr/share/nginx/html/fonts/
COPY scss/* /usr/share/nginx/html/scss/
VOLUME /usr/share/nginx/html
EXPOSE 80/tcp

