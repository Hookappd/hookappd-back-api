from sqlmodel import SQLModel, Field


class ManufacturesBase(SQLModel):
    name: str


class Manufactures(ManufacturesBase, table=True):
    id: int = Field(default=None, primary_key=True)


class ManufacturesCreate(ManufacturesBase):
    pass
