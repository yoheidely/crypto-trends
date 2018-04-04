# -*- coding: utf-8 -*-
import json
import requests
from pytrends.request import TrendReq

CHANNEL = '#検索キーワード'
WEBHOOK_URL = 'TODO'
USERNAME = u'Google Trend Bot'
KEYWORDS = [u'仮想通貨', u'ビットコイン', u'取引所', u'ネム', u'リップル', u'仮想通貨リスク', u'イーサリアム']


def post_message(keyword):
    pytrends = TrendReq(hl='ja-JP', tz=540)
    pytrends.build_payload([keyword], timeframe='now 4-H', geo='JP')

    trends = list(pytrends.related_queries().values())[0]
    top_queries = trends.get('top')
    rising_queries = trends.get('rising')

    text = u''

    if rising_queries is not None and not rising_queries.empty:
        text += u'[%s] Rising queries\n' % keyword
        for index, top_query in rising_queries.iterrows():
            text += u'%2s. %3s%% \u2191  %s\n' % (
                index + 1, top_query.value, top_query.query
            )
        text += u'\n\n'

    if top_queries is not None and not top_queries.empty:
        text += u'[%s] Top queries\n' % keyword
        for index, top_query in top_queries.iterrows():
            text += u'%2s. %3s%%  %s\n' % (
                index + 1, top_query.value, top_query.query
            )

            slack_data = {
                'text': text,
                'channel': CHANNEL,
                'username': USERNAME
            }

    requests.post(
        WEBHOOK_URL,
        data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )


if __name__ == '__main__':
    for keyword in KEYWORDS:
        post_message(keyword)
