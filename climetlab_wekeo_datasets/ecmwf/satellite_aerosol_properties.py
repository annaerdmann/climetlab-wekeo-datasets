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


class satellite_aerosol_properties(Main):
    name = "EO:ECMWF:DAT:SATELLITE_AEROSOL_PROPERTIES"
    dataset = "EO:ECMWF:DAT:SATELLITE_AEROSOL_PROPERTIES"

    choices = [
        "time_aggregation",
        "sensor_on_satellite",
        "algorithm",
        "format_",
    ]

    string_selects = [
        "day",
        "month",
        "orbit",
        "variable",
        "version",
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
        "orbit",
        [
            "ascending",
            "ascending_and_descending",
            "descending",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "aerosol_extinction_coefficient",
            "aerosol_layer_height",
            "aerosol_optical_depth",
            "dust_aerosol_layer_height",
            "dust_aerosol_optical_depth",
            "fine_mode_aerosol_optical_depth",
            "single_scattering_albedo",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "deprecated (v1.11)",
            "deprecated (v4.32)",
            "deprecated (v5.00)",
            "v0.08",
            "v1.0",
            "v1.0",
            "v1.0",
            "v1.00",
            "v1.1",
            "v1.1",
            "v1.1",
            "v1.10",
            "v1.12",
            "v1.2",
            "v1.2",
            "v2.0",
            "v2.0",
            "v2.00",
            "v2.01",
            "v2.1",
            "v2.1",
            "v2.1",
            "v2.10",
            "v2.10",
            "v2.2",
            "v2.2",
            "v2.20",
            "v2.3",
            "v2.30",
            "v2.6",
            "v2.9",
            "v3.0",
            "v3.00",
            "v3.11",
            "v3.51",
            "v3.7",
            "v4.0",
            "v4.0",
            "v4.00",
            "v4.01",
            "v4.02",
            "v4.1",
            "v4.3",
            "v4.32.latest",
            "v4.33",
            "v4.8a",
            "v5.2",
            "v6.0",
            "v7.0",
            "v7.0a",
            "v8",
            "v9",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
        ],
        multiple=True,
    )
    @normalize(
        "time_aggregation",
        [
            "5_daily_composite",
            "daily_average",
            "monthly_average",
        ],
    )
    @normalize(
        "sensor_on_satellite",
        [
            "aatsr_on_envisat",
            "atsr2_on_ers2",
            "gomos_on_envisat",
            "iasi_on_metopa",
            "iasi_on_metopb",
            "iasi_on_metopc",
            "meris_on_envisat",
            "olci_on_sentinel_3a",
            "polder_on_parasol",
            "slstr_on_sentinel_3a",
            "slstr_on_sentinel_3b",
        ],
    )
    @normalize(
        "algorithm",
        [
            "adv",
            "aergom",
            "ens",
            "grasp",
            "imars",
            "lmd",
            "mapir",
            "orac",
            "s4m",
            "s4o",
            "sdv",
            "swansea",
            "ulb",
            "xbaer",
        ],
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self,
        day,
        month,
        orbit,
        variable,
        version,
        year,
        time_aggregation=None,
        sensor_on_satellite=None,
        algorithm=None,
        format_=None,
    ):
        super().__init__(
            day=day,
            month=month,
            orbit=orbit,
            variable=variable,
            version=version,
            year=year,
            time_aggregation=time_aggregation,
            sensor_on_satellite=sensor_on_satellite,
            algorithm=algorithm,
            format_=format_,
        )
