"""filesize in file

Revision ID: 466454cec31
Revises: 4520669b81de
Create Date: 2014-05-13 13:31:13.360082

"""

# revision identifiers, used by Alembic.
revision = '466454cec31'
down_revision = '4520669b81de'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('filesize', sa.Integer(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'filesize')
    ### end Alembic commands ###
