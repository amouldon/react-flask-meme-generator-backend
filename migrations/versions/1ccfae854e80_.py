"""empty message

Revision ID: 1ccfae854e80
Revises: 
Create Date: 2023-01-07 12:19:46.007452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ccfae854e80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meme',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('meme_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_meme',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('meme_template', sa.String(), nullable=False),
    sa.Column('meme_url', sa.String(), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.Column('user_input1', sa.String(), nullable=False),
    sa.Column('user_input2', sa.String(), nullable=True),
    sa.Column('user_input3', sa.String(), nullable=True),
    sa.Column('user_input4', sa.String(), nullable=True),
    sa.Column('input1_positioning', sa.JSON(), nullable=False),
    sa.Column('input2_positioning', sa.JSON(), nullable=True),
    sa.Column('input3_positioning', sa.JSON(), nullable=True),
    sa.Column('input4_positioning', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['meme_template'], ['meme.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_meme')
    op.drop_table('meme')
    # ### end Alembic commands ###