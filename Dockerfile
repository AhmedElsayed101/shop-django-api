# using ubuntu LTS version
FROM ubuntu:20.04 AS builder-image

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get -y install --no-install-recommends \
	python3.9 \
	python3.9-dev \
	python3.9-venv \
	python3-pip \
	python3-wheel \
	build-essential \
	git \
	sudo \
  # Cleanup
  && apt-get -y autoremove && apt-get clean autoclean && rm -rf /var/lib/apt/lists/*

# create and activate virtual environment
# using final folder name to avoid path issues with packages
RUN python3.9 -m venv /home/docker/venv
ENV PATH="/home/docker/venv/bin:$PATH"

# install requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

FROM ubuntu:20.04 AS runner-image
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	python3.9 \
	python3-venv \
  # Cleanup
  && apt-get -y autoremove && apt-get clean autoclean && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home docker
RUN adduser docker sudo
# Users in the sudoers group can sudo as root without password.
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

COPY --from=builder-image /home/docker/venv /home/docker/venv

USER docker
RUN mkdir /home/docker/app
WORKDIR /home/docker/app


COPY ./try_shop/ .

EXPOSE 8000

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1

# activate virtual environment
ENV VIRTUAL_ENV=/home/docker/venv
ENV PATH="/home/docker/venv/bin:$PATH"

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# /dev/shm is mapped to shared memory and should be used for gunicorn heartbeat
# this will improve performance and avoid random freezes
# CMD ["gunicorn", "--preload","-b", "0.0.0.0:8080", "-w", "3", "-k", "gevent", \

# CMD ["gunicorn","-b", "0.0.0.0:8080", "-w", "3", "-k", "gevent", \
# 	"--worker-tmp-dir", "/dev/shm", "--timeout", "1000", \
# 	"--log-level", "debug", "--access-logfile", "-", "--error-logfile", "-", \
# 	"app:app"]
