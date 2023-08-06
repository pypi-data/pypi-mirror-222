"""
Models for the 'exposures' table
"""
import logging
from datetime import date, datetime
from typing import ClassVar

from pydantic import Field
from sqlalchemy import (  # event,
    Column,
    DateTime,
    Double,
    Float,
    ForeignKey,
    Integer,
    Sequence,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from mirar.pipelines.winter.models._fields import FieldsTable, fieldid_field
from mirar.pipelines.winter.models._filters import FiltersTable, fid_field
from mirar.pipelines.winter.models._imgType import ImgTypesTable
from mirar.pipelines.winter.models._nights import Nights, NightsTable
from mirar.pipelines.winter.models._programs import ProgramsTable, default_program
from mirar.pipelines.winter.models.base_model import WinterBase
from mirar.processors.sqldatabase.base_model import (
    BaseDB,
    alt_field,
    az_field,
    dec_field,
    ra_field,
)

# from mirar.utils.sql import create_q3c_extension


logger = logging.getLogger(__name__)


class ExposuresTable(WinterBase):  # pylint: disable=too-few-public-methods
    """
    Raw table in database
    """

    __tablename__ = "exposures"
    __table_args__ = {"extend_existing": True}

    uexpid = Column(
        Integer,
        Sequence(name="exposures_uexpid_seq", start=1, increment=1),
        unique=True,
        autoincrement=True,
    )
    expid = Column(Double, primary_key=True, unique=True, autoincrement=False)
    # Deterministic ID of exposure

    fid: Mapped[int] = mapped_column(ForeignKey("filters.fid"))
    filt: Mapped["FiltersTable"] = relationship(back_populates="exposures")

    nightdate: Mapped[int] = mapped_column(ForeignKey("nights.nightdate"))
    night: Mapped["NightsTable"] = relationship(back_populates="exposures")

    fieldid: Mapped[int] = mapped_column(ForeignKey("fields.fieldid"))
    field: Mapped["FieldsTable"] = relationship(back_populates="exposures")

    itid: Mapped[int] = mapped_column(ForeignKey("imgTypes.itid"))
    img_type: Mapped["ImgTypesTable"] = relationship(back_populates="exposures")

    progname: Mapped[str] = mapped_column(ForeignKey("programs.progname"))
    program_name: Mapped["ProgramsTable"] = relationship(back_populates="exposures")

    utctime = Column(DateTime(timezone=True))

    ExpTime = Column(Float, nullable=False)
    expMJD = Column(Float, nullable=False)
    airmass = Column(Float)
    tempture = Column(Float, default=-999)
    windspd = Column(Float, default=-999)
    Dewpoint = Column(Float, default=-999)
    Humidity = Column(Float, default=-999)
    Pressure = Column(Float, default=-999)

    Moonaz = Column(Float, default=-999)
    Moonalt = Column(Float, default=-999)
    Sunalt = Column(Float, default=-999)

    ra = Column(Float)
    dec = Column(Float)
    altitude = Column(Float)
    azimuth = Column(Float)

    ra_column_name = "ra"
    dec_column_name = "dec"

    raw: Mapped["RawTable"] = relationship(back_populates="exposure_ids")


# @event.listens_for(target=RawTable.__table__, identifier="after_create")
# def raw_q3c(tbl, conn, *args, **kw):
#     create_q3c_extension(
#         conn=conn,
#         __tablename__=RawTable.__tablename__,
#         ra_column_name=RawTable.ra_column_name,
#         dec_column_name=RawTable.dec_column_name,
#     )


default_unknown_field = Field(default=-999)


class Exposures(BaseDB):
    """
    A pydantic model for a raw database entry
    """

    sql_model: ClassVar = ExposuresTable

    expid: int = Field(ge=0)
    fid: int = fid_field
    nightdate: date = Field()  # FIXME : why different to obsdate?
    fieldid: int = fieldid_field
    itid: int = Field(ge=0)
    progname: str = Field(min_length=1)

    utctime: datetime = Field()
    ExpTime: float = Field(ge=0)
    expMJD: float = Field(ge=59000)

    tempture: float = default_unknown_field
    windspd: float = default_unknown_field
    Dewpoint: float = default_unknown_field
    Humidity: float = default_unknown_field
    Pressure: float = default_unknown_field

    Moonaz: float = default_unknown_field
    Moonalt: float = default_unknown_field
    Sunalt: float = default_unknown_field

    ra: float = ra_field
    dec: float = dec_field
    altitude: float = alt_field
    azimuth: float = az_field

    def insert_entry(self, returning_key_names=None) -> tuple:
        """
        Insert the pydantic-ified data into the corresponding sql database

        :return: None
        """
        night = Nights(nightdate=self.nightdate)
        logger.debug(f"Searched for night {self.nightdate}")
        if not night.exists():
            night.insert_entry()

        if not ProgramsTable().exists(values=self.progname, keys="progname"):
            default_progname = ProgramsTable().select_query(
                select_keys="progname",
                compare_values=[default_program.progname],
                compare_keys=["progname"],
            )[0][0]
            self.progname = default_progname

        return self._insert_entry()

    def exists(self) -> bool:
        """
        Checks if the pydantic-ified data exists the corresponding sql database

        :return: bool
        """
        return self.sql_model().exists(values=self.expid, keys="expid")
