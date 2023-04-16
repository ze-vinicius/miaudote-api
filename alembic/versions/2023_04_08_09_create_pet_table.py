"""create pet table

Revision ID: ac32269e5f2b
Revises: 633222fa2730
Create Date: 2023-04-08 09:41:55.574270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac32269e5f2b'
down_revision = '633222fa2730'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "pets",
        sa.Column('id', sa.Integer(), sa.Identity(
            always=False), nullable=False),
        sa.Column('age', sa.String(),nullable=False),
        sa.Column('description', sa.String(),nullable=True),
        sa.Column('name', sa.String(),nullable=False),
        sa.Column('sex', sa.String(),nullable=False),
        sa.Column('size', sa.String(),nullable=False),
        sa.Column('species', sa.String(),nullable=False),
        sa.Column('temper', sa.String(),nullable=False),
        sa.Column('profile_picture', sa.String(),nullable=True),
        sa.Column('adoption_status', sa.String(),nullable=False),
        sa.Column('health_status', sa.String(),nullable=False),
        sa.Column('pet_shelter_id', sa.Integer(),nullable=False),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pet_pkey')),
        sa.ForeignKeyConstraint(['pet_shelter_id'], ['pet_shelters.id'], name=op.f(
            'pet_pet_shelter_id_fkey'), ondelete="CASCADE"),
    )


def downgrade() -> None:
    op.drop_table('pets')
