#!/bin/sh

if [ ! -f /IRM/models/inception-2015-12-05.tgz ]
then
  curl http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz -o /IRM/models/inception-2015-12-05.tgz
  tar xzvf /IRM/models/inception-2015-12-05.tgz -C /IRM/models/
  rm /IRM/models/inception-2015-12-05.tgz
else
  tar xzvf /IRM/models/inception-2015-12-05.tgz -C /IRM/models/
  rm /IRM/models/inception-2015-12-05.tgz
fi