import requests
import os

class YaUploader:

    base_host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы file_path на яндекс диск"""
        url = 'v1/disk/resources/upload'
        headers = {"Authorization": f"OAuth {self.token}"}
        response = requests.get(self.base_host + url,
                                params={"path": file_path, "overwrite": "true"},
                                headers=headers)
        upload_url = response.json()["href"]
        with open(file_path, "rb") as f:
            response = requests.put(upload_url, data=f, headers=headers)
        response.raise_for_status()

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'jo.jpeg'
    token = token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)