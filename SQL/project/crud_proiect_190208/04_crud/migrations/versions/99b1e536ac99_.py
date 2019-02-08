"""empty message

Revision ID: 99b1e536ac99
Revises: 
Create Date: 2019-02-08 04:00:32.259656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99b1e536ac99'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('title_en', sa.String(length=100), nullable=False),
    sa.Column('audience', sa.Integer(), nullable=False),
    sa.Column('open_date', sa.String(), nullable=False),
    sa.Column('genre', sa.String(length=100), nullable=False),
    sa.Column('watch_grade', sa.String(length=100), nullable=False),
    sa.Column('score', sa.Float(), nullable=False),
    sa.Column('poster_url', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###
