FROM python

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7040

CMD [ "python", "main.py"]