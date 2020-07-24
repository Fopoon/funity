#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from unittest import TestCase

from funity import FUnityEditor, UnityProject


class FUnityEditorTestCase(TestCase):

    def test_build_player(self):

        import logging
        logging.basicConfig()
        logging.getLogger('funity').setLevel(logging.INFO)

        editor = FUnityEditor(str(FUnityEditor.find_all()[0]))

        self.assertIsNotNone(editor)

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        return_code = editor.run_build_player(
            project=project,
            build_target='Android'
        )

        self.assertEqual(0, return_code)

    def test_set_serialization_mode(self):

        editor = FUnityEditor(str(FUnityEditor.find_all()[0]))

        self.assertIsNotNone(editor)

        project_dir = Path(__file__).parent / 'unity'

        self.assertTrue(project_dir.exists())

        project = UnityProject(str(project_dir))

        return_code = editor.run_set_serialization_mode(
            project=project,
            serialization_mode='ForceText'
        )

        self.assertEqual(0, return_code)
