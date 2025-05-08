from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, Annotated, List
from datetime import datetime
import uuid
from enum import Enum

# Define MediaType Enum
class MediaType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"
    DOCUMENT = "document"
    AUDIO = "audio"

# Define MediaItem Model
class MediaItem(BaseModel):
    url: HttpUrl
    media_type: MediaType = Field(default=MediaType.IMAGE)
    caption: Optional[str] = None
    uploaded_at: Annotated[datetime, Field(default_factory=datetime.utcnow)]

    class Config:
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }
        json_schema_extra = {
            "example": {
                "url": "https://example.com/images/image.jpg",
                "media_type": "image",
                "caption": "A beautiful example image",
                "uploaded_at": "2024-05-08T10:30:00Z"
            }
        }

# Define Plant Model
class Plant(BaseModel):
    id: Annotated[uuid.UUID, Field(default_factory=uuid.uuid4, alias="_id")]
    name: str
    species: Optional[str] = None
    description: Optional[str] = None
    media: List[MediaItem] = Field(default_factory=list) # Changed from image_url, defaults to empty list

    # Tracking timestamps
    created_at: Annotated[datetime, Field(default_factory=datetime.utcnow)]
    updated_at: Annotated[datetime, Field(default_factory=datetime.utcnow)]

    # Pydantic model configuration
    class Config:
        populate_by_name = True # Allows using alias _id for id field
        json_encoders = {
            uuid.UUID: str, # Serialize UUID to str
            datetime: lambda dt: dt.isoformat() # Serialize datetime to ISO format string
        }
        json_schema_extra = {
            "example": {
                "_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Peace Lily",
                "species": "Spathiphyllum wallisii",
                "description": "A popular indoor houseplant, known for its air-purifying qualities and white spathes.",
                "media": [
                    {
                        "url": "https://example.com/images/peace_lily_1.jpg",
                        "media_type": "image",
                        "caption": "Front view",
                        "uploaded_at": "2024-05-08T10:30:00Z"
                    },
                    {
                        "url": "https://example.com/videos/peace_lily_care.mp4",
                        "media_type": "video",
                        "caption": "Care instructions",
                        "uploaded_at": "2024-05-08T10:35:00Z"
                    }
                ],
                "created_at": "2024-05-08T10:00:00Z",
                "updated_at": "2024-05-08T11:00:00Z"
            }
        }

# Example Usage (not part of the file, just for illustration):
# if __name__ == "__main__":
#     # Example 1: Plant with media
#     plant_data_1 = {
#         "name": "Monstera Deliciosa",
#         "species": "Monstera deliciosa",
#         "description": "Known for its iconic split leaves.",
#         "media": [
#             {"url": "https://example.com/monstera1.jpg", "caption": "Young plant"},
#             {"url": "https://example.com/monstera_video.mp4", "media_type": "video", "caption": "Time-lapse growth"}
#         ]
#     }
#     new_plant_1 = Plant(**plant_data_1)
#     print("--- Plant 1 (with media) ---")
#     print(new_plant_1.model_dump_json(by_alias=True, indent=2))

#     # Example 2: Plant without media (media will default to empty list)
#     plant_data_2 = {
#         "name": "ZZ Plant",
#         "species": "Zamioculcas zamiifolia"
#     }
#     new_plant_2 = Plant(**plant_data_2)
#     print("\n--- Plant 2 (without media) ---")
#     print(new_plant_2.model_dump_json(by_alias=True, indent=2))

#     # Example 3: Creating plant with specific ID and timestamps
#     plant_data_3 = {
#         "_id": uuid.uuid4(),
#         "name": "Fiddle Leaf Fig",
#         "species": "Ficus lyrata",
#         "created_at": datetime.utcnow(),
#         "updated_at": datetime.utcnow()
#     }
#     new_plant_3 = Plant(**plant_data_3)
#     print("\n--- Plant 3 (with specific ID) ---")
#     print(new_plant_3.model_dump_json(by_alias=True, indent=2))
