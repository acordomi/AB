from read_substmat_half import read_substmat
from print_substmat import print_substmat
from pathlib import Path


def test_print_substmat_header(capsys):
    """Test that the header row is formatted correctly."""
    mat_file = Path(__file__).parent / "blosum62_half.mat"
    smat = read_substmat(mat_file)
    print_substmat(smat)
    captured = capsys.readouterr()
    # Header with 5 spaces at start, then 4 spaces between amino acids
    assert captured.out.startswith(
        "     A    R    N    D    C    Q    E    G    H    I    L    K    M    F    P    S    T    W    Y    V\n"
    )


def test_print_substmat_data_row(capsys):
    """Test that a data row is formatted correctly with right-justified numbers."""
    mat_file = Path(__file__).parent / "blosum62_half.mat"
    smat = read_substmat(mat_file)
    print_substmat(smat)
    captured = capsys.readouterr()
    # Check that numbers are right-justified with 3 spaces separator
    assert "E   -1    0    0    2   -4    2    5" in captured.out
