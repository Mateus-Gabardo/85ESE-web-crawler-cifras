FROM python:3.11.6
WORKDIR /app
COPY crawler_lyrics . 
RUN pip install -r requirements.txt
RUN cd crawler_lyrics
CMD ["scrapyrt"]