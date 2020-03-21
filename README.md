# currency exchange

### lesson 1
1. Install django debug toolbar
2. path('auth/', include('django.contrib.auth.urls'))


# run celery-beat /src 
celery -A currency_exchange beat
# run celery /src 
celery -A currency_exchange worker -l info

# compose docker image based on dc.yml configuration
docker-compose -f dc.yml up -d

# check currently rinning docker images
docker ps -a

# listen to processes on ports
sudo lsof -i -P -n | grep LISTEN

# Stop gunicorn (the same with diff word for start and restart)
sudo supervisorctl stop gunicorn

# random image
https://loremflickr.com/320/240/dog

# enter the docker container's bash
docker exec -it <containerId> bash

# site with class-based views
http://ccbv.co.uk/

# check logs in container

# if project doesn't work and loads before the DB
docker-compose -f dc.yml restart backend

# run server on docker on different port
docker exec -it backend python src/manage.py runserver 0:8001

# questions for 22.03
# 1) not sure if behaviour of index is correct
# 2) can't load profile page (however i see new users)
# 3) can't load site with 8000, but it loads with 8001
# 4) celery doesn't work anymore
