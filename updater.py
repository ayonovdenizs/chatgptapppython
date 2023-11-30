import requests

def check_version():
    # URL вашего репозитория на GitHub
    github_repo_url = 'https://api.github.com/repos/ayonovdenizs/chatgptapppython/releases/latest'

    try:
        response = requests.get(github_repo_url)
        response.raise_for_status()

        latest_release = response.json()
        latest_version = latest_release['tag_name']

        print(f'Локальная версия: 1.0.0')
        print(f'Последняя версия на GitHub: {latest_version}')

        if latest_version != '1.0.0':
            print('Доступна новая версия! Рекомендуется обновиться.')
        else:
            print('У вас последняя версия.')

    except requests.exceptions.RequestException as e:
        print(f'Произошла ошибка при запросе к GitHub: {e}')

if __name__ == "__main__":
    check_version()
