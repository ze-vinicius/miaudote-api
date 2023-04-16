"""create address table

Revision ID: 8318dc9cfbea
Revises: ac32269e5f2b
Create Date: 2023-04-08 09:47:42.292949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8318dc9cfbea'
down_revision = 'ac32269e5f2b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "addresses",
        sa.Column('id', sa.Integer(), sa.Identity(
            always=False), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('country', sa.String(),nullable=False),
        sa.Column('state', sa.String(),nullable=False),
        sa.Column('street_address', sa.String(),nullable=True),
        sa.Column('zip_code', sa.String(),nullable=True),
        sa.Column('pet_shelter_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('address_pkey')),
        sa.ForeignKeyConstraint(['pet_shelter_id'], ['pet_shelters.id'], name=op.f(
            'address_pet_shelter_id'), ondelete="CASCADE"),
    )


def downgrade() -> None:
    op.drop_table('addresses')
