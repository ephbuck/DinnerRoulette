FROM python:3

# Set timezone info
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Add a user and switch, using the default root user is BAD
RUN adduser --home /home/flask flask
USER flask
WORKDIR /home/flask
RUN mkdir -p flask_app
WORKDIR /home/flask/flask_app 
RUN chmod -R 755 ./

COPY --chown=flask . .
RUN chmod -R 755 ./

# RUN PIP to install all packages listed in req.txt
RUN pip install --no-cache-dir -r requirements.txt

# CMD tells the docker to run the following command
CMD ["python", "server.py"]
