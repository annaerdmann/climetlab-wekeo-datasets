#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations
from climetlab.decorators import normalize

from climetlab_wekeo_datasets.ecmwf.main import Main


class efas_forecast(Main):
    name = "EO:ECMWF:DAT:EFAS_FORECAST"
    dataset = "EO:ECMWF:DAT:EFAS_FORECAST"

    choices = [
        "originating_centre",
        "variable",
        "model_levels",
        "format_",
    ]

    string_selects = [
        "day",
        "leadtime_hour",
        "month",
        "product_type",
        "soil_level",
        "system_version",
        "time",
        "year",
    ]

    @normalize(
        "day",
        [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
        ],
        multiple=True,
    )
    @normalize(
        "leadtime_hour",
        [
            "0",
            "102",
            "108",
            "114",
            "12",
            "120",
            "126",
            "132",
            "138",
            "144",
            "150",
            "156",
            "162",
            "168",
            "174",
            "18",
            "180",
            "186",
            "192",
            "198",
            "204",
            "210",
            "216",
            "222",
            "228",
            "234",
            "24",
            "240",
            "246",
            "252",
            "258",
            "264",
            "270",
            "276",
            "282",
            "288",
            "294",
            "30",
            "300",
            "306",
            "312",
            "318",
            "324",
            "330",
            "336",
            "342",
            "348",
            "354",
            "36",
            "360",
            "42",
            "48",
            "54",
            "6",
            "60",
            "66",
            "72",
            "78",
            "84",
            "90",
            "96",
        ],
        multiple=True,
    )
    @normalize(
        "month",
        [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "control_forecast",
            "ensemble_perturbed_forecasts",
            "high_resolution_forecast",
        ],
        multiple=True,
    )
    @normalize(
        "soil_level",
        [
            "1",
            "2",
            "3",
        ],
        multiple=True,
    )
    @normalize(
        "system_version",
        [
            "operational",
            "version_4_0",
        ],
        multiple=True,
    )
    @normalize(
        "time",
        [
            "00:00",
            "12:00",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "2018",
            "2019",
            "2020",
            "2021",
            "2022",
            "2023",
        ],
        multiple=True,
    )
    @normalize(
        "originating_centre",
        [
            "cosmo",
            "ecmwf",
            "edzw",
        ],
    )
    @normalize(
        "variable",
        [
            "elevation_v2_0",
            "elevation_v3_0",
            "elevation_v3_5",
            "elevation_v4_0",
            "elevation_v5_0",
            "field_capacity_v2_0",
            "field_capacity_v3_0",
            "field_capacity_v3_5",
            "field_capacity_v4_0",
            "field_capacity_v5_0",
            "river_discharge_in_the_last_24_hours",
            "river_discharge_in_the_last_6_hours",
            "snow_depth_water_equivalent",
            "soil_depth_v2_0",
            "soil_depth_v3_0",
            "soil_depth_v3_5",
            "soil_depth_v4_0",
            "soil_depth_v5_0",
            "upstream_area_v2_0",
            "upstream_area_v3_0",
            "upstream_area_v3_5",
            "upstream_area_v4_0",
            "upstream_area_v5_0",
            "volumetric_soil_moisture",
            "wilting_point_v2_0",
            "wilting_point_v3_0",
            "wilting_point_v3_5",
            "wilting_point_v4_0",
            "wilting_point_v5_0",
        ],
    )
    @normalize(
        "model_levels",
        [
            "soil_levels",
            "surface_level",
        ],
    )
    @normalize(
        "format_",
        [
            "grib.zip",
            "netcdf4.zip",
        ],
    )
    def __init__(
        self,
        day,
        leadtime_hour,
        month,
        product_type,
        soil_level,
        system_version,
        time,
        year,
        originating_centre=None,
        variable=None,
        model_levels=None,
        format_=None,
    ):
        super().__init__(
            day=day,
            leadtime_hour=leadtime_hour,
            month=month,
            product_type=product_type,
            soil_level=soil_level,
            system_version=system_version,
            time=time,
            year=year,
            originating_centre=originating_centre,
            variable=variable,
            model_levels=model_levels,
            format_=format_,
        )
