import shutil
import pytest
import os

from texutils.utils import compare_pdfs
from texutils import TeXUtils


@pytest.fixture(autouse=True)
def setup_resources():
    print("Before test")
    os.mkdir("./tests/tmp")
    shutil.copy('./tests/sample/sample.tex', './tests/tmp/')
    shutil.copy('./tests/sample/sample.pdf', './tests/tmp/')

    yield

    print("After test")
    shutil.rmtree("./tests/tmp")


def test_tex_utils_from_file():
    tex = TeXUtils.from_tex_file('./tests/tmp/sample.tex')
    pdf = tex.create_pdf()

    assert compare_pdfs('./tests/sample/sample.pdf', './tests/tmp/sample.pdf')
