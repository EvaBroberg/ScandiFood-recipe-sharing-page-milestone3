"""added extra column to db

Revision ID: b78d14007902
Revises: 2bb8ca8d9ad2
Create Date: 2020-01-12 11:30:30.544878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b78d14007902'
down_revision = '2bb8ca8d9ad2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('cook_method', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipe', 'cook_method')
    # ### end Alembic commands ###
