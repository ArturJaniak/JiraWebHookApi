import datetime

from models.slack import SlackRequestAttachmentsActions, SlackRequestAttachments, SlackRequest


class SlackRequestAttachmentsActionJsonMapper:
    class Fields:
        TYPE = 'type'
        TEXT = 'text'
        URL = 'url'
        STYLE = 'style'

    @classmethod
    def to_json(cls, action):
        return {
            cls.Fields.TYPE: action.type,
            cls.Fields.TEXT: action.text,
            cls.Fields.URL: action.url,
            cls.Fields.STYLE: action.style
        }


class SlackRequestAttachmentsJsonMapper:
    class Fields:
        COLOR = 'color'
        TITLE = 'title'
        TEXT = 'text'
        ACTIONS = 'actions'
        FOOTER = 'footer'
        FOOTER_ICON = 'footer_icon'

    @classmethod
    def to_json(cls, attachment):
        return {
            cls.Fields.COLOR: attachment.color,
            cls.Fields.TITLE: attachment.title,
            cls.Fields.TEXT: attachment.text,
            cls.Fields.ACTIONS: [SlackRequestAttachmentsActionJsonMapper.to_json(item) for item in
                                 attachment.actions],
            cls.Fields.FOOTER: attachment.footer,
            cls.Fields.FOOTER_ICON: attachment.footer_icon
        }


class SlackRequestJsonMapper:
    class Fields:
        TEXT = 'text'
        CREATED_DATE = 'created_date'
        UPDATED_DATE = 'updated_date'
        ATTACHMENTS = 'attachments'

    @classmethod
    def to_json(cls, data: SlackRequest):
        return {
            cls.Fields.TEXT: data.text,
            cls.Fields.CREATED_DATE: data.created_date,
            cls.Fields.UPDATED_DATE: data.updated_date,
            cls.Fields.ATTACHMENTS: [SlackRequestAttachmentsJsonMapper.to_json(item) for item in data.attachments]
        }


class JiraRequestJsonMapper:
    @classmethod
    def from_json(cls, data):
        attachments_actions_text = data["issue"]["key"]
        attachments_actions_url = data["issue"]["key"]

        attachments_title = data["issue"]["fields"]["summary"]
        attachments_text = data["issue"]["fields"]["description"]

        text = (data["issue"]["fields"]["project"]["key"] +
                data["issue"]["fields"]["project"]["name"])

        action = SlackRequestAttachmentsActions("button", attachments_actions_text,
                                                "config" + attachments_actions_url, "primary")
        attachment = SlackRequestAttachments("#000000", attachments_title,
                                             attachments_text, [action],
                                             "Powered by Maio Software House",
                                             "Tu miejsce na configa")
        created_date = f"{datetime.datetime.now()}"
        updated_date = created_date
        slack_req = SlackRequest("Nowe zgłoszenie w projekcie " + text, [attachment], created_date, updated_date)

        return slack_req
