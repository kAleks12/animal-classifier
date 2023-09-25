from fastapi import APIRouter, UploadFile, File

from src.server import get_error_responses
from src.server.model.image_classification import TagsDTO, TagsResponse
from src.service.image_classification_service import classify
from src.shared.enum.exception_info import ExceptionInfo

router = APIRouter(prefix='/classifier', tags=['Image Classification'])


@router.post('/classify', response_model=TagsResponse,
             responses=get_error_responses(
                 [ExceptionInfo.VALIDATION_ERROR]))
async def classify_image(file: UploadFile):
    return TagsResponse(data=classify(file))
