# -*- coding: utf-8 -*-
"""Youtube video provider - yt-dlp"""
from sqlite3 import Date
from yt_dlp.postprocessor.ffmpeg import FFmpegPostProcessor, FFmpegPostProcessorError
from yt_dlp.postprocessor.embedthumbnail import FFmpegThumbnailsConvertorPP
from yt_dlp.utils import (
    encodeArgument,
    encodeFilename,
    prepend_extension,
    shell_quote,
    DateRange,
    datetime_from_str,
)
from yt_dlp.version import __version__ as yt_dlp_version
from bilibili_toolman.providers import DownloadResult
import logging, yt_dlp, os, subprocess, sys

__desc__ = """Youtube / Twitch / etc 视频下载 (yt-dlp %s)""" % yt_dlp_version
__cfg_help__ = """yt-dlp 参数：
    format (str) - 同 yt-dlp -f
    quite (True,False) - 是否屏蔽 yt-dlp 日志 (默认 False)
特殊参数：
    playlistend - 对于播放列表、频道，下载到（时间顺序，新者在前）第 n 个视频为止
    playliststart - 对于播放列表、频道，从（时间顺序，新者在前）第 n 个视频开始下载

    daterange - 只下载在该参数指定时间窗口内的视频 (精确到毫秒)
        格式可以为 YYmmdd,也可以用相对时间. 如：
        
        e.g. daterange=now; (下载今天上传的视频)
        e.g. daterange=now-1day; (下载昨天到今天上传的视频)
        e.g. daterange=220430~220501 (下载 2022年4月30日~2022年5月1日 的视频)        
    
    hardcode - 烧入硬字幕选项
        e.g. 启用    ..;hardcode;...
        e.g. 换用字体 ..;hardcode=style:FontName=Segoe UI       
        e.g. NV硬解码   ..;hardcode=input:-hwaccel cuda/output:-c:v h264_nvenc -crf 17 -b:v 5M
        多个选项用 / 隔开   
e.g. --youtube "..." --opts "format=best&quiet=True&hardcode" --tags ...
    此外，针对视频对象，还提供其他变量:
        {id}
        {title}    
        {descrption}
        {upload_date}
        {uploader}
        {uploader_id}
        {uploader_url}
        {channel_id}
        {channel_url}
        {duration}
        {view_count}
        {avereage_rating}
        ...
    注：输入播放列表且多 P 时，稿件标题为播放列表标题，稿件描述仅为 `来自Youtube`

默认配置：不烧入字幕，下载最高质量音视频，下载字幕但不操作
"""
ydl = None
logger = logging.getLogger("yt-dlp")
yt_dlp.utils.std_headers[
    "User-Agent"
] = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
params = {
    "logger": logger,
    "outtmpl": "%(id)s.%(ext)s",
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "writethumbnail": True,
    "writesubtitles": True,
    "ignoreerrors":True
}  # default params,can be overridden


def __to_yyyy_mm_dd(date):
    return date[:4] + "/" + date[4:6] + "/" + date[6:]


def update_config(cfg):
    global ydl
    # preprocess some parameters
    if "daterange" in cfg:
        datestr = cfg["daterange"]
        daterange = DateRange()
        if "~" in datestr:
            dateStart, dateEnd = datestr.split("~")
            daterange.start = datetime_from_str(dateStart, precision="second").date()
            daterange.end = datetime_from_str(dateEnd, precision="second").date()
        else:
            daterange.start = datetime_from_str(datestr, precision="second").date()
        cfg["daterange"] = daterange
        logger.info("指定要下载的视频上传时间窗口: %s - %s" % (
            daterange.start.strftime("%Y/%m/%d %H:%M:%S"),
            daterange.end.strftime("%Y/%m/%d %H:%M:%S")
        ))

    if "playlistend" in cfg:
        cfg["playlistend"] = int(cfg["playlistend"])
    if "playlistbegin" in cfg:
        cfg["playlistbegin"] = int(cfg["playlistbegin"])

    hardcodeSettings = None
    if "hardcode" in cfg:  # private implementation of hardcoding subtitles
        hardcodeSettings = HardcodeSettings(from_cmd=cfg["hardcode"])
        del cfg["hardcode"]
    ydl = yt_dlp.YoutubeDL({**params, **cfg})
    ydl.add_post_processor(FFmpegThumbnailsConvertorPP(ydl, format="png"))
    if hardcodeSettings:
        ydl.add_post_processor(HardcodeSubProcesser(ydl, hardcodeSettings))


