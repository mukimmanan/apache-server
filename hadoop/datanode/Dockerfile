FROM hadoop-main:latest
LABEL maintainer="Manan Mukim"

# ENV HDFS_CONF_DFS_DATANODE_DATA_DIR=file:///hadoop/hdfs/data

RUN mkdir -p /hadoop/hdfs/data

COPY start.sh start.sh

RUN chmod +x start.sh

EXPOSE 9864

CMD [ "./start.sh" ]