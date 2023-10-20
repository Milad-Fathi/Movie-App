FROM python:3.10

WORKDIR /BackEnd

COPY ./requirements.txt /BackEnd/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /BackEnd/requirements.txt
 
COPY ./App /BackEnd/

EXPOSE 3000

CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "3000"]

