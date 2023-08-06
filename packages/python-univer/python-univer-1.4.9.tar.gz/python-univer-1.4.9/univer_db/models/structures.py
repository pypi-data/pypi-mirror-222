from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Date, DateTime, Unicode
from sqlalchemy.orm import relationship

from univer_db.orm import get_base


Base = get_base()


class StructureDivision(Base):
    """
    Модель "Подразделение"
    """

    __tablename__ = 'univer_structure_division_1c'

    # Идентификатор
    id = Column('structure_division_id', Integer, primary_key=True)

    # Наименование
    name_kz = Column('structure_division_name_kz', Unicode(500))
    name_ru = Column('structure_division_name_ru', Unicode(500))
    name_en = Column('structure_division_name_en', Unicode(500))

    # Родительское подразделение
    parent_id = Column('structure_division_ext', ForeignKey(
        'univer_structure_division_1c.structure_division_id'))
    parent = relationship('StructureDivision',
                          remote_side='StructureDivision.id')

    # Статус
    status = Column(Integer)

    def __repr__(self):
        return '<StructureDivision {}>'.format(self)

    def __str__(self):
        return self.name_ru


class PersonnelType(Base):
    """
    Тип сотрудника
    """
    __tablename__ = 'univer_type_personal_1c'

    # Идентификатор
    id = Column('type_personal_id', Integer, primary_key=True)

    # Наименование
    name_ru = Column('type_personal_name_ru', Unicode(100))
    name_kz = Column('type_personal_name_kz', Unicode(100))
    name_en = Column('type_personal_name_en', Unicode(100))

    # Статус
    status = Column(Integer)

    def __repr__(self):
        return '<PersonnelType {} (id={} status={})'.format(self, self.id, self.status)

    def __str__(self):
        return self.name_ru


class PersonnelStructureDivisionLink(Base):
    """
    Связь между сотрудником и подразделением
    """
    __tablename__ = 'univer_personal_struct_pos_link_1c'

    # Идентификатор
    id = Column('pers_struct_pos_link_id', Integer, primary_key=True)

    # Статус
    status = Column(Integer)

    # Сотрудник
    personnel_id = Column('personal_id', ForeignKey(
        'univer_personal.personal_id'))
    personnel = relationship('Personnel')

    # Подразделение
    structure_division_id = Column(ForeignKey(
        'univer_structure_division_1c.structure_division_id'))
    structure_division = relationship('StructureDivision')

    # Должность сотрудника
    personnel_position_id = Column('personal_position_id', ForeignKey(
        'univer_personal_position_1c.personal_position_id'))
    personnel_position = relationship('PersonnelPosition')

    # Тип сотрудника
    personnel_type_id = Column('type_id', ForeignKey(
        'univer_type_personal_1c.type_personal_id'))
    personnel_type = relationship('PersonnelType')

    # Ставка
    rate = Column('personal_rate', Float)

    def __repr__(self):
        return '<PersonnelStructureDivisionLink {}>'.format(self)

    def __str__(self):
        return '{} ({})'.format(self.personnel, self.structure_division)


class Faculty(Base):
    """
    Модель "Факультет"
    """

    __tablename__ = 'univer_faculty'

    id = Column('faculty_id', Integer, primary_key=True)
    status = Column(Integer)
    name_kz = Column('faculty_name_kz', Unicode(200))
    name_ru = Column('faculty_name_ru', Unicode(200))
    name_en = Column('faculty_name_en', Unicode(200))

    def __repr__(self):
        return "<Faculty {}>".format(self)

    def __str__(self):
        return self.name_ru


class Chair(Base):
    """
    Модель "Кафедра"
    """

    __tablename__ = 'univer_chair'

    id = Column('chair_id', Integer, primary_key=True)
    faculty_id = Column(ForeignKey('univer_faculty.faculty_id'))
    faculty = relationship('Faculty')
    status = Column(Integer)
    name_kz = Column('chair_name_kz', Unicode(200))
    name_ru = Column('chair_name_ru', Unicode(200))
    name_en = Column('chair_name_en', Unicode(200))
    structure_division_id = Column(ForeignKey(
        'univer_structure_division_1c.structure_division_id'))
    structure_division = relationship('StructureDivision')

    def __repr__(self):
        return '<Chair {}>'.format(self)

    def __str__(self):
        return self.name_ru


class PersonnelPosition(Base):
    """
    Модель "Должность сотрудника"
    """
    __tablename__ = 'univer_personal_position_1c'

    # Идентификатор
    id = Column('personal_position_id', Integer, primary_key=True)

    # Наименование
    name_ru = Column('personal_position_name_ru', Unicode(500))
    name_kz = Column('personal_position_name_kz', Unicode(500))
    name_en = Column('personal_position_name_en', Unicode(500))

    # Статус
    status = Column(Integer)

    def __repr__(self):
        return '<PersonnelPosition {}>'.format(self)

    def __str__(self):
        return self.name_ru
