import argparse
from config import get_cfg
import flask

from flask import request
from commands.slack_commands import SlackRequestWebHookCommand
from mappers.jira_mapper import JiraRequestJsonMapper, SlackRequestJsonMapper

app = flask.Flask(__name__)


@app.route('/jira-webhook', methods=['POST'])
def launch_jira_request_handler():
    obj = JiraRequestJsonMapper.from_json(request.get_json())
    # obj = SlackRequestInsertCommand.execute(obj))
    obj = SlackRequestJsonMapper.to_json(obj)
    obj = SlackRequestWebHookCommand.execute(obj)
    return obj


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='app.py')
    parser.add_argument('-c', dest='config')
    args = parser.parse_args()

    cfg = get_cfg(args.config)
    app.config.from_object(cfg)
    print(f"Server launching with {cfg.__class__.__name__}")
    app.run()
