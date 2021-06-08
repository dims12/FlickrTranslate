Перевод на русский подписей корпуса Flickr8k

1) Перевод уже включён в проект

2) Для самостоятельного повторения процедуры

а) Скачайте корпус Flickr8k

- например, командами

```shell
    wget -q https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip
    unzip -qq Flickr8k_text.zip
```

б) Создайте себе доступ к Cloud Translate API, в частности

- это должно привести к скачиванию JSON файла куда-то на локальный компьютер

- укажите путь к этому файлу в переменной среды `GOOGLE_APPLICATION_CREDENTIALS`

- подробности должны быть на [страницах документации Гугл](https://cloud.google.com/translate/docs/setup#creating_service_accounts_and_keys).

в) запустите программу

```shell
python translate3.py
```

У меня процедура перевода заняла около 1 часа, скорость перевода составила около 10 фраз в секунду, всего было переведено 40k фраз (по данным tqdm и метрик Гугла)