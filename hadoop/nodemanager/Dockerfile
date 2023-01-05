FROM hadoop-main:latest
LABEL maintainer="Manan Mukim"

COPY start.sh start.sh

RUN chmod +x start.sh

EXPOSE 8042

CMD [ "./start.sh" ]