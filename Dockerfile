From python:3.9.5

ADD cryptocheck.py .

COPY requirements.txt .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "./cryptocheck.py"]