# -*- coding: utf-8 -*-

from unittest import TestCase
from zipfile import ZipFile
from StringIO import StringIO
from AnimesubUtil import AnimesubUtil


class TestAnimesubUtil(TestCase):
    def assertEpisode(self, expected, actual):
        self.assertEqual(expected, AnimesubUtil(actual).episode())

    def assertTitle(self, expected, actual):
        self.assertEqual(expected, AnimesubUtil(actual).searchable())

    def test_episode_empty_string(self):
        self.assertEpisode(None, "")

    def test_episode_none(self):
        with self.assertRaises(Exception):
            self.assertEpisode(None, None)

    def test_episode(self):
        self.assertEpisode("01", "[Lorem] Ipsum Dolor Sit - 01 (1080p x265 10bit).mkv")

    def test_episode_unicode(self):
        self.assertEpisode('01', u'[Lorem] Ipsum Dolor Sit - 01 (1080p x265 10bit).mkv')

    def test_episode_in_brackets(self):
        self.assertEpisode("01", "[Lorem] Ipsum Dolor Sit - [01] (1080p x265 10bit).mkv")

    def test_episode_in_brackets(self):
        self.assertEpisode("01", "[Lorem] Ipsum Dolor Sit - [01v2] (1080p x265 10bit).mkv")

    def test_episode_with_dot_in_brackets(self):
        self.assertEpisode("01", "[Lorem] Ipsum Dolor Sit - [01.5] (1080p x265 10bit).mkv")

    def test_episode_with_dot_and_version_in_brackets(self):
        self.assertEpisode("01", "[Lorem] Ipsum Dolor Sit - [01.5v2] (1080p x265 10bit).mkv")

    def test_episode_fps(self):
        self.assertEpisode(None, "[Lorem] Ipsum Dolor Sit (1080p x265 23.976fps 10bit).mkv")

    def test_episode_ep(self):
        self.assertEpisode("01", "Ipsum Dolor Sit ep01")

    def test_searchable_string(self):
        self.assertTitle("", "")

    def test_searchable_none(self):
        with self.assertRaises(Exception):
            self.assertTitle(None, None)

    def test_searchable_brackets(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "[Lorem] Ipsum Dolor Sit - 01 (1080p x265 10bit).mkv")

    def test_searchable_brackets_s1(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "[Lorem] Ipsum Dolor Sit S1 - 01 (1080p x265 10bit).mkv")

    def test_searchable_brackets_season1(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "[Lorem] Ipsum Dolor Sit Season 1 - 01 (1080p x265 10bit).mkv")

    def test_searchable_brackets_half_episode(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "[Lorem] Ipsum Dolor Sit - 01.5 (1080p x265 10bit).mkv")

    def test_searchable_brackets_episode_name(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "[Lorem] Ipsum Dolor Sit - Amet - 01 (1080p x265 10bit).mkv")

    def test_searchable_brackets_title_with_dash(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "[Lorem] Ipsum-Dolor Sit - 01 (1080p x265 10bit).mkv")

    def test_searchable_brackets_no_episode(self):
        self.assertTitle("Ipsum Dolor Sit", "[Lorem] Ipsum Dolor Sit 2018 (1080p x265 10bit).mkv")

    def test_searchable_brackets_and_underline_separator(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "[Lorem]_Ipsum_Dolor_Sit_-_01_(1080p-x265_10bit).mkv")

    def test_searchable_brackets_and_underline_separator_episode_titles(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "[Lorem]_Ipsum_Dolor_Sit_-_Session_01_-_Amet_[720p].mkv")

    def test_searchable_brackets_title_starts_with_3_or_lower_chars(self):
        self.assertTitle("Sed Ipsum Dolor Sit ep01", "[Lorem] Sed - Ipsum Dolor Sit - 01 (1080p x265 10bit).mkv")

    def test_searchable_brackets_with_utf8_chars(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "[Lorem] Ipsum Dolor √Sit - 01 (1080p x265 10bit).mkv")

    def test_searchable_underline_s01e01(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "Ipsum_Dolor_Sit_S01E01_720p_BrRip_Lorem.mkv")

    def test_searchable_starts_with_title(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "Ipsum Dolor Sit - 01 [720p].mkv")

    def test_searchable_starts_with_title_ends_with_episode(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "Ipsum Dolor Sit - 01.mkv")

    def test_searchable_dots_episode_title(self):
        self.assertTitle("Ipsum Dolor Sit ep01", "Ipsum.Dolor.Sit.S01E01.Amet.1080p.x265.Lorem.mkv")

    def assertPrepareZip(self, search_name, check_name, zip_content):
        prepared_content = AnimesubUtil(search_name).prepare_zip(zip_content)
        with ZipFile(prepared_content, 'r') as prepared_zip:
            self.assertEquals(1, len(prepared_zip.filelist))
            self.assertEquals(check_name, prepared_zip.filelist[0].filename)

    def test_prepare_zip_one_episode(self):
        zip_content = StringIO()
        with ZipFile(zip_content, 'w') as myzip:
            myzip.writestr('[Lorem] Ipsum Dolor Sit - 01 (1080p x265 10bit).mkv', '')

        search = check = '[Lorem] Ipsum Dolor Sit - 01 (1080p x265 10bit).mkv'
        self.assertPrepareZip(search, check, zip_content)

    def test_prepare_zip_one_episode_in_directory(self):
        zip_content = StringIO()
        with ZipFile(zip_content, 'w') as myzip:
            myzip.writestr('Ipsum Dolor\\[Lorem] Ipsum Dolor Sit - 01 (1080p x265 10bit).mkv', '')

        search = check = '[Lorem] Ipsum Dolor Sit - 01 (1080p x265 10bit).mkv'
        self.assertPrepareZip(search, check, zip_content)

    def test_prepare_zip_three_episodes(self):
        zip_content = StringIO()
        with ZipFile(zip_content, 'w') as myzip:
            myzip.writestr('[Lorem] Ipsum Dolor Sit - 01 (1080p x265 10bit).mkv', '')
            myzip.writestr('[Lorem] Ipsum Dolor Sit - 02 (1080p x265 10bit).mkv', '')
            myzip.writestr('[Lorem] Ipsum Dolor Sit - 03 (1080p x265 10bit).mkv', '')

        search = check = '[Lorem] Ipsum Dolor Sit - 02 (1080p x265 10bit).mkv'
        self.assertPrepareZip(search, check, zip_content)

    def test_prepare_zip_three_episodes_in_directory(self):
        zip_content = StringIO()
        with ZipFile(zip_content, 'w') as myzip:
            myzip.writestr('Ipsum Dolor\\[Lorem] Ipsum Dolor Sit - 01 (1080p x265 10bit).mkv', '')
            myzip.writestr('Ipsum Dolor\\[Lorem] Ipsum Dolor Sit - 02 (1080p x265 10bit).mkv', '')
            myzip.writestr('Ipsum Dolor\\[Lorem] Ipsum Dolor Sit - 03 (1080p x265 10bit).mkv', '')

        search = check = '[Lorem] Ipsum Dolor Sit - 02 (1080p x265 10bit).mkv'
        self.assertPrepareZip(search, check, zip_content)

    def test_prepare_zip_three_episodes_in_directory_episode_match(self):
        zip_content = StringIO()
        with ZipFile(zip_content, 'w') as myzip:
            myzip.writestr('Ipsum Dolor\\[Consectetur] Ipsum Dolor Sit - 01 [720p x265 10bit].mkv', '')
            myzip.writestr('Ipsum Dolor\\[Consectetur] Ipsum Dolor Sit - 02 [720p x265 10bit].mkv', '')
            myzip.writestr('Ipsum Dolor\\[Consectetur] Ipsum Dolor Sit - 03 [720p x265 10bit].mkv', '')

        search = '[Lorem] Ipsum Dolor Sit - 02 (1080p x265 10bit).mkv'
        check = '[Consectetur] Ipsum Dolor Sit - 02 [720p x265 10bit].mkv'
        self.assertPrepareZip(search, check, zip_content)

    def assertSortBySimilarity(self, search):
        results = [{'title': 'Ipsum ep01'}, {'title': 'Ipsum Dolor ep01'}, {'title': 'Ipsum Dolor Sit ep01'}]
        AnimesubUtil.sort_by_similarity(search, 'title', results)
        first_item = results[0]
        self.assertEqual(search, first_item['title'])

    def test_sort_by_similarity_1(self):
        self.assertSortBySimilarity('Ipsum ep01')

    def test_sort_by_similarity_2(self):
        self.assertSortBySimilarity('Ipsum Dolor ep01')

    def test_sort_by_similarity_2(self):
        self.assertSortBySimilarity('Ipsum Dolor Sit ep01')
