from pydantic import Field

from model.domain import IDModel, address, auth, users


class UserActiveRequest(users.UsernameModel, auth.PasswordModel, users.EmailModel):
    disable: bool = Field(None, alias='Disable')


class SignInRequest(users.UsernameModel, auth.PasswordModel):
    pass


class SignInReponse(users.UsernameModel, IDModel):
    pass


class ProfileResponse(IDModel, users.PublicNameModel, users.AvatarUrl, address.AddressStreet):
    pass


class SignUpRequest(IDModel, users.UsernameModel, auth.PasswordModel, users.EmailModel):
    pass
