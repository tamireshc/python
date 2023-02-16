import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("mensagem", "key")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3456, 2)
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(None, 2)
    assert encrypt_message("mensagem", 2) == "megasn_em"
    assert encrypt_message("mensagem", 4) == "mega_snem"
    assert encrypt_message("mensagem", 5) == "asnem_meg"
    assert encrypt_message("mensagem", 3) == "nem_megas"
    assert encrypt_message("mensagem", 350) == "megasnem"
