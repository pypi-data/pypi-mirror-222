#    This script is part of navis (http://www.github.com/navis-org/navis).
#    Copyright (C) 2018 Philipp Schlegel
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

import nrrd
import os

import multiprocessing as mp
import numpy as np

from glob import glob
from pathlib import Path
from typing import Union, Iterable, Optional, Dict, Any
from typing_extensions import Literal

from .. import config, utils, core
from . import base

# Set up logging
logger = config.get_logger(__name__)


def write_nrrd(x: 'core.NeuronObject',
               filepath: Union[str, Path],
               compression_level: int = 3,
               attrs: Optional[Dict[str, Any]] = None) -> None:
    """Write VoxelNeurons or Dotprops to NRRD file(s).

    Parameters
    ----------
    x :                 VoxelNeuron | Dotprops | NeuronList
                        If multiple neurons, will generate a NRRD file
                        for each neuron (see also ``filepath``).
    filepath :          str | pathlib.Path | list thereof
                        Destination for the NRRD files. See examples for options.
                        If ``x`` is multiple neurons, ``filepath`` must either
                        be a folder, a "formattable" filename (see Examples) or
                        a list of filenames (one for each neuron in ``x``).
                        Existing files will be overwritten!
    compression_level : int 1-9
                        Lower = faster writing but larger files. Higher = slower
                        writing but smaller files.
    attrs :             dict
                        Any additional attributes will be written to NRRD header.

    Returns
    -------
    Nothing

    Examples
    --------
    Save a single neuron to a specific file:

    >>> import navis
    >>> n = navis.example_neurons(1, kind='skeleton')
    >>> vx = navis.voxelize(n, pitch='2 microns')
    >>> navis.write_nrrd(vx, tmp_dir / 'my_neuron.nrrd')

    Save multiple neurons to a folder (must exist). Filenames will be
    autogenerated as "{neuron.id}.nrrd":

    >>> import navis
    >>> nl = navis.example_neurons(5, kind='skeleton')
    >>> dp = navis.make_dotprops(nl, k=5)
    >>> navis.write_nrrd(dp, tmp_dir)

    Save multiple neurons to a folder but modify the pattern for the
    autogenerated filenames:

    >>> import navis
    >>> nl = navis.example_neurons(5, kind='skeleton')
    >>> vx = navis.voxelize(nl, pitch='2 microns')
    >>> navis.write_nrrd(vx, tmp_dir / 'voxels-{neuron.name}.nrrd')

    Save multiple neurons to a zip file:

    >>> import navis
    >>> nl = navis.example_neurons(5, kind='skeleton')
    >>> vx = navis.voxelize(nl, pitch='2 microns')
    >>> navis.write_nrrd(vx, tmp_dir / 'neuronlist.zip')

    Save multiple neurons to a zip file but modify the filenames:

    >>> import navis
    >>> nl = navis.example_neurons(5, kind='skeleton')
    >>> vx = navis.voxelize(nl, pitch='2 microns')
    >>> navis.write_nrrd(vx, tmp_dir / 'voxels-{neuron.name}.nrrd@neuronlist.zip')

    See Also
    --------
    :func:`navis.read_nrrd`
                        Import VoxelNeuron from NRRD files.

    """
    compression_level = int(compression_level)

    if (compression_level < 1) or (compression_level > 9):
        raise ValueError('`compression_level` must be 1-9, got '
                         f'{compression_level}')

    writer = base.Writer(_write_nrrd, ext='.nrrd')

    return writer.write_any(x,
                            filepath=filepath,
                            compression_level=compression_level,
                            **(attrs or {}))


def _write_nrrd(x: Union['core.VoxelNeuron', 'core.Dotprops'],
                filepath: Optional[str] = None,
                compression_level: int = 1,
                **attrs) -> None:
    """Write single neuron to NRRD file."""
    if not isinstance(x, (core.VoxelNeuron, core.Dotprops)):
        raise TypeError(f'Expected VoxelNeuron or Dotprops, got "{type(x)}"')

    header = getattr(x, "nrrd_header", {})
    header['space dimension'] = 3
    header['space directions'] = np.diag(x.units_xyz.magnitude)
    header['space units'] = [str(x.units_xyz.units)] * 3
    header.update(attrs or {})

    if isinstance(x, core.VoxelNeuron):
        data = x.grid
        if data.dtype == bool:
            data = data.astype('uint8')
    else:
        # For dotprops make a horizontal stack from points + vectors
        data = np.hstack((x.points, x.vect))
        header['k'] = x.k

    nrrd.write(str(filepath),
               data=data,
               header=header,
               compression_level=compression_level)


