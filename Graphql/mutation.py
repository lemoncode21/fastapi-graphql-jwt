import strawberry

from Middleware.JWTBearer import IsAuthenticated
from Service.note import NoteService
from Service.authentication import AuthenticationService
from schema import NoteType, NoteInput, RegisterInput, LoginInput, LoginType


@strawberry.type
class Mutation:

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def create_note(self, note_data: NoteInput) -> NoteType:
        return await NoteService.add_note(note_data)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def delete_note(self, note_id: int) -> str:
        return await NoteService.delete(note_id)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def update_note(self, note_id: int, note_data: NoteInput) -> str:
        return await NoteService.update(note_id, note_data)

    @strawberry.mutation
    async def login(self, login_data: LoginInput) -> LoginType:
        return await AuthenticationService.login(login_data)

    @strawberry.mutation
    async def register(self, register_data: RegisterInput) -> str:
        return await AuthenticationService.register(register_data)
