FROM python:3

ENV APP=/app

WORKDIR $APP

RUN pip install --upgrade numpy pandas
RUN pip install --upgrade google-api-python-client google-auth-httplib3 google-auth-oauthlib google-auth

COPY . $APP

CMD [ "python", "app.py" ]