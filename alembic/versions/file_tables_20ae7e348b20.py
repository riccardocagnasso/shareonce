"""File tables

Revision ID: 20ae7e348b20
Revises: None
Create Date: 2014-01-23 14:37:05.393233

"""

# revision identifiers, used by Alembic.
revision = '20ae7e348b20'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'file',
        sa.Column('kind', sa.Unicode(), nullable=False),
        sa.Column('hash', sa.Unicode(), nullable=False),
        sa.Column('mime', sa.Unicode(), nullable=False),
        sa.Column('filename', sa.Unicode(), nullable=False),
        sa.PrimaryKeyConstraint('hash')
    )

    op.create_table(
        'image',
        sa.Column('hash', sa.Unicode(), nullable=False),
        sa.Column('height', sa.Integer(), nullable=True),
        sa.Column('width', sa.Integer(), nullable=True),
        sa.Column('thumbnail_width', sa.Integer(), nullable=True),
        sa.Column('thumbnail_height', sa.Integer(), nullable=True),
        sa.Column('mini_thumbnail_width', sa.Integer(), nullable=True),
        sa.Column('mini_thumbnail_height', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['hash'], [u'file.hash'], onupdate='CASCADE',
                                ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('hash')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    op.drop_table('file')
    ### end Alembic commands ###
