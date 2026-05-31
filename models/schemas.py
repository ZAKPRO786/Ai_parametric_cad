from pydantic import BaseModel


class CylinderSchema(BaseModel):
    shape: str
    radius: float
    height: float


class BoxSchema(BaseModel):
    shape: str
    length: float
    width: float
    height: float


class SpacerSchema(BaseModel):
    shape: str
    outer_radius: float
    inner_radius: float
    height: float


class PipeSchema(BaseModel):
    shape: str
    outer_radius: float
    inner_radius: float
    height: float


class PlateSchema(BaseModel):
    shape: str
    length: float
    width: float
    thickness: float


class BracketSchema(BaseModel):
    shape: str
    length: float
    width: float
    height: float
    thickness: float


class GearSchema(BaseModel):
    shape: str
    teeth: int
    module: float
    thickness: float
    bore_radius: float

class PulleySchema(BaseModel):
    shape: str
    outer_diameter: float
    bore_diameter: float
    width: float


class ShaftSchema(BaseModel):
    shape: str
    diameter: float
    length: float


class FlangeSchema(BaseModel):
    shape: str
    outer_diameter: float
    thickness: float
    bore_diameter: float
class ConeSchema(BaseModel):
    shape: str
    radius: float
    height: float
class MountingPlateSchema(BaseModel):
    shape: str
    length: float
    width: float
    thickness: float
    hole_diameter: float