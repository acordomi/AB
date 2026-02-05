from pathlib import Path
from read_substmat import read_substmat


def test_read_substmat():

    mat_file = Path(__file__).parent / "blosum62_full.mat"

    smat = read_substmat(str(mat_file))

    assert smat["W"]["W"] == 11
    assert smat["W"]["A"] == -3
    assert smat["A"]["W"] == -3
    assert len(smat) == 20
    assert len(smat["L"]) == 20
