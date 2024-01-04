import sys
from pathlib import Path
import pytest
from pytest import mark



sys.path.append(str(Path(__file__).parent.parent))

from LostEncryptor import LostEncrypt


@mark.asciiPlus
@mark.parametrize(
    'entrada,esperado,parametro',
    [('ABCD','BCDE',1),('abcd','bcde',1),('ABCD','CDEF',2),('abcd','cdef',2),('ABCD','DEFG',3),('abcd','defg',3)]
)
def test_asciiPlus_parametro123_sem_incrementFor(entrada,esperado,parametro):
    env = LostEncrypt(entrada)
    env.asciiPlus(parametro)
    assert env.data == esperado

