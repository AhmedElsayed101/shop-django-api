# Bit68

## Development mode

### Prepare environment

- Copy `example.dev.env` to `dev.env`

- Adapt `dev.env`

```ini
COMPOSE_PROJECT_NAME=<APP-NAME>

PYTHON_VERSION=<3.0|3.9>
BROADCAST_PORT_BACKEND=<APP-PORT>
```

- Start development container

```sh
docker-compose -f docker-compose.dev.yml --env-file dev.env up -d
```

- Connect to it

```sh
docker-compose -f docker-compose.dev.yml --env-file dev.env exec backend /bin/bash
``` 

- Start application

```sh
pip install virtualenv
virtualenv ./env
source ./env/bin/activate
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
``` 

## Production mode

### Adapt .env

- Copy `example.env` to `.env`

- Adapt `.env`

```ini
APP_NAME=<APP-NAME>
APP_VERSION=<APP-VERSION>

SECRET_KEY=secret
BROADCAST_PORT_BACKEND=<APP-PORT>
```

### Build image

```sh
make build
```

### Publish image

```sh
make publish
```

### Test it

```sh
docker-compose -f docker-compose.yml up -d
```
