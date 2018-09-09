"""new column

Revision ID: 4ed3e7f53099
Revises: 63977d6c32c6
Create Date: 2018-09-08 14:42:02.720534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ed3e7f53099'
down_revision = '63977d6c32c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###
