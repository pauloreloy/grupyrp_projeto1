FROM python:3
WORKDIR /bot
COPY requirements.txt /bot
RUN pip install --no-cache-dir -r requirements.txt
COPY bot.py /bot/
CMD [ "python", "./bot.py" ]