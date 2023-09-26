FROM gethue/hue:latest

USER root

RUN mv /etc/apt/sources.list.d/nodesource.list /etc/apt/sources.list.d/nodesource.list.disabled
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get  install -y \
    ca-certificates \
    libgnutls30 \
    netcat
RUN mv /etc/apt/sources.list.d/nodesource.list.disabled /etc/apt/sources.list.d/nodesource.list
COPY ./entrypoint.sh .
RUN mkdir hive
COPY  ./hive-site.xml /hive/
RUN chmod +x ./entrypoint.sh

RUN /usr/share/hue/build/env/bin/pip install thrift-sasl

ENTRYPOINT [ "./entrypoint.sh" ]

CMD ["./startup.sh"]