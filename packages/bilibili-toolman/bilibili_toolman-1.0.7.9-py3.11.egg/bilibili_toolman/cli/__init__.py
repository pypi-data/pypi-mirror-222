# -*- coding: utf-8 -*-
import os
import argparse
import logging
import sys
from bilibili_toolman import providers, __version__, __desc__

class AttribuitedDict(dict):
    def __getattr__(self, name):
        return self[name]


pbar = None
global_args = {
    "cookies": {
        "help": "登陆： 使用 Cookies 登陆，即使用 Web API （不可多 P 上传） ( 需要 SESSDATA 及 bili_jct ) e.g.SESSDATA=cb0..; bili_jct=6750..."
    },
    "sms": {
        "help": "登陆：使用短信验证码登陆，即使用 上传助手 API （可多 P 上传）（需手动交互）（有日获取限制，请配合 --save 使用）",
        "default": False,
        "action": "store_true",
    },
    "load": {"help": "登陆：加载凭据，同时用于上传及投稿"},
    "load_upload": {"help": "登陆：使用该凭据上传，而不用--load凭据上传"},
    "load_submit": {"help": "登陆：使用该凭据投稿，而不用--load凭据投稿"},
    "save": {
        "help": "登陆：向stdout输出当前登陆凭据并退出（其他输出转移至stderr）",
        "default": False,
        "action": "store_true",
    },
    "http": {"help": "强制使用 HTTP （不推荐）", "default": False, "action": "store_true"},
    "noenv": {"help": "上传时，不采用环境变量（如代理）", "default": False, "action": "store_true"},
    "cdn": {
        "help": "上传用 CDN （限 Web API) （对应 网宿（适合海外），七牛，百度（默认），七牛，谷歌，百度）",
        "choices": ["ws", "qn", "bda2", "kodo", "gcs", "bos"],
        "default": "bda2",
    },
    "retry_submit_delay" : {"help": "投稿限流时，重新投稿周期", "default": 30},
    "retry_submit_count" : {"help": "投稿限流时，尝试重新投稿次数", "default": 5},
}
local_args = {
    "opts": {"help": "解析可选参数 ，详见 --opts 格式", "default": ""},
    "thread_id": {"help": "分区 ID", "default": 17},
    "tags": {"help": "标签", "default": "转载"},
    "desc": {"help": '描述格式 e.g. "原描述：{desc}" (其他变量详见下文)（仅稿件有描述）', "default": "{desc}"},
    "title": {
        "help": '标题格式 e.g. "[Youtube] {title} (其他变量详见下文)（使用于稿件及分P）"',
        "default": "{title}",
    },
    "seperate_parts": {
        "help": "不分P （e.g. --youtube [播放列表],--localfile [文件夹]）独立投稿（不分P）（Web上传默认不分 P）",
        "default": False,
        "action": "store_true",
    },
    "no_upload": {"help": "只下载资源", "default": False, "action": "store_true"},
    "no_submit": {
        "help": "不提交稿件，适用于获取filename参数",
        "default": False,
        "action": "store_true",
    },
    "original": {"help": "设置稿件为原创", "default": False, "action": "store_true"},
    "no_reprint": {"help": "设置稿件不允许转载", "default": False, "action": "store_true"},
}
arg_epilog = """
变量：
    {title},{desc} 等变量适用于：
        --title, --desc, --tags

通用变量:
    {title}     -       原标题
    {desc}      -       原描述
    {safe_korean_title}
                -       【韩文】替换韩文为特殊字符的标题
    {roma_korean_title}
                -       【韩文】替换韩文为罗马音的标题 (需要安装 korean_romanizer)
本工具支持将给定视频源转载至哔哩哔哩

详见项目 README 以获取更多例程 ： github.com/greats3an/bilibili-toolman
"""


def setup_logging():
    from tqdm.std import tqdm as tqdm_c

    class SemaphoreStdout:
        @staticmethod
        def write(__s):
            # Blocks tqdm's output until write on this stream is done
            # Solves cases where progress bars gets re-rendered when logs
            # spews out too fast
            with tqdm_c.external_write_mode(file=sys.stdout, nolock=False):
                return sys.stdout.write(__s)

    import coloredlogs

    coloredlogs.DEFAULT_LOG_FORMAT = (
        "[ %(asctime)s %(name)8s %(levelname)6s ] %(message)s"
    )
    coloredlogs.install(level=logging.DEBUG, stream=SemaphoreStdout, isatty=True)
    logging.getLogger("urllib3").setLevel(logging.CRITICAL)
    logging.getLogger("PIL.Image").setLevel(logging.CRITICAL)    

def truncate(string, max):
    """truncate & add ... to string over the length of `max`"""
    if len(string) > max:
        string = string[: max - 3] + "..."
    return string

def prepare_temp(temp_path: str):
    if not os.path.isdir(temp_path):
        os.mkdir(temp_path)
    os.chdir(temp_path)
    return True


def report_progress(current, max_val):
    from bilibili_toolman.cli import precentage_progress

    precentage_progress.report(current, max_val)


def _enumerate_providers():
    provider_dict = dict()
    for provider in dir(providers):
        if not "provider_" in provider:
            continue
        provider_name = provider.replace("provider_", "")
        provider_dict[provider_name] = getattr(providers, provider)
    return provider_dict


provider_args = _enumerate_providers()


def _create_argparser():
    p = argparse.ArgumentParser(
        description="%s %s 使用帮助" % (__desc__,__version__),
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=arg_epilog,
    )
    g = p.add_argument_group("身份设置 （随方式优先级排序）")
    for arg_key, arg in global_args.items():
        g.add_argument("--%s" % arg_key, **arg)
    # global args
    g = p.add_argument_group("上传设置")
    for arg_key, arg in local_args.items():
        g.add_argument("--%s" % arg_key, **arg)
    # local args (per source)
    g = p.add_argument_group(
        '解析可选参数 "opts" （格式 ： [参数1]=[值1];[参数2]=[值2] (query-string)）\n'+
        '视频源参数'
    )
    for provider_name, provider in provider_args.items():
        g.add_argument(
            "--%s" % provider_name,
            metavar="%s-URL" % provider_name.upper(),
            type=str,
            help="%s\n   参数:%s" % (provider.__desc__, provider.__cfg_help__),
        )
    return p


def prase_args(args: list):
    if len(args) < 2:
        parser = _create_argparser()
        parser.print_help()
        return
    args.pop(0)  # remove filename
    parser = _create_argparser()
    global_args_dict = AttribuitedDict()
    for k, v in parser.parse_args(args).__dict__.items():
        if k in global_args:
            global_args_dict[k] = v
            if not "--%s" % k in args:
                continue
        elif k in local_args and local_args[k]["default"] != v:
            # raise argparse.ArgumentError(None ,'"上传设置" (--%s) 仅应该出现于视频源后 (e.g. --youtube "..." --tags ..) ' % k)
            pass # TODO : Properly implement this check
    """pre-parse : fetch global args,then remove them"""
    local_args_group = []
    current_line = []
    current_provider = ""

    def add():
        args = parser.parse_args(current_line).__dict__
        args["resource"] = args[current_provider]
        local_args_group.append(
            (provider_args[current_provider], AttribuitedDict(args))
        )

    i = 0
    while i < len(args):
        if args[i][2:] in provider_args:
            # a new proivder. terminates till next provider
            current_provider = args[i][2:]
            current_line = ["--" + current_provider]
            for i in range(i + 1, len(args)):
                if args[i][2:] in provider_args:
                    break
                current_line.append(args[i])
            add()
            i -= 1
        i += 1
    return global_args_dict, local_args_group
