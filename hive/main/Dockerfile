FROM hadoop-main:latest
LABEL maintainer="Manan Mukim"

ENV HIVE_VERSION=3.1.3
ENV HIVE_HOME=/opt/hive
ENV PATH=${HIVE_HOME}/bin:$PATH

WORKDIR /opt

RUN apt-get update

RUN apt-get install wget && \
    wget -c -O hive.tar.gz https://archive.apache.org/dist/hive/hive-${HIVE_VERSION}/apache-hive-${HIVE_VERSION}-bin.tar.gz && \
    tar xvf hive.tar.gz && \
    rm hive.tar.gz && \
    mv apache-hive-${HIVE_VERSION}-bin hive && \
    wget -O ${HIVE_HOME}/lib/postgresql-jdbc.jar https://jdbc.postgresql.org/download/postgresql-42.2.14.jar && \
    apt-get --purge remove -yqq wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./hive-site.xml ${HIVE_HOME}/conf

COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 10000 
EXPOSE 10001
EXPOSE 10002

ENTRYPOINT [ "./entrypoint.sh" ]