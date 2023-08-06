# `geopic-tag-reader`

GeoPicTagReader

**Usage**:

```console
$ geopic-tag-reader [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `read`: Reads EXIF metadata from a picture file,...
* `write`: Override certain exiftags of a picture and...

## `geopic-tag-reader read`

Reads EXIF metadata from a picture file, and prints results

**Usage**:

```console
$ geopic-tag-reader read [OPTIONS]
```

**Options**:

* `--image PATH`: Path to your JPEG image file  [required]
* `--help`: Show this message and exit.

## `geopic-tag-reader write`

Override certain exiftags of a picture and write a new picture in another file

**Usage**:

```console
$ geopic-tag-reader write [OPTIONS]
```

**Options**:

* `--input PATH`: Path to your JPEG image file  [required]
* `--output PATH`: Output path where to write the updated image file. If not present, the input file will be overriten.
* `--capture-time TEXT`: override capture time of the image, formated in isoformat, like '2023-06-01T12:48:01Z'. Note that if no timezone offset is defined, the datetime will be taken as local time and localized using the picture position if available.
* `--help`: Show this message and exit.
