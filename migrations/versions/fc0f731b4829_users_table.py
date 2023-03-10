"""users table

Revision ID: fc0f731b4829
Revises: 
Create Date: 2023-01-30 22:41:15.235699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc0f731b4829'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('migrate_version')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=True))
        batch_op.drop_index('ix_user_nickname')
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)
        batch_op.drop_column('nickname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nickname', sa.VARCHAR(length=64), nullable=True))
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.create_index('ix_user_nickname', ['nickname'], unique=False)
        batch_op.drop_column('password_hash')
        batch_op.drop_column('username')

    op.create_table('migrate_version',
    sa.Column('repository_id', sa.VARCHAR(length=250), nullable=False),
    sa.Column('repository_path', sa.TEXT(), nullable=True),
    sa.Column('version', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('repository_id')
    )
    # ### end Alembic commands ###
