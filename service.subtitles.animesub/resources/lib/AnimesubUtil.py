import os
import re


class AnimesubUtil:
    def __init__(self, file_name):
        self.__file = file_name.lower()

    def searchable(self):
        title_episode = self.title()
        if not title_episode:
            return self.__file

        episode = self.episode()
        if episode:
            title_episode = title_episode + ' ep' + episode
        return title_episode

    def episode(self):
        episode = re.sub("\d{2}.\d{2,}", "", self.__file)
        match = re.search("[\se_\[](?P<episode>\d{2,3})[\s._v\]]", episode)
        if not match:
            return False
        return match.group('episode')

    def title(self):
        title = os.path.splitext(self.__file)[0]
        title = re.sub("\[.*?\]|\(.*?\)|season|s\d{1,2}", "", title)
        match = re.findall("[\s.a-z_]*", title)

        if isinstance(match, list) and len(match) > 0:
            title = match[0]
            if len(self.trim(title)) <= 3:
                for x in range(1, len(match)):
                    if len(self.trim(match[x])) > 1:
                        title = title + ' ' + match[x]
                        break

        return self.trim(title)

    @staticmethod
    def trim(value):
        value = re.sub("-|\.+|\_", " ", value)
        value = re.sub(" +", " ", value)
        return value.strip()
