# Zip Bomb Creator

This Python script is used for generating large files of zeros and compressing them into a zip file for testing or educational purposes.

## Usage
`python create_zipbomb.py [options]`
- -z, --zipfile: Specify the output zip file name (default: zipbomb.zip)
- -b, --block-size: Define the block size in bytes (default: 1024)
- -c, --count: Set the number of blocks to write (default: 10000)

## Example
To create a zip file named zipbomb.zip with 100 blocks of size 2048 bytes:

`python create_zipbomb.py --zipfile zipbomb.zip --block-size 2048 --count 100`
