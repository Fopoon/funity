#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from os import walk
from pathlib import Path
from shutil import copy2, move
from typing import List

from funity import UnityProject


def main():
    args = parse_arguments()
    mode = args.mode
    file_path = Path(__file__)
    data_path = file_path.parent.parent / 'funity' / 'data'
    project = UnityProject(str(file_path.parent.parent / 'tests' / 'unity'))
    target_path = project.get_assets_path() / 'funity'
    if 'export' == mode:
        src_files = get_src_files(target_path)
        log(f'Exporting {len(src_files)} files from {str(target_path)} → {str(data_path)}')
        for src in src_files:
            dst = data_path / src.relative_to(target_path)
            if not dst.exists():
                dst.parent.mkdir(parents=True, exist_ok=True)
            move(str(src), str(dst))
            log(f'↳ {str(src)} → {str(dst)}')

        log(f'Deleted files in {str(project.get_assets_path() / "funity")}')
        project.delete_asset('funity')
    elif 'import' == mode:
        log(f'Deleted files in {str(project.get_assets_path() / "funity")}')
        project.delete_asset('funity')

        src_files = get_src_files(data_path)
        log(f'Importing {len(src_files)} files from {str(data_path)} → {str(target_path)}')
        for src in src_files:
            dst = target_path / src.relative_to(data_path)
            if not dst.exists():
                dst.parent.mkdir(parents=True, exist_ok=True)
            copy2(str(src), str(dst))
            log(f'↳ {str(src)} → {str(dst)}')
    else:
        raise Exception(f'Unsupported mode: {mode}')


def get_src_files(
        path: Path,
        ignored_file_extensions: List[str] = None
) -> List[Path]:
    ignored_file_extensions = ignored_file_extensions \
        if ignored_file_extensions is not None \
        else ['.ds_store', '.meta']
    src_files = []
    for root, dirs, files in walk(str(path)):
        root_path = Path(root)
        for f in files:
            if f.casefold().endswith(tuple(ignored_file_extensions)):
                continue
            src_files.append(root_path / f)
    return src_files


def log(message: str) -> None:
    print(f' {message}')


def parse_arguments():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('-m', '--mode',
                                 help='<Required> The mode.',
                                 type=str,
                                 default='import')
    return argument_parser.parse_args(
        # ['-m', 'export']
        # ['-m', 'import']
    )


if __name__ == '__main__':
    main()
