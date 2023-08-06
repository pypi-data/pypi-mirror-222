# -*- coding: utf-8 -*-
"""
@author: fangjin
@time: 2023/8/3 11:33
@file: __init__.py
@desc:  
@Software: PyCharm
"""
import inspect


def pytest_addoption(parser):
    """添加参数名称"""
    # 添加参数分组
    group = parser.getgroup('pytest-autotest')
    # 添加参数和帮助信息
    group.addoption('--collect-only-appoint-info', default="False", help='指定手机用例特定西悉尼', type="string")


def pytest_collection_finish(session):
    collect_only_appoint_info = session.config.getoption('--collect-only-appoint-info')
    if collect_only_appoint_info == "True":
        config = session.config
        config.option.collectonly = True
        for item in session.items:
            git_local_path = item.config.args[0]
            author = ""
            case_id = ""
            title = item.function.__allure_display_name__
            node_id = item.nodeid
            function_name = item.name
            try:
                function_code = inspect.getsource(item.obj)
            except Exception:
                function_code = "未获取到源代码"
            case_description = ""
            severity = ""
            directory = ""
            other_marker_info = []
            for marker in item.iter_markers():
                if marker.name == "allure_description":
                    case_description = marker.args[0]
                elif marker.name == "allure_label":
                    if marker.kwargs.get("label_type") == "as_id":
                        case_id = marker.args[0]
                    elif marker.kwargs.get("label_type") == "author":
                        author = marker.args[0]
                    elif marker.kwargs.get("label_type") == "severity":
                        severity = marker.args[0]
                    elif marker.kwargs.get("label_type") == "directory":
                        directory = marker.args[0]
                    else:
                        other_marker_info.append((marker.kwargs.get("label_type"), marker.args[0]))
                else:
                    pass

            print(
                {"git_local_path": git_local_path, "author": author, "case_id": case_id,
                 "title": title, "node_id": node_id,
                 "function_name": function_name, "case_description": case_description,
                 "severity": severity, "function_code": function_code,
                 "other_marker_info": other_marker_info, "directory": directory}
            )
