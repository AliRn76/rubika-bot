FROM python:3.10
ENV PYTHONUNBUFFERED 1

RUN mkdir /rubika-bot
WORKDIR /rubika-bot
COPY . /rubika-bot/


RUN mkdir -p /usr/share/fonts/truetype/
RUN install -m644 fonts/B\ Koodak\ Bold.ttf /usr/share/fonts/truetype/

RUN pip install -U pip
RUN pip install mkdocs mkdocs-material mdx-include

CMD ["mkdocs", "serve", "-a", "0.0.0.0:8080"]