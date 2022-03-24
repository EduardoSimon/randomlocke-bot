FROM python:3

ENV APP=/app

WORKDIR $APP

COPY requirements.txt $APP

RUN pip install -r requirements.txt

COPY . $APP

CMD [ "python", "pokebot.py" ]