# -*- coding: utf-8 -*-

from slack_sdk import WebClient

class SlackAPI:
    """
    슬랙 API 핸들러
    """
    def __init__(self, token):
        self.client = WebClient(token)
        
    def get_channel_id(self, channel_name):
        """
        슬랙 채널ID 조회
        """
        result = self.client.conversations_list(limit=5)
        channels = result.data['channels']
        next_cursor = result.data['response_metadata']['next_cursor']
        channel = list(filter(lambda c: c["name"] == channel_name, channels))
        while len(channel) == 0:
            result = self.client.conversations_list(limit=100, cursor=next_cursor)
            print(result)
            channels = result.data['channels']
            next_cursor = result.data['response_metadata']['next_cursor']
            channel = list(filter(lambda c: c["name"] == channel_name, channels))
        channel_id = channel[0]["id"]
        return channel_id

    def get_message_ts(self, channel_id, query):
        """
        슬랙 채널 내 메세지 조회
        """
        result = self.client.conversations_history(channel=channel_id)
        messages = result.data['messages']
        message = list(filter(lambda m: m["text"]==query, messages))[0]
        message_ts = message["ts"]
        return message_ts

    def post_thread_message(self, channel_id, message_ts, text):
        """
        슬랙 채널 내 메세지의 Thread에 댓글 달기
        """
        result = self.client.chat_postMessage(
            channel=channel_id,
            text = text,
            thread_ts = message_ts
        )
        return result

    def post_just_message(self, channel_id, text):
        result = self.client.chat_postMessage(
            channel=channel_id,
            text = text   
        )
        return result #result.ts

    def read_tr_message(self, channel_id, message_ts):
        result = self.client.conversations_replies(
            channel=channel_id,
            ts=message_ts
        )
        return result