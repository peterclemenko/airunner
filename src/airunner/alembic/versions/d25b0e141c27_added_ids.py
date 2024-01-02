"""Added ids

Revision ID: d25b0e141c27
Revises: 28d612bd908c
Create Date: 2024-01-01 15:45:14.216904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd25b0e141c27'
down_revision: Union[str, None] = '28d612bd908c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("brushes") as batch_op:
        batch_op.add_column(sa.Column('generator_setting_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_brushes_generator_setting_id', 'generator_settings', ['generator_setting_id'], ['id'])

    # rest of your code


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
