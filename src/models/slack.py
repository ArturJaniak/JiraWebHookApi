from datetime import datetime
from typing import List


class SlackRequestAttachmentsActions:
    def __init__(self,
                 type: str,
                 text: str,
                 url: str,
                 style: str):
        self.type = type
        self.text = text
        self.url = url
        self.style = style


class SlackRequestAttachments:
    def __init__(self,
                 color: str,
                 title: str,
                 text: str,
                 actions: List[SlackRequestAttachmentsActions],
                 footer: str,
                 footer_icon: str):
        self.color = color
        self.title = title
        self.text = text
        self.actions = actions
        self.footer = footer
        self.footer_icon = footer_icon


class SlackRequest:
    def __init__(self,
                 text: str,
                 attachments: List[SlackRequestAttachments],
                 created_date: datetime,
                 updated_time: datetime):
        self.text = text
        self.attachments = attachments
        self.created_date = created_date
        self.updated_date = updated_time
