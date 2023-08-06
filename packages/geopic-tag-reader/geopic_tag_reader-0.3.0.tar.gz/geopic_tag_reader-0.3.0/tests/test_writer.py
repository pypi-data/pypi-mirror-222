from datetime import datetime, timezone, timedelta
from .conftest import FIXTURE_DIR
import os
import pytest
from geopic_tag_reader import writer, reader
from PIL import Image
import io
from PIL import ExifTags
import pytz


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "1.jpg"))
def test_writePictureMetadata_capture_time(datafiles):
    capture_time = datetime(year=2023, month=6, day=1, hour=12, minute=48, second=1, tzinfo=pytz.UTC)

    with open(str(datafiles / "1.jpg"), "rb") as image_file:
        image_file_upd = writer.writePictureMetadata(image_file.read(), writer.PictureMetadata(capture_time=capture_time))

    pil_img = Image.open(io.BytesIO(image_file_upd))
    tags = reader.readPictureMetadata(pil_img)

    assert datetime.fromtimestamp(tags.ts, tz=pytz.UTC) == capture_time

    # we also check specific tags:
    pil_exif = pil_img._getexif()
    assert pil_exif[ExifTags.Base.DateTimeOriginal] == "2023-06-01 12:48:01"
    assert pil_exif[ExifTags.Base.GPSInfo][ExifTags.GPS.GPSDateStamp] == "2023-06-01"
    assert pil_exif[ExifTags.Base.GPSInfo][ExifTags.GPS.GPSTimeStamp] == (12.0, 48.0, 1.0)


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "1.jpg"))
def test_writePictureMetadata_capture_time_no_timezone(datafiles):
    capture_time = datetime(year=2023, month=6, day=1, hour=12, minute=48, second=1, tzinfo=None)

    with open(str(datafiles / "1.jpg"), "rb") as image_file:
        image_file_upd = writer.writePictureMetadata(image_file.read(), writer.PictureMetadata(capture_time=capture_time))

    pil_img = Image.open(io.BytesIO(image_file_upd))
    tags = reader.readPictureMetadata(pil_img)

    paris = pytz.timezone("Europe/Paris")
    assert datetime.fromtimestamp(tags.ts, tz=pytz.UTC) == paris.localize(capture_time).astimezone(pytz.UTC)

    pil_exif = pil_img._getexif()
    # DateTimeOriginal should be a local time, so 12:48:01 localized in Europe/Paris timezome (since it's where the picture has been taken)
    assert pil_exif[ExifTags.Base.DateTimeOriginal] == "2023-06-01 12:48:01"
    assert pil_exif[ExifTags.Base.GPSInfo][ExifTags.GPS.GPSDateStamp] == "2023-06-01"
    # GPSTimeStamp should always be in UTC
    assert pil_exif[ExifTags.Base.GPSInfo][ExifTags.GPS.GPSTimeStamp] == (10.0, 48.0, 1.0)
    assert pil_exif[ExifTags.Base.OffsetTimeOriginal] == "+02:00"
