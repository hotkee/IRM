FROM python:3.4

MAINTAINER <matt.j.alexander@utah.edu>

# See bugs.txt for explanation
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION python

# Install PIP, TensorFlow, Flask-RESTful
RUN pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.7.1-cp34-none-linux_x86_64.whl
RUN pip3 install flask-restful

# Copy application to appropriate directory
COPY . /IRM/

# If model not available locally pull down
WORKDIR /IRM/scripts
RUN chmod +x install-inception-v3.sh
RUN ./install-inception-v3.sh

# Expose flask port
EXPOSE 5000

# Run app
WORKDIR /IRM
CMD ["python", "irm.py"]