import requests

def check_version(version):
    # URL вашего репозитория на GitHub
    github_repo_url = 'https://api.github.com/repos/ayonovdenizs/chatgptapppython/releases/latest'

    try:
        response = requests.get(github_repo_url)
        response.raise_for_status()

        latest_release = response.json()
        latest_version = latest_release['tag_name']

        print(f'Updater: Локальная версия: {version}')
        print(f'Updater: Последняя версия на GitHub: {latest_version}')

        if latest_version != version:
            print('Updater: Доступна новая версия! Рекомендуется обновиться.')
            return True
        else:
            print('Updater: У вас последняя версия.')
            return False

    except requests.exceptions.RequestException as e:
        print(f'Updater: Произошла ошибка при запросе к GitHub: {e}')

if __name__ == "__main__":
    check_version()
