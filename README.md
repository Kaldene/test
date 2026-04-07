

## Repository structure
```text
.
├── .github/workflows/quality.yml
├── .pylintrc
├── .coveragerc
├── calculator.py
├── requirements.txt
├── tests/
│   └── test_calculator.py
└── README.md
```

## Local запуск
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pylint calculator.py tests/test_calculator.py
pytest --cov=. --cov-report=term-missing --cov-report=html
bandit -r . -x ./tests --skip B101
```

### Скриншот успешного запуска
<img width="690" height="204" alt="image" src="https://github.com/user-attachments/assets/922aa16c-37cb-45c2-b266-71eb2f6a3e0b" />


### Скриншот неуспешного запуска
<img width="1321" height="143" alt="image" src="https://github.com/user-attachments/assets/5d1abb5a-4e2c-4e94-9934-f78a76a9f980" />


### Пример Quality Gate
Например, можно показать:
- падение workflow при coverage < 70%;
- падение workflow при ошибке линтера;
- падение workflow при failing test.

### Вывод
Автоматизация позволила проверять качество проекта при каждом push и pull request.
Благодаря pipeline проблемы со стилем, тестами и покрытием выявляются до merge.
Основные сложности обычно связаны с настройкой GitHub Actions, зависимостей и
корректной конфигурацией quality gates.
