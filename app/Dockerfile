FROM python:latest
WORKDIR /code
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install virtualenv
RUN python3 -m venv virtual
RUN . virtual/bin/activate 
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
CMD ["python", "app.py"]
