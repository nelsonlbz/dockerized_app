FROM python:3.8

WORKDIR /opt
ADD /dockerized_app /opt
RUN pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python", "-u", "/opt/main.py"]
