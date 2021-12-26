FROM python:3.7-slim-buster as builder

WORKDIR /opt/app/

COPY ./contents/requirements.txt /opt/app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

FROM gcr.io/distroless/python3-debian10 as runner

LABEL maintainer="sig9 <sig9@sig9.org>"

WORKDIR /opt/app/

COPY --from=builder /usr/local/lib/python3.7/site-packages /root/.local/lib/python3.7/site-packages
COPY ./contents/ /opt/app/

EXPOSE 5000

CMD ["app.py"]
