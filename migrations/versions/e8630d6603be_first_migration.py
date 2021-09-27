"""first migration

Revision ID: e8630d6603be
Revises: 
Create Date: 2021-09-24 18:52:14.049955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8630d6603be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apartment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('apt_num', sa.String(length=5), nullable=True),
    sa.Column('locality', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_apartment_apt_num'), 'apartment', ['apt_num'], unique=True)
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_type', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('service_type')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=25), nullable=True),
    sa.Column('lname', sa.String(length=25), nullable=True),
    sa.Column('mobile', sa.String(length=10), nullable=True),
    sa.Column('emer_num', sa.String(length=10), nullable=True),
    sa.Column('dob', sa.DateTime(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employee_email'), 'employee', ['email'], unique=True)
    op.create_index(op.f('ix_employee_fname'), 'employee', ['fname'], unique=False)
    op.create_index(op.f('ix_employee_gender'), 'employee', ['gender'], unique=False)
    op.create_index(op.f('ix_employee_lname'), 'employee', ['lname'], unique=False)
    op.create_index(op.f('ix_employee_mobile'), 'employee', ['mobile'], unique=True)
    op.create_table('house',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('house_num', sa.String(length=5), nullable=True),
    sa.Column('bhk', sa.String(length=3), nullable=True),
    sa.Column('rent', sa.String(length=4), nullable=True),
    sa.Column('advance', sa.String(length=4), nullable=True),
    sa.Column('vacancy', sa.Boolean(), nullable=False),
    sa.Column('apt_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['apt_id'], ['apartment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_house_advance'), 'house', ['advance'], unique=False)
    op.create_index(op.f('ix_house_bhk'), 'house', ['bhk'], unique=False)
    op.create_index(op.f('ix_house_house_num'), 'house', ['house_num'], unique=False)
    op.create_index(op.f('ix_house_rent'), 'house', ['rent'], unique=False)
    op.create_index(op.f('ix_house_vacancy'), 'house', ['vacancy'], unique=False)
    op.create_table('tenant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=25), nullable=True),
    sa.Column('lname', sa.String(length=25), nullable=True),
    sa.Column('mob_num', sa.String(length=10), nullable=True),
    sa.Column('emer_num', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('dob', sa.DateTime(), nullable=False),
    sa.Column('Spouse_num', sa.String(length=10), nullable=True),
    sa.Column('house_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['house_id'], ['house.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_tenant_emer_num'), 'tenant', ['emer_num'], unique=False)
    op.create_index(op.f('ix_tenant_fname'), 'tenant', ['fname'], unique=False)
    op.create_index(op.f('ix_tenant_lname'), 'tenant', ['lname'], unique=False)
    op.create_index(op.f('ix_tenant_mob_num'), 'tenant', ['mob_num'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('emp_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['emp_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_tenant_mob_num'), table_name='tenant')
    op.drop_index(op.f('ix_tenant_lname'), table_name='tenant')
    op.drop_index(op.f('ix_tenant_fname'), table_name='tenant')
    op.drop_index(op.f('ix_tenant_emer_num'), table_name='tenant')
    op.drop_table('tenant')
    op.drop_index(op.f('ix_house_vacancy'), table_name='house')
    op.drop_index(op.f('ix_house_rent'), table_name='house')
    op.drop_index(op.f('ix_house_house_num'), table_name='house')
    op.drop_index(op.f('ix_house_bhk'), table_name='house')
    op.drop_index(op.f('ix_house_advance'), table_name='house')
    op.drop_table('house')
    op.drop_index(op.f('ix_employee_mobile'), table_name='employee')
    op.drop_index(op.f('ix_employee_lname'), table_name='employee')
    op.drop_index(op.f('ix_employee_gender'), table_name='employee')
    op.drop_index(op.f('ix_employee_fname'), table_name='employee')
    op.drop_index(op.f('ix_employee_email'), table_name='employee')
    op.drop_table('employee')
    op.drop_table('service')
    op.drop_index(op.f('ix_apartment_apt_num'), table_name='apartment')
    op.drop_table('apartment')
    # ### end Alembic commands ###