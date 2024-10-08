"""update

Revision ID: cadd74eec521
Revises: 23aa79660c07
Create Date: 2024-07-16 15:27:27.930461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cadd74eec521'
down_revision = '23aa79660c07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=50), nullable=True))
        batch_op.create_unique_constraint(None, ['title'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('title')

    # ### end Alembic commands ###
