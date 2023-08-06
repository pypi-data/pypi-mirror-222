#! /usr/bin/env python
"""
Module with various fits handling functions.
"""


__author__ = "Carlos Alberto Gomez Gonzalez"
__all__ = ["open_fits", "info_fits",
           "write_fits", "verify_fits", "byteswap_array"]


import os
import numpy as np
from astropy.io import fits as ap_fits
from astropy.io.fits import HDUList
from ..config.paramenum import ALL_FITS


def open_fits(fitsfilename, n=0, get_header=False, ignore_missing_end=False,
              precision=np.float32, return_memmap=False, verbose=True,
              **kwargs):
    """
    Load a fits file into memory as numpy array.

    Parameters
    ----------
    fitsfilename : string or pathlib.Path
        Name of the fits file or ``pathlib.Path`` object
    n : int, optional
        It chooses which HDU to open. Default is the first one. If n is equal
        to -2, opens and returns all extensions.
    header : bool, optional
        Whether to return the header along with the data or not.
    precision : numpy dtype, optional
        Float precision, by default np.float32 or single precision float.
    ignore_missing_end : bool optional
        Allows to open fits files with a header missing END card.
    return_memmap : bool, optional
        If True, the function returns the handle to the FITS file opened by
        mmap. With the hdulist, array data of each HDU to be accessed with mmap,
        rather than being read into memory all at once. This is particularly
        useful for working with very large arrays that cannot fit entirely into
        physical memory.
    verbose : bool, optional
        If True prints message of completion.
    **kwargs: optional
        Optional arguments to the astropy.io.fits.open() function. E.g.
        "output_verify" can be set to ignore, in case of non-standard header.

    Returns
    -------
    hdulist : HDU or HDUList
        [memmap=True] FITS file ``n`` hdulist. If n equals -2, returns the whole
        hdulist.
    data : numpy ndarray or list of numpy ndarrays
        [memmap=False] Array containing the frames of the fits-cube. If n
        equals -2, returns a list of all arrays.
    header : dict or list of dict
        [memmap=False, header=True] Dictionary containing the fits header.
        If n equals -2, returns a list of all dictionnaries.

    """
    fitsfilename = str(fitsfilename)
    if not os.path.isfile(fitsfilename):
        fitsfilename += ".fits"

    hdulist = ap_fits.open(
        fitsfilename, ignore_missing_end=ignore_missing_end, memmap=True, **kwargs
    )

    # Opening all extensions in a MEF
    if n == ALL_FITS:
        data_list = []
        header_list = []
        if return_memmap:
            return hdulist

        for index, element in enumerate(hdulist):
            data, header = _return_data_fits(
                hdulist=hdulist,
                index=index,
                precision=precision,
                verbose=verbose,
            )
            data_list.append(data)
            header_list.append(header)

        hdulist.close()
        if get_header:
            if verbose:
                print(f"All fits HDU data and headers succesfully loaded.")
            return data_list, header_list
        else:
            if verbose:
                print(f"All fits HDU data succesfully loaded.")
            return data_list
    # Opening only a specified extension
    else:
        if return_memmap:
            return hdulist[n]

        data, header = _return_data_fits(
            hdulist=hdulist,
            index=n,
            precision=precision,
            verbose=verbose,
        )
        hdulist.close()
        if get_header:
            return data, header
        else:
            return data


def _return_data_fits(
    hdulist: HDUList,
    index: int,
    precision=np.float32,
    verbose: bool = True,
):
    """
    Subfunction used to return data (and header) from a given index.

    Parameters
    ----------
    hdulist : HDUList
        List of FITS cubes with their headers.
    index : int
        The wanted index to extract.
    """
    data = hdulist[index].data
    data = np.array(data, dtype=precision)
    header = hdulist[index].header

    if verbose:
        print(
            f"Fits HDU-{index} data successfully loaded, header available. "
            f"Data shape: {data.shape}"
        )
    return data, header


