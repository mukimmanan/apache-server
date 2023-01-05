FROM hadoop-main:latest
LABEL maintainer="Manan Mukim"

# ENV HDFS_CONF_DFS_NAMENODE_DATA_DIR=file:///hadoop/hdfs/name

RUN mkdir -p /hadoop/hdfs/name

RUN hdfs namenode -format  

COPY start.sh start.sh

RUN chmod +x start.sh

EXPOSE 9870 9000

CMD [ "./start.sh" ]