import shutil
import pytest
import os

from texutils.utils import compare_pdfs
from texutils import TeXUtils

parent_directory = os.path.dirname(os.path.abspath(__file__))
tmp_folder = os.path.join(parent_directory, "tmp")
sample_folder = os.path.join(parent_directory, "sample")


@pytest.fixture(autouse=True)
def setup_resources():
    print("Before test")

    os.makedirs(tmp_folder) if not os.path.exists(tmp_folder) else None

    shutil.copy(os.path.join(sample_folder, "sample.tex"), tmp_folder)
    shutil.copy(os.path.join(sample_folder, "sample.tex.j2"), tmp_folder)

    yield

    print("After test")
    shutil.rmtree(tmp_folder)


def test_tex_utils_from_file():
    tex = TeXUtils.from_tex_file(os.path.join(tmp_folder, "sample.tex"))
    pdf = tex.create_pdf()

    assert compare_pdfs(os.path.join(sample_folder, "sample.pdf"), os.path.join(tmp_folder, "sample.pdf"))


def test_tex_utils_from_jinja_file():
    data = {"name": "World"}
    tex = TeXUtils.from_jinja_template_file(os.path.join(tmp_folder, "sample.tex.j2"), **data)
    pdf = tex.create_pdf()

    assert compare_pdfs(os.path.join(sample_folder, "sample.pdf"), os.path.join(tmp_folder, "sample.pdf"))