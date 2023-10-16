FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["predict_docker.py", "Pipfile","Pipfile.lock","./"]

RUN pipenv install --system --deploy

# RUN pipenv install flask gunicorn

EXPOSE 9696

ENTRYPOINT [ "gunicorn","--bind=0.0.0.0:9696","predict_docker:app" ]