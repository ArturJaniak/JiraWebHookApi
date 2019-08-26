from models.slack import SlackRequest


class SlackRequestAttachmentsActionsMongoMapper:
    class Fields:
        TYPE = 'type'
        TEXT = 'text'
        URL = 'url'
        STYLE = 'style'

    @classmethod
    def to_mongo(cls, action):
        return {
            cls.Fields.TYPE: action.type,
            cls.Fields.TEXT: action.text,
            cls.Fields.URL: action.url,
            cls.Fields.STYLE: action.style
        }


class SlackRequestAttachmentsMongoMapper:
    class Fields:
        COLOR = 'color'
        TITLE = 'title'
        TEXT = 'text'
        ACTIONS = 'actions'
        FOOTER = 'footer'
        FOOTER_ICON = 'footer_icon'

    @classmethod
    def to_mongo(cls, attachment):
        return {
            cls.Fields.COLOR: attachment.color,
            cls.Fields.TITLE: attachment.title,
            cls.Fields.TEXT: attachment.text,
            cls.Fields.ACTIONS: [SlackRequestAttachmentsActionsMongoMapper.to_mongo(item) for item in
                                 attachment.actions],
            cls.Fields.FOOTER: attachment.footer,
            cls.Fields.FOOTER_ICON: attachment.footer_icon
        }


class SlackRequestMongoMapper:
    class Fields:
        TEXT = 'text'
        CREATED_DATE = 'created_date'
        UPDATED_DATE = 'updated_date'
        ATTACHMENTS = 'attachments'

    @classmethod
    def to_mongo(cls, data: SlackRequest):
        return {
            cls.Fields.TEXT: data.text,
            cls.Fields.CREATED_DATE: data.created_date,
            cls.Fields.UPDATED_DATE: data.updated_date,
            cls.Fields.ATTACHMENTS: [SlackRequestAttachmentsMongoMapper.to_mongo(item) for item in data.attachments]
        }

    @classmethod
    def from_mongo(cls):
        pass
