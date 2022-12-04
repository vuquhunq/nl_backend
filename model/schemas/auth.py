from pydantic import Field

from model.domain import IDModel, auth, users


class UserActiveRequest(users.UsernameModel, auth.PasswordModel, users.EmailModel):
  disable: bool = Field(None, alias='Disable')

class SignInRequest(users.UsernameModel, auth.PasswordModel):
  pass


class SignUpRequest(IDModel, users.UsernameModel, auth.PasswordModel, users.EmailModel):
  pass