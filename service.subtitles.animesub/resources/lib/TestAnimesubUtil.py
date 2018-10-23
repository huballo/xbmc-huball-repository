# -*- coding: utf-8 -*-

from unittest import TestCase
from AnimesubUtil import AnimesubUtil


class TestAnimesubUtil(TestCase):
    def assertTitle(self, expected, actual):
        self.assertEqual(expected, AnimesubUtil(actual).searchable())

    def test_horriblesubs_shingeki_no_kyojin(self):
        self.assertTitle("shingeki no kyojin ep40", "[HorribleSubs] Shingeki no Kyojin S3 - 40 [1080p].mkv")

    def test_horriblesubs_tensei_shitara_slime_datta_ken(self):
        self.assertTitle("tensei shitara slime datta ken ep01", "[HorribleSubs] Tensei Shitara Slime Datta Ken - 01 [1080p].mkv")

    def test_horriblesubs_goblin_slayer(self):
        self.assertTitle("goblin slayer ep01", "[HorribleSubs] Goblin Slayer - 01 [1080p].mkv")

    def test_horriblesubs_darling_in_the_franxx(self):
        self.assertTitle("darling in the franxx ep01", "[HorribleSubs] Darling in the FranXX - 01 [1080p].mkv")

    def test_horriblesubs_tokyo_ghoul_re(self):
        self.assertTitle("tokyo ghoul re ep01", "[HorribleSubs] Tokyo Ghoul re - 01 [1080p].mkv")

    def test_horriblesubs_sword_art_online(self):
        self.assertTitle("sword art online ep01", "[HorribleSubs] Sword Art Online - 01 [1080p].mkv")

    def test_horriblesubs_sword_art_online_ii(self):
        self.assertTitle("sword art online ii ep01", "[HorribleSubs] Sword Art Online II - 01 [1080p].mkv")

    def test_horriblesubs_sword_art_online_ii_half_episode(self):
        self.assertTitle("sword art online ii ep14", "[HorribleSubs] Sword Art Online II - 14.5 [1080p].mkv")

    def test_horriblesubs_sword_art_online_alicization(self):
        self.assertTitle("sword art online ep01", "[HorribleSubs] Sword Art Online - Alicization - 01 [1080p].mkv")

    def test_horriblesubs_one_punch_man(self):
        self.assertTitle("one punch man ep01", "[HorribleSubs] One-Punch Man - 01 [1080p].mkv")

    def test_oyhs_raws_tensei_shitara_slime_datta_ken(self):
        self.assertTitle("tensei shitara slime datta ken ep01", "[Ohys-Raws] Tensei Shitara Slime Datta Ken - 01 (BS11 1280x720 x264 AAC).mp4")

    def test_oyhs_raws_golbin_slayer(self):
        self.assertTitle("goblin slayer ep01", "[Ohys-Raws] Goblin Slayer - 01 (AT-X 1280x720 x264 AAC).mp4")

    def test_zero_raws_fate_zero(self):
        self.assertTitle("fate zero ep01", "[Zero-Raws] Fate Zero - 01 (BD 1920x1080 x264 FLAC).mkv")

    def test_commie_banana_fish(self):
        self.assertTitle("banana fish ep14", "[Commie] Banana Fish - 14 [F2EB6BF6].mkv")

    def test_utw_fate_apocrypha(self):
        self.assertTitle("fate apocrypha ep01", "[UTW]_Fate_Apocrypha_-_01_[h264-720p][1D074A57].mkv")

    def test_fff_shingeki_no_kyojin(self):
        self.assertTitle("shingeki no kyojin ep01", "[FFF] Shingeki no Kyojin - 01 [BD][1080p-FLAC][7655512C].mkv")

    def test_dok_clannad_after_story(self):
        self.assertTitle("clannad after story ep01", "[Doki] Clannad After Story - 01 (1920x1080 Hi10P BD FLAC) [1AA8D908].mkv")

    def test_coalgirls_no_game_no_life(self):
        self.assertTitle("no game no life ep01", "[Coalgirls]_No_Game_No_Life_01_(1920x1080_Blu-Ray_FLAC)_[5673F6E8].mkv")

    def test_lns_code_geass_akito_the_exiled(self):
        self.assertTitle("code geass ep01", "[LNS] Code Geass - Akito the Exiled - 01 [BD 720p] [34FE67E7].mkv")

    def test_weiss_made_in_abyss(self):
        self.assertTitle("made in abyss ep01", "[WEISS] Made in Abyss 01.mkv")

    def test_reactor_great_teacher_onizuka(self):
        self.assertTitle("gto great teacher onizuka ep01", "[Reaktor] GTO - Great Teacher Onizuka - E01 [576p][x265][10-bit].mkv")

    def test_beatrice_raws_shingeki_no_kyojin(self):
        self.assertTitle("shingeki no kyojin ep01", "[Beatrice-Raws] Shingeki no Kyojin Season 2 - 01 [BDRip 1920x1080 x264 FLAC].mkv")

    def test_noobsubs_tokyo_ghoul(self):
        self.assertTitle("tokyo ghoul ep04", "[NoobSubs] Tokyo Ghoul 04 (1080p Blu-ray Dual Audio 8bit AAC)[564EAF1D].mkv")

    def test_noobsubs_tokyo_ghoul_a(self):
        self.assertTitle("tokyo ghoul ep01", "[NoobSubs] Tokyo Ghoul √A 01 (1080p Blu-ray Dual Audio 8bit AAC)[FA0B064F].mkv")

    def test_cbm_cowboy_bebop(self):
        self.assertTitle("cowboy bebop ep01", "[CBM]_Cowboy_Bebop_-_Session_01_-_Asteroid_Blues_[720p]_[ACFADD3A].mkv")

    def test_hysub_saenai_heroine_no_sodatekata(self):
        self.assertTitle("saenai heroine no sodatekata ep10", "[HYSUB]Saenai Heroine no Sodatekata ♭[10][GB_MP4][1280X720].mp4")

    def test_succ_kimi_no_na_wa(self):
        self.assertTitle("kimi no na wa", "Kimi.no.Na.wa.2016.1080p.Remux.AVC.FLAC.5.1-SUCC.mkv")

    def test_35mm_koe_no_katachi(self):
        self.assertTitle("koe no katachi", "[35mm] Koe no Katachi - A Silent Voice [1080p] [B9471AD7].mkv")

    def test_mabors_vcb_studio_shigatsu_wa_kimi_no_uso(self):
        self.assertTitle("shigatsu wa kimi no uso ep04", "[Mabors&VCB-Studio] Shigatsu wa Kimi no Uso [04][Hi10p_1080p][x264_2flac].mkv")

    def test_mabors_vcb_studio_shigatsu_wa_kimi_no_uso_v2(self):
        self.assertTitle("shigatsu wa kimi no uso ep09", "[Mabors&VCB-Studio] Shigatsu wa Kimi no Uso [09v2][Hi10p_1080p][x264_2flac].mkv")

    def test_pophd_evangelion_111(self):
        self.assertTitle("evangelion", "Evangelion 1.11 You Are (Not) Alone (2007) MULTi [1080p] BluRay x264-PopHD.mkv")

    def test_fch1993_clannad_movie(self):
        self.assertTitle("clannad", "CLANNAD [DVD 720x480 23.976fps AVC-yuv420p10 FLAC] - fch1993.mkv")
