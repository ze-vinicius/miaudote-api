"""create pet shelter table

Revision ID: 633222fa2730
Revises: ba5ba6323902
Create Date: 2023-04-08 09:32:49.396219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '633222fa2730'
down_revision = 'ba5ba6323902'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "pet_shelters",
        sa.Column('id', sa.Integer(), sa.Identity(
            always=False), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('phone', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('profile_picture', sa.String(), nullable=True),
        sa.Column('instagram_address', sa.String(), nullable=True),
        sa.Column('facebook_address', sa.String(), nullable=True),
        sa.Column('twitter_address', sa.String(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pet_shelter_pkey')),
        sa.ForeignKeyConstraint(['owner_id'], ['accounts.id'], name=op.f(
            'pet_shelter_owner_id_fkey'), ondelete="CASCADE"),
    )


def downgrade() -> None:
    op.drop_table('pet_shelters')
