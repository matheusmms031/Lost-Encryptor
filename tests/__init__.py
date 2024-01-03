import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
print(sys.path)

from src import LostEncrypt

