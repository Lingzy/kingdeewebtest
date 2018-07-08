"""
添加自定义断言，断言失败抛出AssertionError
"""


def assertHTTPCode(response, code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list=[200]
    if res_code not in code_list:
        raise AssertionError('status code not in list')

