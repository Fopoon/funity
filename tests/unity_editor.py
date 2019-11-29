# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from funity import UnityEditor, UnityProject


class UnityEditorTestCase(TestCase):

    def test_compile(self):

        editor = UnityEditor(str(UnityEditor.find_all()[0]))

        self.assertIsNotNone(editor)

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        tmp_path = project.path / 'tmp'

        tmp_path.mkdir(exist_ok=True)

        self.assertTrue(tmp_path.exists())

        output_file = tmp_path / 'test.dll'

        self.assertFalse(output_file.exists())

        unity_libraries = editor.get_libs()

        self.assertTrue(unity_libraries)

        csharp_assets = project.find_assets(file_extensions=['.cs'],
                                            skip_folders=UnityProject.SPECIAL_DIRS)
        csharp_files = [str(project.path / a) for a in csharp_assets]

        self.assertTrue(csharp_files)

        try:
            return_code = editor.compile(*csharp_files,
                                         out=str(output_file),
                                         references=unity_libraries,
                                         target='library')

            self.assertEqual(0, return_code)

            self.assertTrue(output_file.exists())
        finally:
            rmtree(str(tmp_path), ignore_errors=True)
