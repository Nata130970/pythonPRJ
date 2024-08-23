from pydantic import BaseModel, field_validator
from pydantic.color import Color
from test.baseclasses import GlobalErrorMesages


class Map(BaseModel):
    geometry: str
    color: Color
    layer_color: Color
    vtec: float


class ColorMap(BaseModel):
    color: str
    value: float

    @field_validator('color')
    def check_field_color(cls, color):
        if '#' in color:
            return color
        else:
            raise ValueError(GlobalErrorMesages.WRONG_FIELD_COLOR_IN_SCHEMA)
