FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile","Pipfile.lock", "predict.py", "./"]

RUN pipenv install --system --deploy

COPY ["dv.bin","model1.bin", "predict.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]