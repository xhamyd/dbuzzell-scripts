from pathlib import Path
import struct
import sys
from typing import Union
import wave

_BITS_PER_BYTE: int = 8
_VERIFY_TYPE = Union[dict[str, int], bool]


def analyze_wav_header(wav_filepath: Path, print_header: bool = True, verify_header: _VERIFY_TYPE = True) -> None:
    """Analyzes the header of the WAV file for inspection or validation.

    Useful for debugging corrupted WAV headers or validating audio file players.

    Args:
        wav_filepath (Path): Path to the WAV file to analyze.
        print_header (bool, optional): Determines whether to display the decoded header information. Defaults to True.
        verify_header (dict[str -> int] or bool, optional): Determines whether to validate the header information.
            Will result in different behavior based on the argument's type (see below). Defaults to True.

    verify_header Accepted Types:
        * If bool, determines whether to run the standard verification checks of the header (ones that must be
            correct for all WAV headers).
        * If dict, users can provide the expected values for the following properties of the WAV file:
            - num_channels (1 for mono, 2 for stereo)
            - sample_rate  (integer only, in Hz)
            - bit_depth    (in bits, eg. 16 or 32)

    """

    print(f'Analyzing {wav_filepath} ...\n')
    total_file_size: int = wav_filepath.stat().st_size  # in bytes

    with wav_filepath.open("rb") as bin_file:
        raw_bytes: bytes = bin_file.read(44)
        # Source: https://docs.python.org/3.8/library/struct.html#format-characters
        frame: tuple = struct.unpack("<4sI4s4sIHHIIHH4sI", raw_bytes)

    # Name each section of the header
    riff_title: str = frame[0].decode()
    file_size: int = frame[1]
    file_type_header: str = frame[2].decode()
    format_chunk_header: int = frame[3].decode()
    format_data_length: int = frame[4]
    format_type: int = frame[5]  # 1 for PCM, 3 for IEEE Float, 6 for A-Law, 7 for μ-Law
                                 # Source: http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html
    num_channels: int = frame[6]
    sampling_rate: int = frame[7]
    bytes_per_second: int = frame[8]
    channel_byte_depth: int = frame[9]
    bit_depth: int = frame[10]
    section_chunk_header: str = frame[11].decode()
    data_size: int = frame[12]

    if print_header:
        print(f'{frame}')
        print(f'Bytes  1- 4: \'{riff_title}\'')
        print(f'Bytes  5- 8: {file_size} bytes')
        print(f'Bytes  9-12: \'{file_type_header}\'')
        print(f'Bytes 13-16: \'{format_chunk_header}\'')
        print(f'Bytes 17-20: {format_data_length} bits')  # Always 16, for positions 21 to 36
        format_name = {1: 'PCM', 3: 'IEEE Float', 6: 'A-Law', 7: 'μ-Law'}.get(format_type, 'UNDEFINED FORMAT!')
        print(f'Bytes 21-22: \'{format_name}\'')
        print(f'Bytes 23-24: {num_channels} channels')
        print(f'Bytes 25-28: {sampling_rate} Hz')
        print(f'Bytes 29-32: {bytes_per_second} bytes/second')
        print(f'Bytes 33-34: {channel_byte_depth} bytes/sample')
        print(f'Bytes 35-36: {bit_depth} bits/sample')
        print(f'Bytes 37-40: \'{section_chunk_header}\'')
        print(f'Bytes 41-44: {data_size} bytes\n')

    if verify_header:
        # If user-provided, use this information to validate the header information
        expected_num_channels: int = verify_header.get('num_channels', None)
        expected_sample_rate: int = verify_header.get('sample_rate', None)
        expected_bit_depth: int = verify_header.get('bit_depth', None)

        try:
            assert riff_title == "RIFF"
            # DEVNOTE: seems like people forget to subtract 8 from the total_file_size, will check data_size instead
            #assert file_size == total_file_size - 8, f"Header is malformed: {file_size=} != {total_file_size=} - 8"
            assert file_type_header == "WAVE"
            assert format_chunk_header == "fmt "
            assert format_data_length == 16
            assert format_type == 1
            if expected_num_channels is not None:
                assert num_channels == expected_num_channels
            if expected_sample_rate is not None:
                assert sampling_rate == expected_sample_rate, \
                    f"Sample Rate Mismatch: expected {expected_sample_rate}, actual {sampling_rate}"
            assert bytes_per_second == (sampling_rate * bit_depth * num_channels) / _BITS_PER_BYTE
            assert channel_byte_depth == (bit_depth * num_channels) / _BITS_PER_BYTE, \
                f"Header is malformed: {channel_byte_depth=} != ({bit_depth=} * {num_channels=}) / {_BITS_PER_BYTE}"
            if expected_bit_depth is not None:
                assert bit_depth == expected_bit_depth, f"Bit Depth Mismatch: expected {expected_bit_depth}, actual {bit_depth}"
            assert section_chunk_header == "data"
            assert data_size == total_file_size - 44
        except AssertionError:
            print('Header validation failed!\n', file=sys.stderr)
            raise

        print('Header validation passed!\n')

    # Each frame is one sample for each channel, interleaved, for PCM
    # This means frame_rate == sample_rate
    bytes_per_frame: int = int(bit_depth / _BITS_PER_BYTE) * num_channels
    num_frames: int = int(data_size / bytes_per_frame)
    duration: float = num_frames / sampling_rate

    print(f'This file is about {duration:.6f} seconds long, made up of {num_frames} frames ({bytes_per_frame} bytes per frame)\n')


def read_wav_properties(wav_filepath: str) -> None:
    """Simpler function to quickly read important properties of a provided WAV file.

    Relies heavily on the `wave` Python library's API, but still provided as general reference.

    Args:
        wav_filepath (str): The filepath to the WAV file

    """
    print(f'Reading properties of {wav_filepath} ...\n')
    with wave.open(wav_filepath, 'r') as wav_file:
        wav_params = wav_file.getparams()
        print(f"Number of channels: {wav_params.nchannels}")
        print(f"Bit depth: {wav_params.sampwidth * _BITS_PER_BYTE} bit")  # bytes-to-bit conversion
        print(f"Sample rate: {wav_params.framerate / 1000} kHz")
        print(f"Number of frames: {wav_params.nframes}")
        print(f"duration: {wav_params.nframes / wav_params.framerate}")
        print(f"compression:\n    type: {wav_params.comptype}\n    name: \"{wav_params.compname}\"\n")


if __name__ == "__main__":
    AUDIO_FILEPATH = Path(r"C:\Windows\Media\Windows Background.wav")
    expected_values = dict(num_channels=2, sample_rate=22050, bit_depth=16)

    print()
    analyze_wav_header(AUDIO_FILEPATH, print_header=True, verify_header=expected_values)

    print("====================\n")
    read_wav_properties(str(AUDIO_FILEPATH))
