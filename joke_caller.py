import pyjokes

from DashAI.back.core.schema_fields import (
    BaseSchema,
    enum_field,
    schema_field,
    string_field,
)
from DashAI.back.core.utils import MultilingualString
from DashAI.back.models.text_to_text_generation_model import (
    TextToTextGenerationTaskModel,
)
from DashAI.back.plugins.settings import BasePluginSettings
from DashAI.back.tasks.text_to_text_generation_task import TextToTextGenerationTask

CALLS = {"es": "Oye", "en": "Hey"}


class Settings(BasePluginSettings):
    name: schema_field(
        string_field(),
        "Juan",
        MultilingualString(
            en="Who the joke is told to.", es="A quién se le cuenta el chiste."
        ),
        alias=MultilingualString(en="Name", es="Nombre"),
    )  # type: ignore
    language: schema_field(
        enum_field(
            list(CALLS),
            labels={
                "es": MultilingualString(en="Spanish", es="Español"),
                "en": MultilingualString(en="English", es="Inglés"),
            },
        ),
        "es",
        MultilingualString(
            en="The language of the call and the joke.",
            es="El idioma del llamado y del chiste.",
        ),
        alias=MultilingualString(en="Language", es="Idioma"),
    )  # type: ignore


class JokeCallerTask(TextToTextGenerationTask):
    DISPLAY_NAME = MultilingualString(
        en="Joke caller (plugin)", es="Chistes con llamado (plugin)"
    )


class JokeCallerSchema(BaseSchema):
    pass


class JokeCallerModel(TextToTextGenerationTaskModel):
    COMPATIBLE_COMPONENTS = ["JokeCallerTask"]
    SCHEMA = JokeCallerSchema
    DISPLAY_NAME = MultilingualString(en="Joke caller (plugin)", es="Chistoso (plugin)")

    def __init__(self, **kwargs):
        pass

    def generate(self, input):
        settings = Settings.load()
        joke = pyjokes.get_joke(language=settings.language)
        return [f'{CALLS[settings.language]}, {settings.name}: "{joke}"']
