<h1 align="center">Welcome to fever-api :fire: </h1>

<p align="center">
  <img src="./.images/fever-api.png" />
</p>

> Just a study using flask for raspberry temperature monitoring

## Why ❓

> The idea is to use this project to study Flask and related technologies.

## Roadmap 🗺️
This is a summary of the project goals:

---
Basic structure
- [x]  Get the current temperature
- [x]  Create an object with the current temperature
- [x]  Get a list of previous temperatures
---

Deployment
- [x]  Adds deploy with docker
---

Database
- [x] Adds a real database, PostgreSQL or similar
---

Enhance the list endpoint
- [x]  Accept a date range as parameter
- [x]  Adapt a list of previous temperatures with a default range to prevent querying all database
---

Add info about quantity of processes
- [ ]  Adds 'quantity of processes at that moment' when temperature is measured
---

Add cached default endpoints

- [ ]  Last hour
- [ ]  Last 24 hours
- [ ]  Last week
- [ ]  Last month
- [ ]  Average values for each one
---

## Related
- [🚒 fever-dashboard](https://github.com/C41949/fever-dashboard)

## Usage

Coding
```sh
python3 -m venv api_env
source api_env/bin/activate
pip install -r req.txt
python wsgi.py
```

Deploy
```sh
make measure
```

## Author

👤 **Vinicius Kammradt**

* [Website](https://kammradt.now.sh)
* [Twitter](https://twitter.com/kammzinho)
* [Github](https://github.com/kammradt)
* [LinkedIn](https://linkedin.com/in/vinicius-kammradt)

## Show your support

Give a ⭐️ if this project helped you!

***
