from zipfile import ZipFile
import subprocess


def extract(path_in: str, path_out: str) -> None:
    """Extract all zip files in path

    Arguments:
        path_in {str} -- Path for folder with zip files
        path_out {str} -- Path for output extract files

    Returns:
        None -- None
    """
    # Get dirs
    dirs = subprocess.os.listdir(path_in)

    # Extract zip files
    for d in dirs:
        zips = subprocess.os.listdir("{}/{}".format(path_in, d))
        for z in zips:
            file_zip = "{}/{}/{}".format(path_in, d, z)

            print("[INFO] Extract: {}".format(file_zip))

            zf = ZipFile(file_zip, "r")
            zf.extractall(path_out)
            zf.close()
