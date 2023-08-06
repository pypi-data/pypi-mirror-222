import enum
from dataclasses import dataclass

__all__ = ["Tag", "EnvType", "AnnotationType"]


class Tag(str, enum.Enum):
    """
    Namespace for useful tags that deepchecks case use
    You can use `AppContext` to pass user tags to deepchecks

    USER_INPUT
        Relevant only for auto_collect=True and for cases where there is no clear understanding
        For what is the "user input" (like in the case of `openai.Completion`)

    USER_ID
        The external user that used the AI model

    EXT_INTERACTION_ID
        An external unique id the user can set, this id can be used later on to annotate the interaction
        if EXT_INTERACTION_ID was not supplied by the user, deepchecks will try to capture openai response id
        (i.e. - {"id": <openai unique id>, ...} and will set it as the "ext_interaction_id" of the logged interaction
    """
    USER_INPUT = "user_input"
    USER_ID = "user_id"
    EXT_INTERACTION_ID = "ext_interaction_id"


class EnvType(str, enum.Enum):
    PROD = "PROD"
    EVAL = "EVAL"


class AnnotationType(str, enum.Enum):
    GOOD = "good"
    BAD = "bad"
    UNKNOWN = "unknown"
