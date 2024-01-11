"""removed line_width from gridsettings

Revision ID: b925a36da48e
Revises: b43466380c79
Create Date: 2024-01-11 09:14:52.034120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b925a36da48e'
down_revision: Union[str, None] = 'b43466380c79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('grid_settings', 'line_width')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grid_settings', sa.Column('line_width', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
