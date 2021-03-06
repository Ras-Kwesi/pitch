"""change

Revision ID: 167f22757efe
Revises: 5e1c607d6923
Create Date: 2018-09-10 16:38:18.093112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '167f22757efe'
down_revision = '5e1c607d6923'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_comment', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_comment'], ['id'])
    op.add_column('pitches', sa.Column('poster', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['poster'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'poster')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'pitch_comment')
    # ### end Alembic commands ###
