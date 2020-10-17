FROM rabbitmq:3

# Define environment variables.
ENV RABBITMQ_USER user
ENV RABBITMQ_PASSWORD user
ENV RABBITMQ_PID_FILE /var/lib/rabbitmq/mnesia/rabbitmq

COPY . /queue
WORKDIR /queue
ADD ./init.sh /queue/init.sh
RUN chmod +x /queue/init.sh

# Define default command
CMD ["./init.sh"]
