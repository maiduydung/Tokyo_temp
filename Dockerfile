FROM python:3.8.5

COPY ./app.py /deploy/

COPY ./requirements.txt /deploy/

COPY ./model_tokyo_temp.pkl /deploy/

WORKDIR /deploy/

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python", "app.py"]