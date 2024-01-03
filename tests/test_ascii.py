import sys
from pathlib import Path
import pytest



sys.path.append(str(Path(__file__).parent.parent))

from src import LostEncrypt




def test_mytest():
    env = LostEncrypt("ABC")
    assert env.data == 'ABC'

