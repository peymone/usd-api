<h1 align="center">USD API</h1>

<p align="center">
    <img src="https://img.shields.io/badge/%20Python-3.11.3-blue?style=for-the-badge&logo=Python" alt="Python">
    <img src="https://img.shields.io/badge/%20Django-5.1.3-brightgreen?style=for-the-badge" alt="Django">
    <img src="https://img.shields.io/badge/%20requests-2.32.3-brightgreen?style=for-the-badge" alt="requests">
    <img src="https://img.shields.io/badge/%20tzlocal-5.2-brightgreen?style=for-the-badge" alt="tzlocal">
</p>

<p align="center">
    <img src="https://img.shields.io/github/downloads/peymone/usd-api/total?style=social&logo=github" alt="downloads">
    <img src="https://img.shields.io/github/watchers/peymone/usd-api" alt="watchers">
    <img src="https://img.shields.io/github/stars/peymone/usd-api" alt="stars">

<h2>About</h2>

_**Another test task. Here are the details:**_

```

Create a basic Django project that, when calling "/get-current-usd/", will return the current dollar to ruble exchange rate in JSON format and the last 10 rate requests.

To get the rate, use an external API (choose the appropriate one yourself). There should be a pause of at least 10 seconds between each rate request.

```

_P.S. I think that using API in this case is inappropriate, since registration + paid tariff is required. Therefore, I did it with the help of parser. What is the purpose of the delay between requests?_

<h2>Deployment</h2>

- _Clone repo:_ ```git clone https://github.com/peymone/usd-api.git```
- _Create python virtual environment:_ ```python -m venv venv```
- _Activate virtual environment:_ ```venv/scripts/activate```
- _Install dependencies:_ ```pip install -r requirements.txt```
- _Make migrations:_
    - ```python api/manage.py makemigrations```
    - ```python api/manage.py migrate```
- _At last, run server:_ ```python api/manage.py runserver```
- _Go here: <a href="http://127.0.0.1:8000/get-current-usd/">api link</a>_

<br>

> _If you want a normal deployment, do it yourself **OR** hire me_