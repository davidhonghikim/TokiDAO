# TokiDAO API - TODO List

This file tracks pending tasks, features to be implemented, and bugs to be fixed for the TokiDAO FastAPI backend.

## MVP Features (Backend)
- [ ] **User Management:**
    - [ ] User registration (username, email, password hashing)
    - [ ] User login (JWT generation)
    - [ ] Get current user profile
    - [ ] Update user profile (optional)
- [ ] **Plant Module:**
    - [ ] Define `Plant` Pydantic model (`app/models/plant.py`)
    - [ ] Define `PlantCreate`, `PlantUpdate`, `PlantInDB` Pydantic schemas (`app/schemas/plant.py`)
    - [ ] Implement CRUD operations for Plants (`app/crud/crud_plant.py`)
    - [ ] Create API endpoints for Plants (`app/api/v1/endpoints/plants.py`)
        - [ ] POST `/plants/` (Create Plant - authenticated)
        - [ ] GET `/plants/{plant_id}` (Get Plant by ID - public)
        - [ ] GET `/plants/` (List/Search Plants - public, with pagination and basic filtering)
        - [ ] PUT `/plants/{plant_id}` (Update Plant - authenticated, owner/admin)
        - [ ] DELETE `/plants/{plant_id}` (Delete Plant - authenticated, owner/admin)
- [ ] **Mushroom Module (similar to Plant Module):**
    - [ ] Define `Mushroom` Pydantic model
    - [ ] Define `Mushroom` Pydantic schemas
    - [ ] Implement CRUD for Mushrooms
    - [ ] Create API endpoints for Mushrooms
- [ ] **Garden Tracking Module (User-specific entries):**
    - [ ] Define `GardenEntry` model (links to User, Plant/Mushroom, date planted, notes, etc.)
    - [ ] Define `GardenEntry` schemas
    - [ ] Implement CRUD for Garden Entries (user-owned)
    - [ ] Create API endpoints for Garden Entries (user-owned)

## Post-MVP / Enhancements
- [ ] Advanced search and filtering for plants/mushrooms (e.g., by characteristics, growing conditions)
- [ ] Image upload capability for plants, mushrooms, garden entries
- [ ] Gamification elements (points, badges - define backend logic)
- [ ] Admin panel/endpoints for managing data
- [ ] Comprehensive test coverage (aim for >80%)
- [ ] Implement proper logging to `logs/errors.log` and potentially structured logging.
- [ ] Rate limiting
- [ ] Caching for frequently accessed public data

## Bugs / Issues
- [ ] (Track any bugs discovered here)

## Refactoring / Technical Debt
- [ ] (Track areas for future improvement here)