def read_nrrd(f: Union[str, Iterable],
              threshold: Optional[Union[int, float]] = None,
              include_subdirs: bool = False,
              parallel: Union[bool, int] = 'auto',
              output: Union[Literal['voxels'],
                            Literal['dotprops'],
                            Literal['raw']] = 'voxels',
              errors: Union[Literal['raise'],
                            Literal['log'],
                            Literal['ignore']] = 'log',
              **kwargs) -> 'core.NeuronObject':
    """Create Neuron/List from NRRD file.

    See `here <http://teem.sourceforge.net/nrrd/format.html>`_ for specs of
    NRRD file format including description of the headers.

    Parameters
    ----------
    f :                 str | iterable
                        Filename(s) or folder. If folder, will import all
                        ``.nrrd`` files.
    threshold :         int | float | None
                        For ``output='dotprops'`` only: a threshold to filter
                        low intensity voxels. If ``None``, no threshold is
                        applied and all values > 0 are converted to points.
    include_subdirs :   bool, optional
                        If True and ``f`` is a folder, will also search
                        subdirectories for ``.nrrd`` files.
    parallel :          "auto" | bool | int,
                        Defaults to ``auto`` which means only use parallel
                        processing if more than 10 NRRD files are imported.
                        Spawning and joining processes causes overhead and is
                        considerably slower for imports of small numbers of
                        neurons. Integer will be interpreted as the number of
                        cores (otherwise defaults to ``os.cpu_count() - 2``).
    output :            "voxels" | "dotprops" | "raw"
                        Determines function's output. See Returns for details.
    errors :            "raise" | "log" | "ignore"
                        If "log" or "ignore", errors will not be raised but
                        instead empty neuron will be returned.

    **kwargs
                        Keyword arguments passed to :func:`navis.make_dotprops`
                        if ``output='dotprops'``. Use this to adjust e.g. the
                        number of nearest neighbors used for calculating the
                        tangent vector by passing e.g. ``k=5``.

    Returns
    -------
    navis.VoxelNeuron
                        If ``output="voxels"`` (default): requires NRRD data to
                        be 3-dimensional voxels. VoxelNeuron will have NRRD file
                        header as ``.nrrd_header`` attribute.
    navis.Dotprops
                        If ``output="dotprops"``: requires NRRD data to be
                        either:
                          - ``(N, M, K)`` (i.e. 3D) in which case we will turn
                            voxels into a point cloud (see also ``threshold``
                            parameter)
                          - ``(N, 3)`` = x/y/z points
                          - ``(N, 6)`` = x/y/z points + x/y/z vectors
                          - ``(N, 7)`` = x/y/z points + x/y/z vectors + alpha

                        Dotprops will contain NRRD header as ``.nrrd_header``
                        attribute.
    navis.NeuronList
                        If import of multiple NRRD will return NeuronList of
                        Dotprops/VoxelNeurons.
    (image, header)     (np.ndarray, OrderedDict)
                        If ``output='raw'`` return raw data contained in NRRD
                        file.

    """
    utils.eval_param(output, name='output',
                     allowed_values=('raw', 'dotprops', 'voxels'))

    # If is directory, compile list of filenames
    if isinstance(f, (str, Path)) and Path(f).expanduser().is_dir():
        f = Path(f).expanduser()
        if not include_subdirs:
            f = [os.path.join(f, x) for x in os.listdir(f) if
                 os.path.isfile(os.path.join(f, x)) and x.endswith('.nrrd')]
        else:
            f = [y for x in os.walk(f) for y in glob(os.path.join(x[0], '*.nrrd'))]

    if utils.is_iterable(f):
        # Do not use if there is only a small batch to import
        if isinstance(parallel, str) and parallel.lower() == 'auto':
            if len(f) < 10:
                parallel = False

        if parallel:
            # Do not swap this as ``isinstance(True, int)`` returns ``True``
            if isinstance(parallel, (bool, str)):
                n_cores = os.cpu_count() - 2
            else:
                n_cores = int(parallel)

            with mp.Pool(processes=n_cores) as pool:
                results = pool.imap(_worker_wrapper, [dict(f=x,
                                                           threshold=threshold,
                                                           output=output,
                                                           errors=errors,
                                                           include_subdirs=include_subdirs,
                                                           parallel=False) for x in f],
                                    chunksize=1)

                res = list(config.tqdm(results,
                                       desc='Importing',
                                       total=len(f),
                                       disable=config.pbar_hide,
                                       leave=config.pbar_leave))

        else:
            # If not parallel just import the good 'ole way: sequentially
            res = [read_nrrd(x,
                             threshold=threshold,
                             include_subdirs=include_subdirs,
                             output=output,
                             errors=errors,
                             parallel=parallel,
                             **kwargs)
                   for x in config.tqdm(f, desc='Importing',
                                        disable=config.pbar_hide,
                                        leave=config.pbar_leave)]

        if output == 'raw':
            return [r[0] for r in res], [r[1] for r in res]

        return core.NeuronList([r for r in res if r])

    # Open the file
    f = str(Path(f).expanduser())
    fname = os.path.basename(f).split('.')[0]
    data, header = nrrd.read(f)

    if output == 'raw':
        return data, header

    # Try parsing units - this is modelled after the nrrd files you get from
    # Virtual Fly Brain (VFB)
    units = None
    su = None
    voxdim = np.array([1, 1, 1])
    if 'space directions' in header:
        sd = np.asarray(header['space directions'])
        if sd.ndim == 2:
            voxdim = np.diag(sd)[:3]
    if 'space units' in header:
        su = header['space units']
        if len(su) == 3:
            units = [f'{m} {u}' for m, u in zip(voxdim, su)]
    else:
        units = voxdim

    try:
        if output == 'dotprops':
            # If we're trying to get voxels from an image
            if data.ndim == 3:
                if threshold:
                    data = data >= threshold

                # Convert data to x/y/z coordinates
                # Note we need to multiply units before creating the Dotprops
                # - otherwise the KNN will be wrong
                x, y, z = np.where(data)
                points = np.vstack((x, y, z)).T
                points = points * voxdim

                x = core.make_dotprops(points, **kwargs)
            elif data.ndim == 2:
                if data.shape[1] == 3:
                    points, vect, alpha = data, None, None
                elif data.shape[1] == 6:
                    points, vect, alpha = data[:, :3], data[:, 3:6], None
                elif data.shape[1] == 7:
                    points, vect, alpha = data[:, :3], data[:, 3:6], data[:, 6]
                else:
                    raise ValueError('Expected data to be either (N, 3), (N, 6) '
                                     f'or (N, 7) but NRRD file contains {data.shape}')
                # Get `k` either from provided kwargs or the file's header
                k = kwargs.pop('k', header.get('k', 20))

                x = core.Dotprops(points, k=k, vect=vect, alpha=alpha, **kwargs)
            else:
                raise ValueError('Data must be 2- or 3-dimensional to extract '
                                 f'Dotprops, got {data.ndim}')

            if su and len(su) == 3:
                x.units = [f'1 {s}' for s in su]
        else:
            if data.ndim == 2:
                logger.warning(f'Data in NRRD file is of shape {data.shape} - '
                               'i.e. 2D. Could this be a point cloud/dotprops '
                               'instead of voxels?')
            x = core.VoxelNeuron(data, units=units)
    except BaseException as e:
        msg = f'Error converting file {fname} to neuron.'
        if errors == 'raise':
            raise ImportError(msg) from e
        elif errors == 'log':
            logger.error(f'{msg}: {e}')
        return

    # Add some additional properties
    x.name = fname
    x.origin = f
    x.nrrd_header = header

    return x


def _worker_wrapper(kwargs):
    """Helper for importing NRRDs using multiple processes."""
    return read_nrrd(**kwargs)
