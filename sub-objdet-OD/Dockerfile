FROM ubuntu:18.04

# Increase to refresh the build
ARG REFRESHED=2

RUN apt-get update
RUN apt-get install -y git python-pip

COPY requirements.txt /challenge-solution/requirements.txt
RUN pip install -r /challenge-solution/requirements.txt

COPY /example_detector/* /challenge-solution/

COPY solution.py /challenge-solution
CMD python /challenge-solution/solution.py