class HardcodeSettings:
    style = "FontName=Segoe UI,FontSize=24"
    """alternative font style for subs filter"""
    input = ""  # params for input file
    output = ""  # params for output file
    """other FFMPEG parameters"""

    def __init__(self, from_cmd):
        """Constructs settings via commandline"""
        for cmd in from_cmd.split("/"):
            if not cmd:
                break
            idx = cmd.index(":")
            key, value = cmd[:idx], cmd[idx + 1 :]
            setattr(self, key, value)


class HardcodeSubProcesser(FFmpegPostProcessor):
    def run_ffmpeg_multiple_files(self, input_paths, out_path, opts):
        """making ffmpeg output to stdout instead,and allowing input parameters"""
        self.check_version()

        oldest_mtime = min(
            os.stat(encodeFilename(path)).st_mtime for path in input_paths
        )

        opts += self._configuration_args()

        files_cmd = []
        for path in input_paths:
            files_cmd.extend(
                [
                    encodeArgument("-i"),
                    encodeFilename(self._ffmpeg_filename_argument(path), True),
                ]
            )
        cmd = [
            encodeFilename(self.executable, True),
            encodeArgument("-y"),
            encodeArgument("-hide_banner"),
        ] + self.settings.input.split()
        # avconv does not have repeat option
        if self.basename == "ffmpeg":
            cmd += [
                encodeArgument("-loglevel"),
                encodeArgument("warning"),
                encodeArgument("-stats"),
            ]
        cmd += (
            files_cmd
            + [encodeArgument(o) for o in opts]
            + [encodeFilename(self._ffmpeg_filename_argument(out_path), True)]
        )
        self._downloader.to_screen("[debug] ffmpeg command line: %s" % shell_quote(cmd))
        p = subprocess.Popen(
            cmd, stdout=sys.stdout, stderr=sys.stderr, stdin=subprocess.PIPE
        )
        p.communicate()
        if p.returncode != 0:
            raise FFmpegPostProcessorError("See stderr for more info")
        self.try_utime(out_path, oldest_mtime, oldest_mtime)

    def __init__(self, downloader, settings: HardcodeSettings):
        self.settings = settings
        super().__init__(downloader=downloader)

    def run(self, information):
        sub = information["requested_subtitles"]
        if sub:
            lang = list(sub.keys())[0]
            sub_filename = f"{information['display_id']}.{lang}.vtt"
            if os.path.isfile(sub_filename):
                self._downloader.to_screen("[ffmpeg] 烧入字幕: %s" % sub_filename)
                filename = information["filepath"]
                opts = [
                    "-vf",
                    f"subtitles={sub_filename}:force_style='{self.settings.style}'",
                    "-qscale",
                    "0",
                    "-c:a",
                    "copy",
                ] + self.settings.output.split()

                temp_filename = prepend_extension(filename, "temp")
                self.run_ffmpeg(filename, temp_filename, opts)

                os.remove(encodeFilename(filename))
                os.rename(encodeFilename(temp_filename), encodeFilename(filename))
        return [], information  # by default, keep file and do nothing


def download_video(res) -> DownloadResult:
    with DownloadResult() as results:
        def append_result(entry):
            if not entry: return
            with DownloadResult() as result:
                video_path = "%s.%s" % (entry["display_id"], entry["ext"])
                if not os.path.exists(video_path):
                    return
                result.extra = entry
                result.title = entry["title"]
                result.soruce = entry["webpage_url"]
                result.video_path = video_path
                """For both total results and local sub-results"""
                results.cover_path = result.cover_path = "%s.%s" % (
                    entry["display_id"],
                    "png",
                )
                if not os.path.isfile(results.cover_path):
                    logger.error("Thumbnail not found. Discarding info.")
                    results.cover_path = ""
                date = __to_yyyy_mm_dd(entry["upload_date"])
                result.description = f"""作者 : {entry['uploader']} [{date} 上传]

来源 : https://youtu.be/{entry['id']}

{entry['description']}"""
            results.results.append(result)

        info = ydl.extract_info(res, download=True)
        if not info:
            return results
        results.soruce = info["webpage_url"]
        results.title = info["title"]
        """Appending our results"""
        if "entries" in info:  # A playlist
            for entry in info["entries"]:
                append_result(entry)
            results.description = "转自Youtube"
        else:  # Singular videos
            append_result(info)        
        if len(results.results) > 1:
            results.description = '\n'.join(['P%d : %s' % result for result in enumerate(results.results)])
        else:
            results.description = results.results[0].description
        return results
