FROM python

RUN mkdir -p /usr/src/web/
WORKDIR /usr/src/web/

COPY . /usr/src/web/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["gunicorn"  , "-b", "0.0.0.0:$PORT", "web:app"]