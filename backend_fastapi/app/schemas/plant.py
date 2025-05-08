from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, List, Annotated
from datetime import datetime
import uuid

from app.models.plant import MediaType # Import MediaType from the model

# --- MediaItem Schemas --- 

class MediaItemBase(BaseModel):
    url: HttpUrl
    media_type: MediaType = Field(default=MediaType.IMAGE)
    caption: Optional[str] = None

class MediaItemCreate(MediaItemBase):
    # Inherits all fields from MediaItemBase
    # No additional fields needed for creation by user initially
    pass

class MediaItemResponse(MediaItemBase):
    uploaded_at: datetime

    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }
        json_schema_extra = {
            "example": {
                "url": "https://example.com/images/plant_image.jpg",
                "media_type": "image",
                "caption": "Beautiful plant in bloom",
                "uploaded_at": "2024-05-08T12:00:00Z"
            }
        }

# --- Plant Schemas --- 

class PlantBase(BaseModel):
    name: str
    species: Optional[str] = None
    description: Optional[str] = None
    media: Optional[List[MediaItemCreate]] = Field(default_factory=list)

class PlantCreate(PlantBase):
    # Inherits all fields from PlantBase
    # ID, created_at, updated_at will be set by the server/database
    pass

class PlantUpdate(BaseModel):
    # All fields are optional for an update operation
    name: Optional[str] = None
    species: Optional[str] = None
    description: Optional[str] = None
    media: Optional[List[MediaItemCreate]] = None # Allows replacing or adding media
    # updated_at will be set by the server automatically

# Schema for representing a Plant as it is in the database, including all fields from the model
class PlantInDB(PlantBase):
    id: Annotated[uuid.UUID, Field(alias="_id")] # From model
    created_at: datetime # From model
    updated_at: datetime # From model
    media: List[MediaItemResponse] = Field(default_factory=list) # Use MediaItemResponse here

    class Config:
        populate_by_name = True
        json_encoders = {
            uuid.UUID: str,
            datetime: lambda dt: dt.isoformat()
        }

# Schema for responses when returning a single plant or list of plants
class PlantResponse(PlantBase):
    id: uuid.UUID # No alias needed for response, use field name 'id'
    created_at: datetime
    updated_at: datetime
    media: List[MediaItemResponse] = Field(default_factory=list) # Use MediaItemResponse here

    class Config:
        populate_by_name = True # If data is read using _id, it can populate id
        json_encoders = {
            uuid.UUID: str,
            datetime: lambda dt: dt.isoformat()
        }
        json_schema_extra = {
            "example": {
                "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "name": "Venus Flytrap",
                "species": "Dionaea muscipula",
                "description": "A carnivorous plant known for its trapping mechanism.",
                "media": [
                    {
                        "url": "https://example.com/images/venus_flytrap.jpg",
                        "media_type": "image",
                        "caption": "Close-up of a trap",
                        "uploaded_at": "2024-05-08T14:00:00Z"
                    }
                ],
                "created_at": "2024-05-08T13:00:00Z",
                "updated_at": "2024-05-08T15:00:00Z"
            }
        }

# Schema for a list of plants (e.g., for /plants/ endpoint)
class PlantListResponse(BaseModel):
    plants: List[PlantResponse]
    total_count: int
    # Add other pagination fields if needed, e.g., page, per_page, total_pages

    class Config:
        json_schema_extra = {
            "example": {
                "plants": [
                    {
                        "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                        "name": "Venus Flytrap",
                        "species": "Dionaea muscipula",
                        "description": "A carnivorous plant...",
                        "media": [
                            {
                                "url": "https://example.com/images/venus_flytrap.jpg",
                                "media_type": "image",
                                "caption": "Close-up",
                                "uploaded_at": "2024-05-08T14:00:00Z"
                            }
                        ],
                        "created_at": "2024-05-08T13:00:00Z",
                        "updated_at": "2024-05-08T15:00:00Z"
                    }
                ],
                "total_count": 1
            }
        }
