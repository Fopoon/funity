# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from unittest import TestCase

from funity import UnityProject


class UnityProjectTestCase(TestCase):

    def test_find_assets(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        csharp_assets = project.find_assets(file_extensions=['.cs'],
                                            skip_folders=UnityProject.SPECIAL_DIRS)

        self.assertTrue(csharp_assets)

        self.assertCountEqual(csharp_assets, [
            'Assets/Scripts/MyClass.cs',
            'Assets/Scripts/MyMonoBehaviour.cs',
        ])

    def test_get_build_scenes(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        scenes = project.get_build_scenes()

        self.assertTrue(scenes)

    def test_get_editor_version(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        editor_version = project.get_editor_version()

        self.assertEqual(editor_version, '2019.2.6f1')

    def test_get_project_bundle_version(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        bundle_version = project.get_project_bundle_version()

        self.assertEqual(bundle_version, 0.1)

    def test_get_project_company_name(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        self.assertEqual(project.get_project_company_name(), 'fopoon')

    def test_get_project_layers(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        layers = project.get_project_layers()

        self.assertCountEqual(layers, [
            'Default',
            'TransparentFX',
            'Ignore Raycast',
            'Water',
            'UI',
            'layer_8'
        ])

        layers = project.get_project_layers(include_none=True)

        self.assertCountEqual(layers, [
            'Default',
            'TransparentFX',
            'Ignore Raycast',
            None,
            'Water',
            'UI',
            None,
            None,
            'layer_8',
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
        ])

    def test_get_project_product_name(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        self.assertEqual(project.get_project_product_name(), 'funity')

    def test_get_project_sorting_layers(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        sorting_layers = project.get_project_sorting_layers()

        self.assertCountEqual(sorting_layers, [
            'Default',
            'sorting_layer_1'
        ])

    def test_get_project_tags(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        tags = project.get_project_tags()

        self.assertCountEqual(tags, [
            'tag_0'
        ])
