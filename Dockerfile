FROM python:3.8.10
WORKDIR /code 
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# ADDED THIS FOR SUPPORT FOR MAC M1;
RUN pip install tensorflow-aarch64 -f https://tf.kmtea.eu/whl/stable.html
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9001"]