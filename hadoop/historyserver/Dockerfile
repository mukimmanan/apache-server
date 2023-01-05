FROM hadoop-main:latest
LABEL maintainer="Manan Mukim"

ENV HDFS_CONF_DFS_DATANODE_DATA_DIR=file:///hadoop/dfs/data

RUN mkdir -p /hadoop/yarn/timeline

VOLUME [ "./yarn/timeline:/hadoop/yarn/timeline" ]

COPY start.sh start.sh

RUN chmod +x start.sh

EXPOSE 8188

CMD [ "./start.sh" ]