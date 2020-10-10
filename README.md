# NEX-FLIX

Nex-flix is a mini watchlist apps built on top of Python and Django Framework.


### Technology Stack

* Python
* Django Framework
* PostgreSQL




### Installation

This project requires [Python](https://python.org/) v3+ to run.

Install the dependencies.
```sh
$ cd nex-flix
$ pip3 install -r requirements.tx
```

Migrate model to your local database (require [Postgres](www.postgresql.org) to run), and create .env to define DATABASE_URL config routed to your db instances prior to run this.
```sh
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
Run
```sh
$ python3 manage.py runserver
```

Execute the call
```sh
$ curl localhost:8000/watchlist/
```


### API
Nex-flix is deployed on heroku. the host is [here](https://nex-flix.herokuapp.com)


#### Endpoints

|method | detail | url |
| ------ | ------ | ------ |
|GET| Get Now Playing Movies | [host]/movies/now-playing |
|GET| Get All Watchlist| host]/watchlist/ |
|GET| Get Watchlist by id| host]/watchlist/:id/ |
|POST| Add Movie To Watchlist | [host]/watchlist/ |
|PUT| Update watchlist comment and status by id | [host]/watchlist/:id/ |
|DELETE| Delete from watchlist by id | [host]/watchlist/:id/ |





### Disclaimer
This project is consuming the [TMDb](https://developers.themoviedb.org/) API to fetch Movies data 
,but is not endorsed or certified by TMDb.

