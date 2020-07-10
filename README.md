# uso-lab-book

## Prerequisites

### Installing on your own computer

In order to build the documentation you will need the following packages:

```
python3-pip
ditaa
graphiz
```

For debian-based installs, you can install them by using:

```
# apt-get install python3-pip ditaa graphiz
```

In order do build the rest of the documentation, you will need to install them
using pip3 by running the following command in the repo directory:

```
pip3 -r requirements.txt
```

### Installing inside of docker

In order to compile the documentation inside a docker image, you need to have
installed `docker` and `docker-compose`. The installation method depends on the
distribution you're running.

## Building the documentation

### Building the documentation on the host computer

To build the documentation on your host OS, you will need to run the following
command in the root directory of the repo:

```
make html
```

### Building the documentation using containers

To build the documentation using containers, you will need to run the following
command in the root directory of the repo:

```
make docker-build
```

The above command will take more time on your first run, since it will build the
containers.
