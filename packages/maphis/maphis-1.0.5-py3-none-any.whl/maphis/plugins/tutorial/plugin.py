from typing import List, Optional

import numpy as np
from skimage.measure import perimeter

from maphis.plugin_creation import Plugin, Info, State, action_info, region_computation, param_int, Photo, LabelImg, \
    RegionComputation, PropertyComputation, scalar_property_computation, ScalarValue, ureg, RegionsCache, RegionProperty, Region


@action_info(name='Tutorial', description='A demonstration of plugin creation.', group='General')
class Tutorial(Plugin):

    def __init__(self, state: State, info: Optional[Info] = None):
        super().__init__(state, info)

    @staticmethod
    @region_computation(name='Blue threshold',
                        description='Segments the photo based on thresholding the blue channel.',
                        group='Segmentation')
    @param_int(name="Threshold value", description="The value to treshold the blue channel against.",
               key="threshold_value", default_value=120, min_value=0, max_value=255)
    def blue_threshold(comp: RegionComputation, photo: Photo, *args) -> List[LabelImg]:
        # get the pixel data from `photo`
        image: np.ndarray = photo.image

        # Threshold the blue channel and obtain binary mask.
        # We are interested in pixels that have blue values lower than the threshold.
        # Our plugin will work on photos with specimens photographed against a blue background.

        mask = image[:, :, 2] < comp.user_params_dict['threshold_value'].value

        # access the `Labels` LabelImg for storing regions. This is where we will store the segmentation.
        label_image: LabelImg = photo['Labels']

        # Get the label hierarchy for the `LabelImg`
        label_hierarchy = label_image.label_hierarchy

        # We will assign the segmented regions the code "1:0:0:0". However, this representation is mainly for
        # humans to be easy to interpret, internally we have to convert this code to the according integer label:
        region_label = label_hierarchy.label("1:0:0:0")

        # Now we can actually assign the regions pixel the corresponding label:
        # Where the mask is True, assign `region_label`, anywhere else assign the value 0
        label_image.label_image = np.where(mask, region_label, 0).astype(np.uint32)

        # return the label image in a list
        return [label_image]

    @staticmethod
    @scalar_property_computation(name='Perimeter',
                                 description='Computes the perimeter of regions in pixels or real units.',
                                 group='Length & area measurements',
                                 export_target='Common',
                                 default_value=ScalarValue(ureg('0 px')))
    def perimeter(comp: PropertyComputation, photo: Photo, region_labels: List[int], regions_cache: RegionsCache, props: List[str]) -> List[RegionProperty]:
        computed_perimeters: List[RegionProperty] = []

        for region_label in region_labels:
            # if a region whose label is `region_label` is not present in this `photo`s segmentation, let's move on to
            # another `region_label` in `region_labels`
            if region_label not in regions_cache.regions:
                continue
            region: Region = regions_cache.regions[region_label]

            perimeter_property: RegionProperty = comp.example('perimeter')
            perimeter_property.label = region_label

            region_perimeter_px = ScalarValue(perimeter(region.mask) * ureg('px'))

            # if `photo` has a scale available, we convert the value in pixel units to real units
            if photo.image_scale is not None:
                perimeter_property.value = ScalarValue(region_perimeter_px / photo.image_scale)
            else:
                perimeter_property.value = region_perimeter_px

            computed_perimeters.append(perimeter_property)

        return computed_perimeters