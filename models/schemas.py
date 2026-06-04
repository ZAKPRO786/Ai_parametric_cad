from typing import List, Optional

from pydantic import BaseModel


# -------------------------
# Feature Schemas
# -------------------------

class HolePatternFeature(BaseModel):
    type: str
    count: int
    diameter: float


class ChamferFeature(BaseModel):
    type: str
    size: float


class FilletFeature(BaseModel):
    type: str
    radius: float


class ShellFeature(BaseModel):
    type: str
    thickness: float


# -------------------------
# Basic Shapes
# -------------------------

class CylinderSchema(BaseModel):
    shape: str
    radius: float
    height: float
    features: Optional[List[dict]] = []


class BoxSchema(BaseModel):
    shape: str
    length: float
    width: float
    height: float
    features: Optional[List[dict]] = []


class SpacerSchema(BaseModel):
    shape: str
    outer_radius: float
    inner_radius: float
    height: float
    features: Optional[List[dict]] = []


class PipeSchema(BaseModel):
    shape: str
    outer_radius: float
    inner_radius: float
    height: float
    features: Optional[List[dict]] = []


class PlateSchema(BaseModel):
    shape: str
    length: float
    width: float
    thickness: float
    features: Optional[List[dict]] = []


class BracketSchema(BaseModel):
    shape: str
    length: float
    width: float
    height: float
    thickness: float
    features: Optional[List[dict]] = []


class GearSchema(BaseModel):
    shape: str
    teeth: int
    module: float
    thickness: float
    bore_radius: float
    features: Optional[List[dict]] = []


# -------------------------
# Advanced Parts
# -------------------------

class PulleySchema(BaseModel):
    shape: str
    outer_diameter: float
    bore_diameter: float
    width: float
    features: Optional[List[dict]] = []


class ShaftSchema(BaseModel):
    shape: str
    diameter: float
    length: float
    features: Optional[List[dict]] = []


class FlangeSchema(BaseModel):
    shape: str
    outer_diameter: float
    thickness: float
    bore_diameter: float
    features: Optional[List[dict]] = []


class ConeSchema(BaseModel):
    shape: str
    radius: float
    height: float
    features: Optional[List[dict]] = []


class MountingPlateSchema(BaseModel):
    shape: str
    length: float
    width: float
    thickness: float
    hole_diameter: float
    features: Optional[List[dict]] = []


# -------------------------
# New UST Benchmark Parts
# -------------------------

class ElectronicsEnclosureSchema(BaseModel):
    shape: str
    length: float
    width: float
    height: float
    wall_thickness: float
    features: Optional[List[dict]] = []


class SteppedShaftSchema(BaseModel):
    shape: str
    length: float
    features: Optional[List[dict]] = []


class CalibrationBlockSchema(BaseModel):
    shape: str
    length: float
    width: float
    height: float
    features: Optional[List[dict]] = []
class EnclosureSchema(BaseModel):
    shape: str
    features: Optional[List[dict]] = []


class ClevisBracketSchema(BaseModel):
    shape: str
    features: Optional[List[dict]] = []


class PlanetaryGearSchema(BaseModel):
    shape: str
    features: Optional[List[dict]] = []


class EngineCylinderSchema(BaseModel):
    shape: str
    features: Optional[List[dict]] = []


class SpiralStaircaseSchema(BaseModel):
    shape: str
    features: Optional[List[dict]] = []
class AdvancedClevisBracketSchema(BaseModel):
    shape: str
    features: Optional[List[dict]] = []


class ImpellerSchema(BaseModel):
    shape: str
    features: Optional[List[dict]] = []
class GlobeValveSchema(BaseModel):
    shape: str
    features: Optional[List[dict]] = []
class TyreMouldSchema(BaseModel):
    shape: str
    features: Optional[List[dict]] = []