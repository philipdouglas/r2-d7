FROM python:3.6-slim
WORKDIR /bot
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD r2d7 ./r2d7/
CMD python -m r2d7.slack
