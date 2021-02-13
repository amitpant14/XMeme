FROM python:3.6-alpine

RUN adduser -D xmemeuser

WORKDIR /home/xmeme

COPY backend/requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY backend/api api
COPY backend/migrations migrations
COPY backed/backend.py backend/config.py backend/boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP backend.py

RUN chown -R xmemeuser:xmemeuser ./
USER xmemeuser

EXPOSE 8081
ENTRYPOINT ["./boot.sh"]