def byteswap_array(array):
    """FITS files are stored in big-endian byte order. All modern CPUs are
    little-endian byte order, so at some point you have to byteswap the data.
    Some FITS readers (cfitsio, the fitsio python module) do the byteswap when
    reading the data from disk to memory, so we get numpy arrays in native
    (little-endian) byte order. Unfortunately, astropy.io.fits does not byteswap
    for us, and we get numpy arrays in non-native byte order. However, most of
    the time we never notice this because when you do any numpy operations on
    such arrays, numpy uses an intermediate buffer to byteswap the array behind
    the scenes and returns the result as a native byte order array. Some
    operations require the data to be byteswaped before and will complain about
    it. This function will help in those cases.

    Parameters
    ----------
    array : numpy ndarray
        2d input array.

    Returns
    -------
    array_out : numpy ndarray
        2d resulting array after the byteswap operation.

    Note
    ----
    More info about byteswapping here:
    http://docs.scipy.org/doc/numpy-1.10.1/user/basics.byteswapping.html

    """
    array_out = array.byteswap().newbyteorder()
    return array_out


def info_fits(fitsfilename, **kwargs):
    """
    Print the information about a fits file.

    Parameters
    ----------
    fitsfilename : str
        Path to the fits file.
    **kwargs: optional
        Optional arguments to the astropy.io.fits.open() function. E.g.
        "output_verify" can be set to ignore, in case of non-standard header.

    """
    with ap_fits.open(fitsfilename, memmap=True, **kwargs) as hdulist:
        hdulist.info()


def verify_fits(fitsfilename):
    """
    Verify "the FITS standard" of a fits file or list of fits.

    Parameters
    ----------
    fitsfilename : string or list
        Path to the fits file or list with fits filename paths.

    """
    if isinstance(fitsfilename, list):
        for ffile in fitsfilename:
            with ap_fits.open(ffile) as f:
                f.verify()
    else:
        with ap_fits.open(fitsfilename) as f:
            f.verify()


def write_fits(fitsfilename, array, header=None, output_verify="exception",
               precision=np.float32, verbose=True):
    """
    Write array and header into FITS file.

    If there is a previous file with the same filename then it's replaced.

    Parameters
    ----------
    fitsfilename : string
        Full path of the fits file to be written.
    array : numpy ndarray or tuple of numpy ndarray
        Array(s) to be written into a fits file. If a tuple of several arrays,
        the fits file will be written as a multiple extension fits file
    header : numpy ndarray, or tuple of headers, optional
        Header dictionary, or tuple of headers for a multiple extension fits
        file.
    output_verify : str, optional
        {"fix", "silentfix", "ignore", "warn", "exception"}
        Verification options:
        https://docs.astropy.org/en/stable/io/fits/api/verification.html
    precision : numpy dtype, optional
        Float precision, by default np.float32 or single precision float.
    verbose : bool, optional
        If True prints message.

    """

    if not fitsfilename.endswith(".fits"):
        fitsfilename += ".fits"

    res = "saved"
    if os.path.exists(fitsfilename):
        os.remove(fitsfilename)
        res = "overwritten"

    if isinstance(array, tuple):
        new_hdul = ap_fits.HDUList()
        if header is None:
            header = [None] * len(array)
        elif not isinstance(header, tuple):
            header = [header] * len(array)
        elif len(header) != len(array):
            msg = "If input header is a tuple, it should have the same length "
            msg += "as tuple of arrays."
            raise ValueError(msg)

        for i in range(len(array)):
            array_tmp = array[i].astype(precision, copy=False)
            new_hdul.append(ap_fits.ImageHDU(array_tmp, header=header[i]))

        new_hdul.writeto(fitsfilename, output_verify=output_verify)
    else:
        array = array.astype(precision, copy=False)
        ap_fits.writeto(fitsfilename, array, header, output_verify)

    if verbose:
        print("Fits file successfully {}".format(res))
