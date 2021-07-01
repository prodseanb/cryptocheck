From python:3.9.5

ADD run.py .

ADD banner.py .

COPY requirements.txt .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "./run.py"]