# -*- coding: utf-8 -*-

from unittest import TestCase
from AnimesubUtil import AnimesubUtil


class TestAnimesubUtil(TestCase):
    def assertEpisode(self, expected, actual):
        self.assertEqual(expected, AnimesubUtil(actual).episode())

    def assertTitle(self, expected, actual):
        self.assertEqual(expected, AnimesubUtil(actual).searchable())

    def test_episode_empty_string(self):
        self.assertEpisode(None, "")

    def test_episode_none(self):
        with self.assertRaises(TypeError):
            self.assertEpisode(None, None)

    def test_episode(self):
        self.assertEpisode("01", "[Lorem] Ipsum Dolor Sit - 01 (1080p x265 10bit).mkv")

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

    def test_searchable_string(self):
        self.assertTitle("", "")

    def test_searchable_none(self):
        with self.assertRaises(TypeError):
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
