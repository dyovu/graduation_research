from backend.api.insertion import router as insertion_router
from backend.api.compare import router as compare_router
from backend.api.retrieve import router as retrieve_router


__all__ = [
    "insertion_router",
    "retrieve_router",
    "compare_router",
]