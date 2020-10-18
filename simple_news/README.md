
Clone repo - git clone https://github.com/FabelVlad/test-assessment.git

in directory `simple_news` make file `.env` (or just rename `.env.example`)
set up env variables like in `.env.example`
set DJANGO_DEBUG `on` or `off` and DJANGO_USE_HEROKU `off` for local develop
 
Docker
- make sure that docker is running - type `docker ps` in command line
- from directory `test_assessment` run `docker-compose up` command
- open `http://localhost:1337/api/v1/` in your browser
- run `docker-compose exec web python manage.py createsuperuser` (do not forget login and password, use it in Postman auth)

Heroku
- link **`https://simple-news-z.herokuapp.com/api/v1/`**

- make sure that you have Heroku CLI
- set DJANGO_DEBUG `off` and DJANGO_USE_HEROKU `on` in `.env`
- from directory `simple_news` run next commands:
  - heroku login
  - heroku container:login
  - heroku create `app_name`
  - heroku addons:create heroku-postgresql:hobby-dev -a `app_name` #  attache an application to Postgres
  - heroku addons:create heroku-redis:hobby-dev -a `app_name` #  attache an application to Redis
  - heroku container:push web -a `app_name`
  - heroku container:release web -a `app_name`
  - heroku run python manage.py migrate -a `app_name`
  - heroku run python manage.py createsuperuser -a `app_name` (do not forget login and password, use it in Postman auth)
- open `https://app_name.herokuapp.com/api/v1/`
 
Postman
