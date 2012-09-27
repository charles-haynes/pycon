import re
import mutagen.easyid3
import os

__author__ = 'chaynes'

class CanonicalName(object):
    def __init__(self, name):
        self.id3 = mutagen.easyid3.EasyID3(name)

    @property
    def name(self):
        fields = {'album': self.id3['album'],
                  'artist': self.id3['artist'],
                  'title': self.id3['title'],
                  'ext': '.mp3'}

        grandparent_dir_format = "{artist!s}"
        dir_format = "{album!s}"
        file_format = "{title!s}{ext!s}"

        if 'compilation' in self.id3 and self.id3['compilation']:
            grandparent_dir_format = "Various Artists"
            file_format = "{artist!s} - " + file_format
        try:
            fields['track'] = int(re.match('\d+', str(self.id3['tracknumber'])).group())
            file_format = "{track:02d} - " + file_format
        except (KeyError, AttributeError):
            pass

        return os.path.join(
            grandparent_dir_format, dir_format, file_format).format(**fields)
