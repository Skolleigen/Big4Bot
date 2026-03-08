import os
from pathlib import Path

# When running from source, the config is at adapters/shared/config.py
# The repository root is two directories up.
_local_root = Path(__file__).parent.parent.parent

# When installed as a pip package, Big4Bot needs to know where the methodology definitions live.
# Users should export BIG4BOT_HOME. We fallback to the local git clone path if undefined.
BIG4BOT_HOME = Path(os.getenv("BIG4BOT_HOME", _local_root))

DOMAINS_DIR = BIG4BOT_HOME / "domains"
REGISTRY_DIR = BIG4BOT_HOME / "registry"

SKILLS_INDEX_PATH = REGISTRY_DIR / "skills-index.yaml"
DEPENDENCIES_PATH = REGISTRY_DIR / "dependencies.yaml"
USAGE_POLICY_PATH = REGISTRY_DIR / "usage_policy.yaml"
