FROM ubuntu:latest
RUN apt-get update && apt-get -y install python3 python3-pip chromium-browser chromium-chromedriver
RUN pip3 install selenium
RUN rm -rf /var/lib/apt/lists/*
COPY test_selenium.py 
