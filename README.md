# IRM
Image Recognition Microservice

Image Recognition Microservice (IRM) is an open source microservice used for classifying images. Images are uploaded through http(s)
POST requests using form-data encoding. Form-data encoding includes the following (key, value) pairs:

("file", image_file)

Backend image classification uses Google's Tensorflow library. IRM was developed to be used by students at the University of Utah while
creating Android/iOS augmented reality apps.

## Requirements

IRM requires python 2.7.11+ in addition to the following python dependencies:

- PyPi PIP
- [Tensorflow](https://www.tensorflow.org/)
- flask-restful (pip package)

Additional model files are also needed for classification:

- classify_image_graph_def.pb
- imagenet_2012_challenge_label_map_proto.pbtxt
- imagenet_synset_to_human_label_map.txt

Model files can be obtained by downloading and extracting the following file:

- http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz

## Installation

Installation provides two pipelines: [Docker](http://docker.com/) and manual.

### Docker Installation

IRM provides one Dockerfile:

- Dockerfile

which can be used to create a Docker image and an associated container. Following are the instructions to follow:

- Install Docker on your machine.

- Build Docker image.

```bash
$ docker build --tag TagNameGoesHere .
```

- Create/Run Docker container from previously built Docker image.

```bash
$ docker run -it -p 5000:5000 -d TagNameGoesHere
```

## Manual Installation

Manual installation follows closely the requirements identified in the Requirements section.
Furthermore, required model files should be placed in a directory named "models" relative to the project's root directory.

## Notes

Please read over bugs.txt as it relates to current issues when working with Tensorflow 0.7.1.
