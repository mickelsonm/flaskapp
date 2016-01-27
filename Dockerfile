FROM ubuntu:14.04

#sets up system dependencies
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev build-essential

#moves source files inside the container
COPY src/ /src
WORKDIR /src

#installs the app dependencies
RUN pip install -r requirements.txt

#exposes port 5000
EXPOSE 5000

#starts up the application
ENTRYPOINT ["python"]
CMD ["app.py"]
