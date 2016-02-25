FROM python:2.7.11
MAINTAINER <matt.j.alexander@utah.edu>

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION python

RUN pip install --upgrade pip
RUN pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.7.1-cp27-none-linux_x86_64.whl
RUN pip install flask-restful

COPY . /imagenet/

ADD http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz /imagenet/models/

EXPOSE 5000

CMD ["python", "/imagenet/tpc.py"]