FROM ubuntu:latest
RUN apt-get update && apt-get -y install python3 python3-pip chromium-browser chromium-chromedriver
RUN pip3 install selenium
RUN rm -rf /var/lib/apt/lists/*
RUN mkdir /opt/instagram
COPY test_selenium.py /opt/
COPY script.sh /opt/
WORKDIR /opt
CMD [ "python3", "test_selenium.py" ]
