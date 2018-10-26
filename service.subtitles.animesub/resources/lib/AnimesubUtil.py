import os
import re
from StringIO import StringIO
from zipfile import ZipFile
from difflib import SequenceMatcher


class AnimesubUtil:
    def __init__(self, file_name):
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
        match = re.search("([\se_\[]|ep)(?P<episode>\d{2,3})([\s._v\]]|$)", episode, re.IGNORECASE)
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

    def prepare_zip(self, content):
        result = None
        with ZipFile(content, 'r') as myzip:
            if len(myzip.filelist) > 1:
                best_match = self.get_best_match(myzip.filelist)
                result = self.get_new_zip(myzip, best_match)
            elif self.is_one_file_in_directory(myzip.filelist):
                result = self.get_new_zip(myzip, myzip.filelist[0])

        if result:
            if isinstance(content, basestring):
                with open(content, "wb") as myfile:
                    myfile.write(result.getvalue())
        else:
            result = content

        return result

    def get_best_match(self, file_list):
        candidate = None
        candidate_score = -1
        episode = self.episode()
        file_name = self.__file.lower()
        for x in file_list:
            if not x.filename.endswith('/'):
                current_filename = os.path.basename(x.filename)
                current_episode = AnimesubUtil(current_filename).episode()
                current_score = SequenceMatcher(None, file_name, current_filename.lower()).ratio()
                if episode == current_episode:
                    current_score += 1
                if current_score > candidate_score:
                    candidate_score = current_score
                    candidate = x
        return candidate

    @staticmethod
    def get_new_zip(zip_file, zip_info):
        content = StringIO()
        with ZipFile(content, 'w') as myzip:
            base_name = os.path.basename(zip_info.filename)
            file_bytes = zip_file.read(zip_info.filename)
            myzip.writestr(base_name, file_bytes)
        return content

    @staticmethod
    def is_one_file_in_directory(file_list):
        return len(file_list) == 1 and file_list[0].filename != os.path.basename(file_list[0].filename)

    @staticmethod
    def trim(value):
        value = re.sub("-|\.+|\_", " ", value, flags=re.IGNORECASE)
        value = re.sub(" +", " ", value, flags=re.IGNORECASE)
        return value.strip()
