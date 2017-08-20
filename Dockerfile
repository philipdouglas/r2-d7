FROM python:3.6-slim
ADD . /src
WORKDIR /src
RUN pip install .
CMD python -m r2d7.slack
