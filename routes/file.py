import uuid

from fastapi import APIRouter, Depends, File, UploadFile

from model.domain.auth import TokenData
from utils.jwt import get_current_user

routes = APIRouter(tags=['File'], prefix='/file')


@routes.post('/files')
async def create_file(file: bytes = File()):
  return {'file_size': len(file)}


@routes.post('/upload-file/')
def upload_file(file: UploadFile = File(), user: TokenData = Depends(get_current_user)):
  try:
    content = file.file.read()
    with open('static/'+ uuid.uuid1, 'wb') as f:
      f.write(content)
  except Exception:
    file.file.close()
  return {'filename': file.filename}
