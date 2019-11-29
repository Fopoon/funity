# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from unittest import TestCase

from funity import UnityProject


class UnityProjectTestCase(TestCase):

    def test_get_build_scenes(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        scenes = project.get_build_scenes()

        self.assertTrue(scenes)

    def test_get_project_company_name(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        self.assertEqual(project.get_project_company_name(), 'fopoon')

    def test_get_project_product_name(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        self.assertEqual(project.get_project_product_name(), 'funity')
