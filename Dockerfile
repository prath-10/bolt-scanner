FROM python:3.8-alpine

LABEL maintainer="Evyatar Meged <evyatarmeged@gmail.com>"
LABEL dockerfile-creator="Mostafa Hussein <mostafa.hussein91@gmail.com>"

RUN addgroup -S bolt && \
    adduser -S bolt -G bolt

RUN apk add --no-cache gcc musl-dev libxml2-dev libxslt-dev nmap nmap-scripts openssl

USER bolt
WORKDIR /home/bolt
RUN pip install bolt-scanner

ENV PATH=/home/bolt/.local/bin:${PATH}

ENTRYPOINT ["bolt"]
CMD ["--help"]
