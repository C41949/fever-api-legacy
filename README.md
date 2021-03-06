<h1 align="center">Welcome to TemperatureAPI 👋</h1>

<p align="center">
  <img src="./.images/temperature.png" />
</p>

> Just a study using flask for raspberry temperature monitoring

## Why?

> The idea is to use this project to study Flask and related technologies.

## What?
This is a summary of the project goals:
- [x] Create an api with the following endpoints
  - [x] Get the current temperature
  - [x] Get the current temperature
  - [x] Get a list of previous temperatures
---
- [ ] Enhance the list endpoint
  - [ ] Accept a date range as parameter
  - [ ] Adapt a list of previous temperatures with a default range to prevent querying all database
---
- [ ] Create an endpoint to count days
  - [ ] Count days with temperatures with specific interval
    - ex: `param = 3`,  `response = { 50-52: { qtd: 3, data: [] }, 53-55: { qtd: 2, data: [] }  }`
---
- [ ] Add info about quantity of processes
  - [ ] Adds 'quantity of processes at that moment' when temperature is measured
---
- [ ] Add info about quantity of processes
  - [ ] Adds a `Process` entity, and save the top ones at the measurement moment

## Related
- [temperature-worker](.)
    - 🚧
- [temperature-dashboard](.)
    - 🚧

## Usage

```sh
python3 -m venv api_env
source api_env/bin/activate
pip install -r req.txt
python app.py
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
