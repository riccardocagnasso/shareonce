"""Upload table

Revision ID: 56899827a148
Revises: 20ae7e348b20
Create Date: 2014-01-24 15:18:16.260889

"""

# revision identifiers, used by Alembic.
revision = '56899827a148'
down_revision = '20ae7e348b20'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'upload',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('hash', sa.Unicode(), nullable=True),
        sa.ForeignKeyConstraint(['hash'], ['file.hash'],
                                onupdate='CASCADE', ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('image')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'image',
        sa.Column('hash', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('height', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('width', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('thumbnail_width', sa.INTEGER(),
                  autoincrement=False, nullable=True),
        sa.Column('thumbnail_height', sa.INTEGER(),
                  autoincrement=False, nullable=True),
        sa.Column('mini_thumbnail_width', sa.INTEGER(),
                  autoincrement=False, nullable=True),
        sa.Column('mini_thumbnail_height', sa.INTEGER(),
                  autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ['hash'], [u'file.hash'], name=u'image_hash_fkey',
            onupdate=u'CASCADE', ondelete=u'CASCADE'),
        sa.PrimaryKeyConstraint('hash', name=u'image_pkey')
    )
    op.drop_table('upload')
    ### end Alembic commands ###
