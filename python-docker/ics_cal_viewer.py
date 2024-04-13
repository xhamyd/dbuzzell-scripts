from datetime import datetime
import json
from pathlib import Path
import re

import click


def serialize_timestamp(val: str) -> dict[str, int]:
    if "Z" in val:
        date_val = datetime.strptime(val, '%Y%m%dT%H%M%SZ')
    elif "T" in val:
        date_val = datetime.strptime(val, '%Y%m%dT%H%M%S')
    else:
        date_val = datetime.strptime(val, '%Y%m%d')

    return dict(year=date_val.year,
                month=date_val.month,
                day=date_val.day,
                hour=date_val.hour,
                minute=date_val.minute,
                second=date_val.second)


def ics_to_json(ics_filestr: str, output_filestr: str):
    print(f"\nParsing {ics_filestr}... ", end="")
    ics_filepath: Path = Path(ics_filestr).resolve()
    ics_str: str = ics_filepath.read_text().replace("\\,", ",")
    ics_lines: list[str] = ics_str.splitlines()
    ics_dicts: list[list[str]] = [line.split(':', 1) for line in ics_lines if ':' in line]
    print(f"Done!")

    assert ics_dicts[0] == ['BEGIN', 'VCALENDAR']
    assert ics_dicts[-1] == ['END', 'VCALENDAR']

    # Parse the global calendar info
    CAL_NAME = TIMEZONE = None
    s_i = e_i = None
    event_i: list[tuple[int]] = list()
    for i, (k, v) in enumerate(ics_dicts):
        if k == "X-WR-CALNAME":
            CAL_NAME = v
        elif k == "X-WR-TIMEZONE":
            TIMEZONE = v
        elif v == "VEVENT":
            if k == "BEGIN":
                s_i = i
            elif k == "END":
                e_i = i
                event_i.append((s_i, e_i))

    # Parse the individual event info
    events_list: list[dict] = list()
    for s_i, e_i in event_i:
        event_dict: dict[str, datetime] = dict()
        for k, v in ics_dicts[s_i + 1:e_i]:
            if dt_match := re.match(r'DT(?P<field>[A-Z]+)', k):
                event_dict[dt_match.group('field')] = serialize_timestamp(v)
            elif k in ("CREATED", "LAST-MODIFIED"):
                event_dict[k] = serialize_timestamp(v)
            elif k in ("LOCATION", "STATUS", "SUMMARY"):
                event_dict[k] = v
            else:
                # Skip the other fields that don't seem necessary
                pass
        events_list.append(event_dict)

    out_dict = dict(name=CAL_NAME, timezone=TIMEZONE, events=events_list)

    print(f"Writing to {output_filestr}... ", end="")
    with Path(output_filestr).open('w') as out_f:
        json.dump(out_dict, out_f, indent=4)
    print("Done!")


@click.command()
@click.option('--ics-folder', '-f', type=str, help='The ICS file to read')
def cli(ics_folder):
    for ics_filepath in Path(ics_folder).glob("*.ics"):
        output_filepath = ics_filepath.with_suffix(".json")
        ics_to_json(ics_filepath, output_filepath)


if __name__ == "__main__":
    cli()
