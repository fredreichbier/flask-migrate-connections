"""empty message

Revision ID: 0f14dff7473c
Revises: 
Create Date: 2019-06-13 13:20:13.610073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f14dff7473c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    print('Migration URI = {!r}'.format(op.get_bind().engine))
    print('Migration character_set_results = {}'.format(op.get_bind().execute("SELECT @@character_set_results").fetchall()[0]))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
