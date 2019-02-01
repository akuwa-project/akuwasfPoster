FROM python:3
MAINTAINER Jean-Baptiste GANDONOU (jean.gandonou@rintio.com)
ADD . /
RUN pip3 install pymongo
RUN pip3 install flask
RUN pip3 install flask_restplus
RUN pip3 install api
CMD [ "python3", "entre_swagger.py" ]
