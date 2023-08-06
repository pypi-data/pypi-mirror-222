import requests
from .. import config
from .. import tools


# 请求获取models的api并返回内容
def get_models() -> str:

    header = {
        "Accept-Encoding": "gzip",
        "Content-Type": "application/json",
        "X-Omni-Key": config.API_KEY
    }

    response = requests.get(config.endpoint + "v2/models", headers=header)
    tools.response_check(response)
    return response.content.decode("utf-8")
