FROM openjdk:8-jdk-slim-buster
LABEL maintainer="Manan Mukim"

RUN apt-get update -yqq && \
    apt-get upgrade -yqq && \
    apt-get install -yqq --no-install-recommends \
    apt-utils \
    curl \
    wget \
    netcat && \
    apt-get autoremove -yqq --purge

ENV HADOOP_VERSION=3.3.4
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=/etc/hadoop
ENV USER=root
ENV PATH=${HADOOP_HOME}/bin/:$PATH

RUN mkdir -p /opt/hadoop

RUN wget -c -O hadoop.tar.gz https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
RUN tar xvf hadoop.tar.gz --directory=/opt/hadoop --exclude=hadoop-${HADOOP_VERSION}/share/doc --strip 1
RUN rm -rf hadoop.tar.gz
RUN ln -s /opt/hadoop/etc/hadoop /etc/hadoop
RUN mkdir /opt/hadoop/logs
RUN mkdir /hadoop-data

COPY ./conf/ ./conf
USER root
RUN mv ./conf/* /etc/hadoop/
RUN rm -rf ./conf

COPY ./entrypoint.sh .

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]