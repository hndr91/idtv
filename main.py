# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
# Modified by : M.A. Hendrawan
# Modified on : 23.04.2017

# Disclaimer
# I do not own the stream urls or provide the stream urls. The stream urls belongs to the following below
# ---------------------------------- #
# 1. Global TV - metube.id
# 2. MNC TV - metube.id
# 3. RCTI - metube.id
# 4. TRANS 7 - vidio.com
# 5. TRANS TV - vidio.com
# 6. INDOSIAR - vidio.com
# 7. SCTV - vidio.com
# 8. ANTV - vidio.com
# 9. TVONE - vidio.com
# 10. METROTV - metrotvnews.com
# 11. KOMPAS TV - vidio.com
# 12. RTV - vidio.com
# --------------------------------- #

# Fanart "Texture 42" by xnienke http://xnienke.deviantart.com/art/Texture-42-286924446

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

VIDEOS = {'LIVE': [{'name': 'Global TV',
                    'thumb': 'http://www.globaltv.co.id/images/logobaru.png',
                    'video': 'http://cdn.live.metube.id/globaltv.m3u8',
                    'genre': 'TV'},
                   {'name': 'MNC TV',
                    'thumb': 'http://webcms.mncgroup.com/timthumb.php?zc=3&w=180&h=33&src=/app/webroot/files/mnctv/logo.png',
                    'video': 'http://cdn.live.metube.id/mnctv.m3u8',
                    'genre': 'TV'},
                   {'name': 'RCTI',
                    'thumb': 'http://www.rcti.tv/assets/images/RCTI-logo.png',
                    'video': 'http://cdn.live.metube.id/rcti.m3u8',
                    'genre': 'TV'},
                   {'name': 'TRANS 7',
                    'thumb': 'http://career.trans7.co.id/images/trans7.png',
                    'video': 'https://livestream-hybrid.akamaized.net/live/smil:trans7.smil/playlist.m3u8',
                    'genre': 'TV'},
                   {'name': 'TRANS TV',
                    'thumb': 'http://www.transtv.co.id/template/front/source/images/bg/logo.png',
                    'video': 'https://livestream-hybrid.akamaized.net/live/smil:transtv.smil/playlist.m3u8',
                    'genre': 'TV'},
                   {'name': 'INDOSIAR',
                    'thumb': 'http://www.indosiar.com/assets/img/logo-indosiar.png',
                    'video': 'https://livestream-hybrid.akamaized.net/live/smil:indosiar.smil/playlist.m3u8',
                    'genre': 'TV'},
                   {'name': 'SCTV',
                    'thumb': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/SCTV_Logo.svg/2000px-SCTV_Logo.svg.png',
                    'video': 'https://livestream-hybrid.akamaized.net/live/smil:sctv.smil/playlist.m3u8',
                    'genre': 'TV'},
                   {'name': 'ANTV',
                    'thumb': 'http://www.an.tv/assets/uploads/2017/02/Logo-Antv-Viva.png',
                    'video': 'https://livestream-hybrid.akamaized.net/live/smil:antv.smil/playlist.m3u8',
                    'genre': 'TV'},
                   {'name': 'TVONE',
                    'thumb': 'http://vignette3.wikia.nocookie.net/globaltvindonesia/images/5/50/LOGO-tvOne-New-2012.jpg',
                    'video': 'https://livestream-hybrid.akamaized.net/live/smil:tvone.smil/playlist.m3u8',
                    'genre': 'TV'},
                   {'name': 'METRO TV',
                    'thumb': 'http://vignette2.wikia.nocookie.net/logopedia/images/b/bb/New_MetroTV_Logo_2010.png',
                    'video': 'http://edge.metrotvnews.com:1935/live-edge/smil:metro.smil/playlist.m3u8',
                    'genre': 'TV'},
                   {'name': 'KOMPAS TV',
                    'thumb': 'http://www.kompas.tv/assets/assets/logo.png',
                    'video': 'https://livestream-hybrid.akamaized.net/live/smil:kompastv.smil/playlist.m3u8',
                    'genre': 'TV'},
                   {'name': 'RTV',
                    'thumb': 'http://1.bp.blogspot.com/-utv-FB1mrlM/U4k4U2JN9HI/AAAAAAAARqU/EKp90xumCvg/s1600/LOGO+RAJAWALI+TV.png',
                    'video': 'https://livestream-hybrid.akamaized.net/live/smil:rtv.smil/playlist.m3u8',
                    'genre': 'TV'}
                  ]}

#http://www.dailymotion.com/cdn/live/video/x41047b.m3u8?auth=1493107731-2688-uslpojk6-e4ad0b3485cffcf8351e695a2f2e2840

def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: list
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': category, 'genre': category})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/vids/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
