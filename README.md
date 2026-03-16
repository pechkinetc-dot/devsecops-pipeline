# DevSecOps Pipeline - Дипломная работа

## Описание
Безопасный CI/CD пайплайн для open-source проекта с интеграцией:
- **SAST** (статический анализ кода)
- **DAST** (динамический анализ безопасности)
- **Security Gateway** (автоматическая блокировка релизов)
- **Проверка на секреты** (секреты в коде)

## Целевой проект
**DefectDojo** (django-DefectDojo)
- Open-source платформа для управления уязвимостями
- Стек: Python (Django) + PostgreSQL + Valkey
- GitHub: https://github.com/DefectDojo/django-DefectDojo

## Стек технологий
| Категория | Инструмент |
|-----------|------------|
| CI/CD | GitHub Actions |
| SAST | Bandit, CodeQL, Semgrep |
| DAST | OWASP ZAP |
| Secrets | GitLeaks, TruffleHog |
| Containers | Trivy, Docker Scan |
| SCA | Dependency-Check, pip-audit |

## Структура репозитория
