# -*- coding: utf-8 -*-

from platformcode import config, logger, platformtools
from core import httptools, scrapertools
from lib import balandroresolver

def get_video_url(page_url, url_referer=''):
    logger.info("url=" + page_url)

    video_urls = []

    page_url = page_url.replace('/uptobox/', '/uptobox.com/')

    vid = scrapertools.find_single_match(page_url, "(?:uptobox.com/|uptostream.com/)(?:iframe/|)([A-z0-9]+)")
    if not vid: return video_urls

    video_urls = balandroresolver.resolve_uptobox().getLink(vid, video_urls)
    # logger.info(video_urls)

    return video_urls

