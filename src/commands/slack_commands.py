import json

import requests

from mappers.jira_mapper import SlackRequestJsonMapper
from models.slack import SlackRequest
from repositories.slack_repo import SenderRepository
from flask import current_app as app


class SlackRequestInsertCommand:
    @classmethod
    def execute(cls, obj: SlackRequest):
        SenderRepository.insert(obj)


class SlackRequestWebHookCommand:
    @classmethod
    def execute(cls, obj: SlackRequestJsonMapper):
        dict_to_string = json.dumps(obj)
        string_to_bytes = str.encode(dict_to_string)
        requests.post(app.config['SLACK_URL'],
                      data=string_to_bytes, json=obj)
        return "ok"
