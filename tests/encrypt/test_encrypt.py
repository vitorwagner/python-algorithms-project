from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    result = encrypt_message("Test", 1)
    assert result == "T_tse"

    result = encrypt_message("Test", 2)
    assert result == "ts_eT"

    result = encrypt_message("Test", 3)
    assert result == "seT_t"

    result = encrypt_message("Test", 4)
    assert result == "tseT"

    result = encrypt_message("Test", 6)
    assert result == "tseT"

    result = encrypt_message("a lost colony on tau ceti iv", 7)
    assert result == " tsol a_vi itec uat no ynoloc"

    result = encrypt_message("", 7)
    assert result == ""

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Teste", "Teste")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(7, 7)
