# CI/CD Quality Pipeline for Python Project

## Project goal
This repository demonstrates an automated quality-control pipeline in GitHub Actions.
The pipeline checks code style, runs unit tests, validates test coverage, performs a
security scan, and saves reports as artifacts.

## Implemented checks

### 1. Linting
- Tool: `pylint`
- Line length limit: 100 characters
- Unused imports and variables are treated as violations
- Quality gate: pylint score must be at least `7.0`

### 2. Unit tests
- Tool: `pytest`
- Number of tests: 6
- Main business logic is covered
- If at least one test fails, the workflow fails

### 3. Coverage check
- Tool: `pytest-cov`
- Quality gate: coverage must be at least `70%`
- HTML coverage report is generated and uploaded as an artifact

### 4. Automatic report
- `quality-report.md` is generated in CI
- `htmlcov/` and `quality-report.md` are uploaded as GitHub Actions artifacts

## Extra tasks for a higher grade
Two additional improvements were added:
1. **SAST / security scan** using `bandit`
2. **Artifact-based reporting** with a generated quality summary file

> If your teacher strictly counts the second extra point only from the list in the task,
> replace the second improvement with PR comments or mutation testing.

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

## Что нужно добавить перед сдачей
После публикации репозитория на GitHub добавь в README:
- скриншот **успешного** запуска workflow;
- скриншот **неуспешного** запуска workflow;
- пример сработавшего Quality Gate;
- краткий вывод по автоматизации и возникшим сложностям.

Ниже можно вставить подготовленные разделы.

### Скриншот успешного запуска
_Вставить изображение после первого успешного прогона._

### Скриншот неуспешного запуска
_Вставить изображение после намеренно сломанного теста или нарушения линтера._

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
