FROM python:3
MAINTAINER Jean-Baptiste GANDONOU (jean.gandonou@rintio.com)
ADD . /
RUN pip3 install requirements.txt
CMD [ "python3", "entre_swagger.py" ]
