import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


def groupby_hydroyear(ds, split=9):
    """
    Helper function for grouping a :class:`xarray.Dataset` into seperate
    Datasets for each hydrological year.

    Parameters
    ----------
    ds : :class:`xarray.Dataset`
        Needs to have a coordinate `'time'`.
    split : int, optional
        Month at whichs beginning the hydrological year is starting.
        The default is 9 (September).

    Returns
    -------
    grouped
        A `GroupBy` object patterned after :class:`pandas.GroupBy` that can be
        iterated over in the form of `(unique_value, grouped_array)` pairs

    Examples
    --------
    See :ref:`this section <groupby_hydroyear_example>` in the 1d example 
    notebook.

    """
    time = ds['time'].to_index()
    ds['hydro_year'] = time.year.where(time.month<split, time.year+1)
    return ds.groupby('hydro_year')


def layer_plot(
    ax,
    ds,
    color_variable='layer_densities',
    vmin=50.,
    vmax=550.,
    cmap='cool',
    cbar_label='Density [kg/m$^{3}$]',
    top_line_kwargs=None,
    layer_line_kwargs=None,
    colorbar=True,
    cax_kwargs=None,
):

    """
    Plot the layers in the modeled snowpack with optional coloring relating to
    one of the state variables 'layer_heights', 'layer_densities', or 
    'layer_max_densities'.

    Parameters
    ----------
    ax : :class:`matplotlib.axes.Axes`
        Axes to which the plot is written.
    ds : :class:`xarray.Dataset`
        result from :func:`convert_1d` with `return_layers` set to True.
    color_variable : str or None, optional
        The variable which determines the layer coloring. If set to None, no
        coloring of the layers will be applied. The default is
        'layer_densities'.
    vmin : float, optional
        Minimum for the colormap. The default is 50.
    vmax : float, optional
        Maximum for the colormap. The default is 550.
    cmap : str or :class:`matplotlib.colors.Colormap`
        Colormap for the layer coloring.
    cbar_label : str, optional
        Label of the colorbar. The default is 'Density [kg/m$^{3}$]'.
    top_line_kwargs : dict or None, optional
        Keyword arguments for the line at top of the snowpack. The default is
        None which sets reasonable defaults.
    layer_line_kwargs : dict or None, optional
        Keyword arguments for the lines between the snow layers. The default is
        None which sets reasonable defaults.
    colorbar : bool
        Whether to plot a colorbar or not.
    cax_kwargs : dict or None, optional
        Keyword arguments passed to :func:`matplotlib.colorbar.make_axes`. The default
        is None.
    Returns
    -------
    None.

    Notes
    -----
    If `color_variable` is not None, plotting is slower than without any coloring
    of the layers.

    Examples
    --------
    Examples are given in :ref:`the respective section <layer_plot_example>`
    of the 1d example notebook. 
    """
    d_large = ds.copy()

    if color_variable is not None:
        # drop=True leads to reduced array for faster plotting:
        d_small = d_large.where(d_large['layer_heights'] != 0, drop=True)
        d_small['layer_tops'] = d_small['layer_heights'].cumsum(dim='layers', skipna=True)
        color_norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax, clip=True)
        color_mapper = mpl.cm.ScalarMappable(norm=color_norm, cmap=cmap)

        for t in d_small['time'].to_index():
            tops = d_small['layer_tops'].sel(time=t).to_numpy()
            colors = d_small[color_variable].sel(time=t).to_numpy()
            # removing nans from tops and colors
            tops = tops[~np.isnan(colors)]
            colors = colors[~np.isnan(colors)]
            # add zero to beginning of tops 
            # for flat shading in pcolormesh, Z needs to be smaller than x and y
            y = np.concatenate((np.array([0]), tops))
            Z = colors.reshape(len(colors), 1)
            x = [mpl.dates.date2num(t)-0.5, mpl.dates.date2num(t)+0.5]
            ax.pcolormesh(
                x,
                y,
                Z,
                shading='flat',
                cmap=cmap,
                norm=color_norm)

    # we now need the complete time index for layertops to go to zero. Otherwise
    # there would be nans and and the layertops would be connected from arbitrary
    # locations
    d_large['layer_tops'] = d_large['layer_heights'].cumsum(dim='layers', skipna=True)
    # remove layers with nan in color variable in order to avoid the same layer 
    # border to be drawn several times
    tops = (d_large['layer_tops']
        .where(
            ~np.isnan(d_large['layer_densities']).all(dim='time'),
            drop=True
        )
    )
    # draw layerborders
    l_kwargs = {'lw': 0.5, 'c': 'k'}
    if layer_line_kwargs is not None:
        l_kwargs.update(layer_line_kwargs)
    ax.plot(d_large['time'].to_index(), tops.to_numpy().T, **l_kwargs)
    # draw line at top of the snowcover
    t_kwargs = {'lw': 2, 'c': 'k', 'label': 'HS modeled'}
    if top_line_kwargs is not None:
        t_kwargs.update(top_line_kwargs)
    ax.plot(d_large['time'].to_index(), d_large['hs'].to_pandas(), **t_kwargs)

    if color_variable is not None and colorbar:
        c_kwargs = {'pad': 0.01}
        if cax_kwargs is not None:
            c_kwargs.update(cax_kwargs)
        cax, _ = mpl.colorbar.make_axes(ax, **c_kwargs)
        cbar = plt.colorbar(color_mapper, cax, ax)
        cbar.set_label(cbar_label)
    return None
