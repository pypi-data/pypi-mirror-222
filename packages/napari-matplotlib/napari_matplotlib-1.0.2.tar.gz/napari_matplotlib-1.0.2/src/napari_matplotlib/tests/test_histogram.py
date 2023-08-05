from copy import deepcopy

import pytest

from napari_matplotlib import HistogramWidget


@pytest.mark.mpl_image_compare
def test_histogram_2D(make_napari_viewer, astronaut_data):
    viewer = make_napari_viewer()
    viewer.theme = "light"
    viewer.add_image(astronaut_data[0], **astronaut_data[1])
    fig = HistogramWidget(viewer).figure
    # Need to return a copy, as original figure is too eagerley garbage
    # collected by the widget
    return deepcopy(fig)


@pytest.mark.mpl_image_compare
def test_histogram_3D(make_napari_viewer, brain_data):
    viewer = make_napari_viewer()
    viewer.theme = "light"
    viewer.add_image(brain_data[0], **brain_data[1])
    axis = viewer.dims.last_used
    slice_no = brain_data[0].shape[0] - 1
    viewer.dims.set_current_step(axis, slice_no)
    fig = HistogramWidget(viewer).figure
    # Need to return a copy, as original figure is too eagerley garbage
    # collected by the widget
    return deepcopy(fig)
