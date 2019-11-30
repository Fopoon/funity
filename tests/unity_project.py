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

    def test_get_project_input_axes(self):

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        axes = project.get_project_input_axes()

        self.assertCountEqual(axes, [
            {'serializedVersion': 3, 'm_Name': 'Horizontal', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': 'left', 'positiveButton': 'right', 'altNegativeButton': 'a', 'altPositiveButton': 'd', 'gravity': 3, 'dead': 0.001, 'sensitivity': 3, 'snap': 1, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Vertical', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': 'down', 'positiveButton': 'up', 'altNegativeButton': 's', 'altPositiveButton': 'w', 'gravity': 3, 'dead': 0.001, 'sensitivity': 3, 'snap': 1, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Fire1', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': 'left ctrl', 'altNegativeButton': None, 'altPositiveButton': 'mouse 0', 'gravity': 1000, 'dead': 0.001, 'sensitivity': 1000, 'snap': 0, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Fire2', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': 'left alt', 'altNegativeButton': None, 'altPositiveButton': 'mouse 1', 'gravity': 1000, 'dead': 0.001, 'sensitivity': 1000, 'snap': 0, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Fire3', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': 'left shift', 'altNegativeButton': None, 'altPositiveButton': 'mouse 2', 'gravity': 1000, 'dead': 0.001, 'sensitivity': 1000, 'snap': 0, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Jump', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': 'space', 'altNegativeButton': None, 'altPositiveButton': None, 'gravity': 1000, 'dead': 0.001, 'sensitivity': 1000, 'snap': 0, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Mouse X', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': None, 'altNegativeButton': None, 'altPositiveButton': None, 'gravity': 0, 'dead': 0, 'sensitivity': 0.1, 'snap': 0, 'invert': 0, 'type': 1, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Mouse Y', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': None, 'altNegativeButton': None, 'altPositiveButton': None, 'gravity': 0, 'dead': 0, 'sensitivity': 0.1, 'snap': 0, 'invert': 0, 'type': 1, 'axis': 1, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Mouse ScrollWheel', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': None, 'altNegativeButton': None, 'altPositiveButton': None, 'gravity': 0, 'dead': 0, 'sensitivity': 0.1, 'snap': 0, 'invert': 0, 'type': 1, 'axis': 2, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Horizontal', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': None, 'altNegativeButton': None, 'altPositiveButton': None, 'gravity': 0, 'dead': 0.19, 'sensitivity': 1, 'snap': 0, 'invert': 0, 'type': 2, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Vertical', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': None, 'altNegativeButton': None, 'altPositiveButton': None, 'gravity': 0, 'dead': 0.19, 'sensitivity': 1, 'snap': 0, 'invert': 1, 'type': 2, 'axis': 1, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Fire1', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': 'joystick button 0', 'altNegativeButton': None, 'altPositiveButton': None, 'gravity': 1000, 'dead': 0.001, 'sensitivity': 1000, 'snap': 0, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Fire2', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': 'joystick button 1', 'altNegativeButton': None, 'altPositiveButton': None, 'gravity': 1000, 'dead': 0.001, 'sensitivity': 1000, 'snap': 0, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Fire3', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': 'joystick button 2', 'altNegativeButton': None, 'altPositiveButton': None, 'gravity': 1000, 'dead': 0.001, 'sensitivity': 1000, 'snap': 0, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Jump', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': 'joystick button 3', 'altNegativeButton': None, 'altPositiveButton': None, 'gravity': 1000, 'dead': 0.001, 'sensitivity': 1000, 'snap': 0, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Submit', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': 'return', 'altNegativeButton': None, 'altPositiveButton': 'joystick button 0', 'gravity': 1000, 'dead': 0.001, 'sensitivity': 1000, 'snap': 0, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Submit', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': 'enter', 'altNegativeButton': None, 'altPositiveButton': 'space', 'gravity': 1000, 'dead': 0.001, 'sensitivity': 1000, 'snap': 0, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0},
            {'serializedVersion': 3, 'm_Name': 'Cancel', 'descriptiveName': None, 'descriptiveNegativeName': None, 'negativeButton': None, 'positiveButton': 'escape', 'altNegativeButton': None, 'altPositiveButton': 'joystick button 1', 'gravity': 1000, 'dead': 0.001, 'sensitivity': 1000, 'snap': 0, 'invert': 0, 'type': 0, 'axis': 0, 'joyNum': 0}
        ])

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
