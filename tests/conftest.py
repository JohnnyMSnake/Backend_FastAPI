from __future__ import annotations

from io import BytesIO
from pathlib import Path

import pytest
from fastapi import UploadFile


FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def _upload_file_from_fixture(filename: str) -> UploadFile:
	fixture_path = FIXTURES_DIR / filename
	return UploadFile(file=BytesIO(fixture_path.read_bytes()), filename=fixture_path.name)


@pytest.fixture
def csv_upload_file() -> UploadFile:
	return _upload_file_from_fixture("prueba.csv")


@pytest.fixture
def duplicated_csv_upload_file() -> UploadFile:
	return _upload_file_from_fixture("prueba_duplicados.csv")


@pytest.fixture
def unsupported_upload_file() -> UploadFile:
	return _upload_file_from_fixture("prueba.txt")


@pytest.fixture
def xlsx_upload_file() -> UploadFile:
	return _upload_file_from_fixture("prueba.xlsx")
