#!/bin/bash

rm /srv/project/src/celerybeat.pid
celery -A currency_exchange beat --workdir=/srv/project/src --pidfile=/srv/project/src/celerybeat.pid