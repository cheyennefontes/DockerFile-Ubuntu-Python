FROM ubuntu

RUN apt update && apt install -y python3 && apt install -y python3-pip && pip install requests && pip install beautifulsoup4 && apt clean

COPY scrp.py /opt/scrp.py

CMD python3 /opt/scrp.py
