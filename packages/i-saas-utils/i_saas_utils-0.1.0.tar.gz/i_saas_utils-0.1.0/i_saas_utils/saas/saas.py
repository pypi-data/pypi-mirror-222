import json
import os
import sys
import urllib.parse
from importlib import import_module
from random import shuffle

import dns.resolver
import requests


def get_list_dirs(path: str):
    return list(filter(os.path.isdir, os.listdir(path)))


def get_list_files(source: str, short_name: bool = False) -> list[str]:
    list_files = []
    for path, dirs, files in os.walk(source):
        if short_name:
            short_path = os.path.relpath(path, source)
        else:
            short_path = path

        for file in files:
            list_files.append(os.path.join(short_path, file))
    return list_files


def choice_action(
    action: str = None,
    data: dict | None = None,
    path: str = "actions",
    file_name: str = "main",
    function_name: str = "main",
):
    if action is None:
        if len(sys.argv) == 1:
            raise Exception("Action not found")
        action = sys.argv[1]
    if data is None:
        data = os.getenv("SAAS_DATA")
        if not data:
            raise Exception("Data not found")
        data = json.loads(data)

    list_dirs = get_list_dirs(path)

    if action in list_dirs:
        import_module(f"{action}.{file_name}").__getattr__(function_name)(data)
    else:
        raise Exception(f"ERROR POSSIBLE ACTION {list_dirs}")


def check_exists_hostname(hostname: str, is_url: bool = False):
    if is_url:
        parsed_url = urllib.parse.urlparse(hostname)
        hostname = parsed_url.hostname
    try:
        return dns.resolver.resolve(hostname, raise_on_no_answer=False)
    except dns.resolver.NXDOMAIN:
        return None


def generate_new_hostname(
    hostname: str, suffix: list[str], count: int = 1, ignore: list[str] | None = None
):
    if ignore is None:
        ignore = []
    shuffle(suffix)

    cur_suffix = 0
    suffix_shift = [0 for _ in range(len(suffix))]

    answers = []
    while count > 0:
        new_hostname = f"{hostname}-{suffix_shift[cur_suffix]}.{suffix[cur_suffix]}"
        while check_exists_hostname(new_hostname) or new_hostname in ignore:
            suffix_shift[cur_suffix] += 1
            new_hostname = f"{hostname}-{suffix_shift[cur_suffix]}.{suffix[cur_suffix]}"
        answers.append(new_hostname)

        suffix_shift[cur_suffix] += 1
        cur_suffix = (cur_suffix + 1) % len(suffix)

        count -= 1
    return answers


class TeleGram:
    def __init__(self, bot_token: str, default_chat_id: str | None):
        self.token = bot_token
        self.default_chat_id = default_chat_id
        self.url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    def send_notification(self, message: str, chat_id: str | None = None):
        if chat_id is None:
            chat_id = self.default_chat_id

        payload = {"chat_id": chat_id, "text": message}
        response = requests.post(self.url, data=payload)

        if response.status_code != 200:
            raise Exception(f"Can't send notify - {response.text}")
