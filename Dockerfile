FROM python:3.8.13-bullseye

COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader popular
WORKDIR ./src

EXPOSE 5000
CMD ["pyhon", "api.py"]
