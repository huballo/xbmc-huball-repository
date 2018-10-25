import os
import re


class AnimesubUtil:
    def __init__(self, file_name):
        if not isinstance(file_name, str):
            raise TypeError(file_name, "Must be str")
        self.__file = file_name

    def searchable(self):
        title_episode = self.title()
        if not title_episode:
            return self.__file

        episode = self.episode()
        if episode:
            title_episode = title_episode + ' ep' + episode
        return title_episode

    def episode(self):
        episode = re.sub("[\s._-]\d{2}.\d{2,}", "", self.__file, flags=re.IGNORECASE)
        match = re.search("[\se_\[](?P<episode>\d{2,3})[\s._v\]]", episode, re.IGNORECASE)
        if not match:
            return None
        return match.group('episode')

    def title(self):
        title = os.path.splitext(self.__file)[0]
        title = re.sub("\[.*?\]|\(.*?\)|season|s\d{1,2}e\d{1,2}.*|s\d{1,2}|[^\x00-\x7F]+", "", title, flags=re.IGNORECASE)
        match = re.findall("[a-zA-Z][a-zA-Z.-]*[_\sa-zA-Z]*[a-zA-Z]", title, re.IGNORECASE)

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
        value = re.sub("-|\.+|\_", " ", value, flags=re.IGNORECASE)
        value = re.sub(" +", " ", value, flags=re.IGNORECASE)
        return value.strip()
