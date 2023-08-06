from typing import Optional
from datetime import datetime, timedelta
from dataclasses import dataclass

try:
    import pyexiv2  # type: ignore
    import timezonefinder  # type: ignore
    import pytz
except ImportError:
    raise Exception(
        """Impossible to write the exif tags without the '[write-exif]' dependency (that will need to install libexiv2).
Install this package with `pip install geopic-tag-reader[write-exif]` to use this function"""
    )

tz_finder = timezonefinder.TimezoneFinder()


@dataclass
class PictureMetadata:
    capture_time: Optional[datetime] = None


def writePictureMetadata(picture: bytes, metadata: PictureMetadata) -> bytes:
    """
    Override exif metadata on raw picture and return updated bytes
    """
    if not metadata.capture_time:
        return picture

    img = pyexiv2.ImageData(picture)

    updated_exif = {}

    if metadata.capture_time:
        if metadata.capture_time.utcoffset() is None:
            metadata.capture_time = localize(metadata.capture_time, img)

        # for capture time, override GPSInfo time and DatetimeOriginal
        updated_exif["Exif.Photo.DateTimeOriginal"] = metadata.capture_time.strftime("%Y-%m-%d %H:%M:%S")
        offset = metadata.capture_time.utcoffset()
        if offset is not None:
            updated_exif["Exif.Photo.OffsetTimeOriginal"] = format_offset(offset)

        utc_dt = metadata.capture_time.astimezone(tz=pytz.UTC)
        updated_exif["Exif.GPSInfo.GPSDateStamp"] = utc_dt.strftime("%Y-%m-%d")
        updated_exif["Exif.GPSInfo.GPSTimeStamp"] = utc_dt.strftime("%H/1 %M/1 %S/1")
    img.modify_exif(updated_exif)

    return img.get_bytes()


def format_offset(offset: timedelta) -> str:
    """Format offset for OffsetTimeOriginal. Format is like "+02:00" for paris offset
    >>> format_offset(timedelta(hours=5, minutes=45))
    '+05:45'
    >>> format_offset(timedelta(hours=-3))
    '-03:00'
    """
    offset_hour, remainer = divmod(offset.total_seconds(), 3600)
    return f"{'+' if offset_hour >= 0 else '-'}{int(abs(offset_hour)):02}:{int(remainer/60):02}"


def localize(dt: datetime, metadata: pyexiv2.ImageData) -> datetime:
    """
    Localize a datetime in the timezone of the picture
    If the picture does not contains GPS position, the datetime will not be modified.
    """
    exif = metadata.read_exif()
    lon = exif["Exif.GPSInfo.GPSLongitude"]
    lon_ref = exif.get("Exif.GPSInfo.GPSLongitudeRef", "E")
    lat = exif["Exif.GPSInfo.GPSLatitude"]
    lat_ref = exif.get("Exif.GPSInfo.GPSLatitudeRef", "N")

    if not lon or not lat:
        return dt  # canot localize, returning same date

    lon = _from_dms(lon) * (1 if lon_ref == "E" else -1)
    lat = _from_dms(lat) * (1 if lat_ref == "N" else -1)

    tz_name = tz_finder.timezone_at(lng=lon, lat=lat)
    if not tz_name:
        return dt  # cannot find timezone, returning same date

    tz = pytz.timezone(tz_name)

    return tz.localize(dt)


def _from_dms(val: str) -> float:
    """Convert exif lat/lon represented as degre/minute/second into decimal
    >>> _from_dms("1/1 55/1 123020/13567")
    1.9191854417991367
    >>> _from_dms("49/1 0/1 1885/76")
    49.00688961988304
    """
    deg_raw, min_raw, sec_raw = val.split(" ")
    deg_num, deg_dec = deg_raw.split("/")
    deg = float(deg_num) / float(deg_dec)
    min_num, min_dec = min_raw.split("/")
    min = float(min_num) / float(min_dec)
    sec_num, sec_dec = sec_raw.split("/")
    sec = float(sec_num) / float(sec_dec)

    return float(deg) + float(min) / 60 + float(sec) / 3600
