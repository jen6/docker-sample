FROM public.ecr.aws/docker/library/python:3.8.10

ADD requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY . /app

CMD python -m uvicorn app.main:app  --host=0.0.0.0

