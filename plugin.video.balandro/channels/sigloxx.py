﻿# -*- coding: utf-8 -*-

from platformcode import logger, platformtools
from core.item import Item
from core import httptools, scrapertools, servertools, tmdb


host = 'https://2000peliculassigloxx.com/'

perpage = 25


def mainlist(item):
    return mainlist_pelis(item)

def mainlist_pelis(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone ( title = 'Sagas', action = 'sagas', url = host + 'sagas/', search_type = 'movie' ))

    itemlist.append(item.clone ( title = 'Por año', action = 'anios', search_type = 'movie' ))

    itemlist.append(item.clone ( title = 'Por actor', action = 'listas', url = host + 'actores/' ))
    itemlist.append(item.clone ( title = 'Por actriz', action = 'listas', url = host + 'actrices/' ))
    itemlist.append(item.clone ( title = 'Por dirección, guionistas, productores', action = 'listas', url = host + 'directores/' ))
    itemlist.append(item.clone ( title = 'Por compositores, escritores, novelistas', action = 'listas', url = host + 'otras-biografias/' ))

    # ~ itemlist.append(item.clone ( title = 'Buscar película ...', action = 'search', search_type = 'movie' ))

    return itemlist


def sagas(item):
    logger.info()
    itemlist = []

    data = httptools.downloadpage(item.url).data

    bloque = scrapertools.find_single_match(data, '>Sagas</h2>(.*?)</main>')

    matches = scrapertools.find_multiple_matches(bloque, '.*?<a href="(.*?)".*?title="(.*?)"')

    for url, title in matches:
        if not title: continue

        itemlist.append(item.clone( action = 'list_films', title = title, url = url ))

    return itemlist


def anios(item):
    logger.info()
    itemlist = []

    url = host
    data = httptools.downloadpage(url).data

    bloque = scrapertools.find_single_match(data, '>Décadas<(.*?)>Biografías<')

    matches = scrapertools.find_multiple_matches(bloque, '<li id=".*?<a href="([^"]+)">(.*?)</a>')

    for url, title in matches:
        if not url or not title: continue

        if not '/anos-' in url: continue

        itemlist.append(item.clone( action = 'list_films', title = title, url = url ))

    return itemlist


def listas(item):
    logger.info()
    itemlist = []

    data = httptools.downloadpage(item.url).data

    if '/otras-biografias' in item.url:
        matches = scrapertools.find_multiple_matches(data, '<li><a href="([^"]+)".*?rel="noopener noreferrer">(.*?)</a>')

        for url, title in matches:
            if not url or not title: continue

            itemlist.append(item.clone( action= 'list_films', title = title, url = url ))
    else:
       matches = scrapertools.find_multiple_matches(data, '<figure.*?<a href="([^"]+)".*?src="([^"]+)".*?alt="(.*?)".*?</figure>')

       for url, thumb, title in matches:
           if not url or not title: continue

           itemlist.append(item.clone( action = 'list_films', title = title, url = url, thumbnail = thumb ))

    return sorted(itemlist, key = lambda it: it.title)


def list_films(item):
    logger.info()
    itemlist = []

    if not item.page: item.page = 0

    data = httptools.downloadpage(item.url).data

    bloque = scrapertools.find_single_match(data, '<nav id="site-navigation"(.*?)<nav')

    matches = scrapertools.find_multiple_matches(bloque, 'data-src="(.*?)".*?alt="(.*?)".*?<a href="(.*?)"')

    num_matches = len(matches)
    desde = item.page * perpage
    hasta = desde + perpage

    for thumb, title, url in matches[desde:hasta]:
        if not url or not title: continue

        if title == '2000PeliculasSigloXX': continue

        name = title.strip()

        try:
            year = title.split('(')[1]
            year = year.split(',')[0]

            if year:
                title = title.replace(year + ', ', '')

                name = title
                name = name.split('(')[0]
                name = name.strip()
        except:
            year = ''

        if not year: year = '-'

        itemlist.append(item.clone( action = 'findvideos', title = title, url = url, thumbnail = thumb,
                                    contentType = 'movie', contentTitle = name, infoLabels = {'year': year} ))

    tmdb.set_infoLabels(itemlist)

    if num_matches > hasta:
        next_page = item.page + 1
        itemlist.append(item.clone( title='>> Página siguiente', page = next_page, action = 'list_films', text_color='coral' ))

    return itemlist


def findvideos(item):
    logger.info()
    itemlist = []

    data = httptools.downloadpage(item.url).data

    url = scrapertools.find_single_match(data, '<source src="(.*?)"')
    if not url:
       url = scrapertools.find_single_match(data, '<source type="video/mp4".*?src="(.*?)"')

    url = url.replace('https://www.adf.ly/6680622/banner/', '').replace('&amp;', '&')

    if url.startswith('https://ipfs.infura.io/'):
        headers = {'referer': host}
        url = httptools.downloadpage(url, headers = headers, only_headers = True, follow_redirects = False).headers.get('location')
        if url:
            itemlist.append(Item( channel = item.channel, action = 'play', server = 'directo', language = 'Esp', url = url ))
            return itemlist

    if url:
           servidor = servertools.get_server_from_url(url)
           servidor = servertools.corregir_servidor(servidor)

           if servidor and servidor != 'directo':
               url = servertools.normalize_url(servidor, url)

               itemlist.append(Item( channel = item.channel, action = 'play', server = servidor, language = 'Esp', url = url ))

    return itemlist


def list_search(item):
    logger.info()
    itemlist = []

    data = httptools.downloadpage(item.url).data

    matches = scrapertools.find_multiple_matches(data, '<article id="post-(.*?)</article>')

    for article in matches:
        url = scrapertools.find_single_match(article, ' href="([^"]+)"')
        title = scrapertools.find_single_match(article, 'rel="bookmark">(.*?)</a>')

        if not url or not title: continue

        itemlist.append(item.clone( action = 'findvideos', url = url, title = title,
                                    contentType = 'movie', contentTitle = title, infoLabels = {'year': '-'} ))

    return itemlist


def search(item, texto):
    logger.info()
    try:
        item.url = host + '?s=' + texto.replace(" ", "+")
        return list_search(item)
    except:
        import sys
        for line in sys.exc_info():
            logger.error("%s" % line)
        return []
