"""Angular zero-to-master content: Beginner -> Intermediate -> Advanced -> Master."""
from ._dsl import apply_extras
from .angular_extras import EXTRAS
from .angular_beginner import TOPICS as BEGINNER
from .angular_intermediate import TOPICS as INTERMEDIATE

SUBJECT = "Angular"
TOPICS = [*BEGINNER, *INTERMEDIATE]
# real-world (English), pros, cons and new-feature sections for the detailed notes
_x = EXTRAS[: len(TOPICS)]
apply_extras(TOPICS, _x)
