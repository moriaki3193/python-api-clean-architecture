"""
"""
import json
import aiohttp


class ArticleDriverImpl:
    """
    """
    async def get_articles(self, page: int) -> dict:
        url = f'https://qiita.com/api/v2/items?page={page}&per_page=20'
        response = await aiohttp.request('GET', url)._coro
        articles = json.loads(await response.text())
        return {
            'articles': [{
                'id': a['id'],
                'body': a['body'],
            } for a in articles]
        }
