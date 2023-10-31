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


class reanalysis_carra_height_levels(Main):
    name = "EO:ECMWF:DAT:REANALYSIS_CARRA_HEIGHT_LEVELS"
    dataset = "EO:ECMWF:DAT:REANALYSIS_CARRA_HEIGHT_LEVELS"

    choices = [
        "domain",
        "product_type",
        "format_",
    ]

    string_selects = [
        "day",
        "height_level",
        "leadtime_hour",
        "month",
        "time",
        "variable",
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
        "height_level",
        [
            "100_m",
            "150_m",
            "15_m",
            "200_m",
            "250_m",
            "300_m",
            "30_m",
            "400_m",
            "500_m",
            "50_m",
            "75_m",
        ],
        multiple=True,
    )
    @normalize(
        "leadtime_hour",
        [
            "1",
            "12",
            "15",
            "18",
            "2",
            "21",
            "24",
            "27",
            "3",
            "30",
            "4",
            "5",
            "6",
            "9",
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
        "time",
        [
            "00:00",
            "03:00",
            "06:00",
            "09:00",
            "12:00",
            "15:00",
            "18:00",
            "21:00",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "pressure",
            "relative_humidity",
            "specific_cloud_ice_water_content",
            "specific_cloud_liquid_water_content",
            "temperature",
            "wind_direction",
            "wind_speed",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "1990",
            "1991",
            "1992",
            "1993",
            "1994",
            "1995",
            "1996",
            "1997",
            "1998",
            "1999",
            "2000",
            "2001",
            "2002",
            "2003",
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
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
        "domain",
        [
            "east_domain",
            "west_domain",
        ],
    )
    @normalize(
        "product_type",
        [
            "analysis",
            "forecast",
        ],
    )
    @normalize(
        "format_",
        [
            "grib",
            "netcdf",
        ],
    )
    def __init__(
        self,
        day,
        height_level,
        leadtime_hour,
        month,
        time,
        variable,
        year,
        domain=None,
        product_type=None,
        format_=None,
    ):
        super().__init__(
            day=day,
            height_level=height_level,
            leadtime_hour=leadtime_hour,
            month=month,
            time=time,
            variable=variable,
            year=year,
            domain=domain,
            product_type=product_type,
            format_=format_,
        )
