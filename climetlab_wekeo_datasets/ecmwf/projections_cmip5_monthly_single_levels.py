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


class projections_cmip5_monthly_single_levels(Main):
    name = "EO:ECMWF:DAT:PROJECTIONS_CMIP5_MONTHLY_SINGLE_LEVELS"
    dataset = "EO:ECMWF:DAT:PROJECTIONS_CMIP5_MONTHLY_SINGLE_LEVELS"

    choices = [
        "experiment",
        "model",
        "ensemble_member",
        "format_",
    ]

    string_selects = [
        "period",
        "variable",
    ]

    @normalize(
        "period",
        [
            "185001-185412",
            "185001-185512",
            "185001-185912",
            "185001-187512",
            "185001-189912",
            "185001-190012",
            "185001-195012",
            "185001-199012",
            "185001-200512",
            "185001-201212",
            "185101-187512",
            "185101-190012",
            "185501-185912",
            "185601-186112",
            "185912-185912",
            "185912-188411",
            "185912-195911",
            "186001-186412",
            "186001-186912",
            "186001-188412",
            "186101-186512",
            "186201-186712",
            "186501-186912",
            "186601-187012",
            "186801-187312",
            "187001-187412",
            "187001-187912",
            "187101-187512",
            "187401-187912",
            "187501-187912",
            "187601-188012",
            "187601-190012",
            "188001-188412",
            "188001-188512",
            "188001-188912",
            "188001-195012",
            "188101-188512",
            "188101-200512",
            "188412-190911",
            "188501-188912",
            "188501-190912",
            "188601-189012",
            "188601-189112",
            "189001-189412",
            "189001-189912",
            "189101-189512",
            "189201-189712",
            "189501-189912",
            "189601-190012",
            "189801-190312",
            "190001-190412",
            "190001-190912",
            "190001-194912",
            "190001-199912",
            "190101-190512",
            "190101-192512",
            "190101-195012",
            "190401-190912",
            "190501-190912",
            "190601-191012",
            "190912-193411",
            "191001-191412",
            "191001-191512",
            "191001-191912",
            "191001-193412",
            "191101-191512",
            "191501-191912",
            "191601-192012",
            "191601-192112",
            "192001-192412",
            "192001-192912",
            "192101-192512",
            "192201-192712",
            "192501-192912",
            "192601-193012",
            "192601-195012",
            "192801-193312",
            "193001-193412",
            "193001-193912",
            "193101-193512",
            "193401-193912",
            "193412-195911",
            "193501-193912",
            "193501-195912",
            "193601-194012",
            "194001-194412",
            "194001-194512",
            "194001-194912",
            "194101-194512",
            "194501-194912",
            "194601-195012",
            "194601-195112",
            "195001-195012",
            "195001-195412",
            "195001-195912",
            "195001-199912",
            "195001-199912",
            "195001-200512",
            "195001-200912",
            "195001-201212",
            "195101-195112",
            "195101-195512",
            "195101-197512",
            "195101-200012",
            "195101-200512",
            "195101-200512",
            "195101-200812",
            "195101-201012",
            "195101-201012",
            "195201-195212",
            "195201-195712",
            "195301-195312",
            "195401-195412",
            "195501-195512",
            "195501-195912",
            "195501-200512",
            "195601-195612",
            "195601-196012",
            "195701-195712",
            "195801-195812",
            "195801-196312",
            "195901-195912",
            "195912-198411",
            "195912-200110",
            "195912-200511",
            "195912-200512",
            "196001-196012",
            "196001-196412",
            "196001-196912",
            "196001-198412",
            "196101-196112",
            "196101-196512",
            "196101-200512",
            "196201-196212",
            "196301-196312",
            "196401-196412",
            "196401-196912",
            "196501-196512",
            "196501-196912",
            "196601-196612",
            "196601-197012",
            "196701-196712",
            "196801-196812",
            "196901-196912",
            "197001-197012",
            "197001-197412",
            "197001-197512",
            "197001-197912",
            "197101-197112",
            "197101-197512",
            "197201-197212",
            "197301-197312",
            "197401-197412",
            "197501-197512",
            "197501-197912",
            "197601-197612",
            "197601-198012",
            "197601-198112",
            "197601-200012",
            "197701-197712",
            "197801-197812",
            "197801-200812",
            "197804-197812",
            "197809-200811",
            "197809-200812",
            "197901-197912",
            "197901-198312",
            "197901-198812",
            "197901-200512",
            "197901-200812",
            "197901-200912",
            "197901-201012",
            "198001-198012",
            "198001-198412",
            "198001-198912",
            "198101-198112",
            "198101-198512",
            "198201-198212",
            "198201-198712",
            "198301-198312",
            "198401-198412",
            "198401-198812",
            "198412-200511",
            "198412-200512",
            "198501-198512",
            "198501-198912",
            "198501-200512",
            "198601-198612",
            "198601-199012",
            "198701-198712",
            "198801-198812",
            "198801-199312",
            "198901-198912",
            "198901-199312",
            "198901-199812",
            "199001-199012",
            "199001-199412",
            "199001-199912",
            "199101-199112",
            "199101-199512",
            "199101-200512",
            "199201-199212",
            "199301-199312",
            "199401-199412",
            "199401-199812",
            "199401-199912",
            "199501-199512",
            "199501-199912",
            "199601-199612",
            "199601-200012",
            "199701-199712",
            "199801-199812",
            "199901-199912",
            "199901-200312",
            "199901-200812",
            "200001-200012",
            "200001-200412",
            "200001-200512",
            "200001-200612",
            "200001-200912",
            "200001-200912",
            "200001-201212",
            "200101-200112",
            "200101-200512",
            "200101-201012",
            "200112-200512",
            "200201-200212",
            "200301-200312",
            "200401-200412",
            "200401-200812",
            "200501-200512",
            "200501-200912",
            "200501-206512",
            "200501-209912",
            "200501-210012",
            "200512-201111",
            "200512-203011",
            "200512-209911",
            "200512-209912",
            "200512-210012",
            "200601-200612",
            "200601-200612",
            "200601-200812",
            "200601-200912",
            "200601-201012",
            "200601-201012",
            "200601-201512",
            "200601-202512",
            "200601-203012",
            "200601-203512",
            "200601-204412",
            "200601-205012",
            "200601-205412",
            "200601-205512",
            "200601-206012",
            "200601-206512",
            "200601-209912",
            "200601-210012",
            "200601-210212",
            "200601-215012",
            "200601-220012",
            "200601-230012",
            "200701-200712",
            "200701-200712",
            "200801-200812",
            "200801-200812",
            "200812-200812",
            "200901-200911",
            "200901-200912",
            "200901-200912",
            "200901-200912",
            "201001-201012",
            "201001-201412",
            "201001-201912",
            "201101-201112",
            "201101-201512",
            "201101-201512",
            "201101-202012",
            "201112-203611",
            "201201-201212",
            "201301-201312",
            "201401-201412",
            "201501-201512",
            "201601-201612",
            "201601-202012",
            "201601-202012",
            "201601-202512",
            "201701-201712",
            "201801-201812",
            "201901-201912",
            "202001-202012",
            "202001-202912",
            "202101-202112",
            "202101-202512",
            "202101-202512",
            "202101-203012",
            "202201-202212",
            "202301-202312",
            "202401-202412",
            "202501-202512",
            "202601-202612",
            "202601-203012",
            "202601-203012",
            "202601-203512",
            "202601-205012",
            "202701-202712",
            "202801-202812",
            "202901-202912",
            "203001-203012",
            "203001-203912",
            "203012-205511",
            "203101-203112",
            "203101-203512",
            "203101-203512",
            "203101-204012",
            "203201-203212",
            "203301-203312",
            "203401-203412",
            "203501-203512",
            "203601-203612",
            "203601-204012",
            "203601-204012",
            "203601-204512",
            "203612-206111",
            "203701-203712",
            "203801-203812",
            "203901-203912",
            "204001-204012",
            "204001-204912",
            "204101-204112",
            "204101-204512",
            "204101-205012",
            "204201-204212",
            "204301-204312",
            "204401-204412",
            "204501-204512",
            "204501-210012",
            "204601-204612",
            "204601-205012",
            "204601-205512",
            "204701-204712",
            "204801-204812",
            "204901-204912",
            "205001-205012",
            "205001-205912",
            "205101-205112",
            "205101-205512",
            "205101-206012",
            "205101-207512",
            "205101-209912",
            "205101-210012",
            "205101-210112",
            "205201-205207",
            "205201-205212",
            "205301-205311",
            "205301-205312",
            "205401-205406",
            "205401-205412",
            "205501-205507",
            "205501-205512",
            "205512-208011",
            "205601-205612",
            "205601-206012",
            "205601-206512",
            "205601-209912",
            "205601-210012",
            "205701-205712",
            "205801-205812",
            "205901-205912",
            "206001-206012",
            "206001-206912",
            "206101-206112",
            "206101-206512",
            "206101-207012",
            "206101-210112",
            "206112-208611",
            "206201-206212",
            "206301-206312",
            "206401-206412",
            "206501-206512",
            "206601-206612",
            "206601-207012",
            "206601-207512",
            "206601-209912",
            "206701-206712",
            "206801-206812",
            "206901-206912",
            "207001-207012",
            "207001-207912",
            "207101-207112",
            "207101-207512",
            "207101-208012",
            "207201-207212",
            "207301-207312",
            "207401-207412",
            "207501-207512",
            "207601-207612",
            "207601-208012",
            "207601-208512",
            "207601-210012",
            "207701-207712",
            "207801-207812",
            "207901-207912",
            "208001-208012",
            "208001-208912",
            "208012-209511",
            "208012-209910",
            "208012-209911",
            "208012-209912",
            "208012-210011",
            "208012-210012",
            "208101-208112",
            "208101-208512",
            "208101-209012",
            "208201-208212",
            "208301-208312",
            "208401-208412",
            "208501-208512",
            "208601-208612",
            "208601-209012",
            "208601-209512",
            "208612-209911",
            "208612-209912",
            "208701-208712",
            "208801-208812",
            "208901-208912",
            "209001-209012",
            "209001-209912",
            "209001-210012",
            "209101-209112",
            "209101-209412",
            "209101-209512",
            "209101-210012",
            "209201-209212",
            "209301-209312",
            "209401-209412",
            "209501-209512",
            "209512-209912",
            "209601-209612",
            "209601-209912",
            "209601-210012",
            "209601-210112",
            "209601-210512",
            "209701-209712",
            "209801-209812",
            "209901-209902",
            "209901-209912",
            "209911-209912",
            "209912-210012",
            "209912-212411",
            "209912-219911",
            "210001-210012",
            "210001-230012",
            "210012-210012",
            "210101-211012",
            "210101-212512",
            "210101-215012",
            "210101-229912",
            "210101-230012",
            "210601-211512",
            "211101-212012",
            "211601-212512",
            "212101-213012",
            "212412-214911",
            "212601-213512",
            "212601-215012",
            "213101-214012",
            "213601-214512",
            "214101-215012",
            "214601-215512",
            "214912-217411",
            "215101-216012",
            "215101-217512",
            "215101-220012",
            "215601-216512",
            "216101-217012",
            "216601-217512",
            "217101-218012",
            "217412-219911",
            "217601-218512",
            "217601-220012",
            "218101-219012",
            "218601-219512",
            "219101-220012",
            "219601-220512",
            "219912-222411",
            "219912-229911",
            "220101-221012",
            "220101-222512",
            "220101-225012",
            "220601-221512",
            "221101-222012",
            "221601-222512",
            "222101-223012",
            "222412-224911",
            "222601-223512",
            "222601-225012",
            "223101-224012",
            "223601-224512",
            "224101-225012",
            "224601-225512",
            "224912-227411",
            "225101-226012",
            "225101-227512",
            "225101-230012",
            "225601-226512",
            "226101-227012",
            "226601-227512",
            "227101-228012",
            "227412-229911",
            "227601-230012",
            "228101-229012",
            "229101-230012",
            "229912-229912",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
            "10m_wind_speed",
            "2m_temperature",
            "eastward_turbulent_surface_stress",
            "evaporation",
            "maximum_2m_temperature_in_the_last_24_hours",
            "mean_precipitation_flux",
            "mean_sea_level_pressure",
            "minimum_2m_temperature_in_the_last_24_hours",
            "near_surface_relative_humidity",
            "near_surface_specific_humidity",
            "northward_turbulent_surface_stress",
            "runoff",
            "sea_ice_fraction",
            "sea_ice_plus_snow_amount",
            "sea_ice_surface_temperature",
            "sea_ice_thickness",
            "sea_surface_height_above_geoid",
            "sea_surface_salinity",
            "sea_surface_temperature",
            "skin_temperature",
            "snow_depth_over_sea_ice",
            "snowfall",
            "soil_moisture_content",
            "surface_latent_heat_flux",
            "surface_pressure",
            "surface_sensible_heat_flux",
            "surface_snow_amount",
            "surface_solar_radiation_downwards",
            "surface_thermal_radiation_downwards",
            "surface_upwelling_longwave_radiat_ion",
            "surface_upwelling_shortwave_radiation",
            "toa_incident_solar_radiation",
            "toa_outgoing_clear_sky_longwave_radiation",
            "toa_outgoing_clear_sky_short_wave_radiation",
            "toa_outgoing_longwave_radiation",
            "toa_outgoing_shortwave_radiation",
            "total_cloud_cover",
        ],
        multiple=True,
    )
    @normalize(
        "experiment",
        [
            "amip",
            "historical",
            "rcp_2_6",
            "rcp_4_5",
            "rcp_6_0",
            "rcp_8_5",
        ],
    )
    @normalize(
        "model",
        [
            "access1_0",
            "access1_3",
            "bcc_csm1_1",
            "bcc_csm1_1_m",
            "bnu_esm",
            "canam4",
            "cancm4",
            "canesm2",
            "ccsm4",
            "cesm1_bgc",
            "cesm1_cam5",
            "cesm1_fastchem",
            "cesm1_waccm",
            "cmcc_cesm",
            "cmcc_cm",
            "cmcc_cms",
            "cnrm_cm5",
            "cnrm_cm5_2",
            "csiro_mk3_6_0",
            "ec_earth",
            "fgoals_g2",
            "fgoals_s2",
            "fio_esm",
            "gfdl_cm2p1",
            "gfdl_cm3",
            "gfdl_esm2g",
            "gfdl_esm2m",
            "gfdl_hiram_c180",
            "gfdl_hiram_c360",
            "giss_e2_h",
            "giss_e2_h_cc",
            "giss_e2_r",
            "giss_e2_r_cc",
            "hadcm3",
            "hadgem2_a",
            "hadgem2_cc",
            "hadgem2_es",
            "inmcm4",
            "ipsl_cm5a_lr",
            "ipsl_cm5a_mr",
            "ipsl_cm5b_lr",
            "mpi_esm_lr",
            "mpi_esm_mr",
            "mpi_esm_p",
            "noresm1_m",
            "noresm1_me",
        ],
    )
    @normalize(
        "ensemble_member",
        [
            "r10i1p1",
            "r11i1p1",
            "r12i1p1",
            "r13i1p1",
            "r14i1p1",
            "r1i1p1",
            "r1i1p121",
            "r1i1p124",
            "r1i1p125",
            "r1i1p126",
            "r1i1p127",
            "r1i1p128",
            "r1i1p2",
            "r1i1p3",
            "r1i2p1",
            "r1i2p2",
            "r2i1p1",
            "r2i1p2",
            "r2i1p3",
            "r2i3p1",
            "r3i1p1",
            "r3i1p2",
            "r3i1p3",
            "r3i2p1",
            "r4i1p1",
            "r4i1p2",
            "r4i1p3",
            "r4i3p1",
            "r5i1p1",
            "r5i1p2",
            "r5i1p3",
            "r5i3p1",
            "r6i1p1",
            "r6i1p2",
            "r6i1p3",
            "r7i1p1",
            "r8i1p1",
            "r9i1p1",
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
        period,
        variable,
        experiment=None,
        model=None,
        ensemble_member=None,
        format_=None,
    ):
        super().__init__(
            period=period,
            variable=variable,
            experiment=experiment,
            model=model,
            ensemble_member=ensemble_member,
            format_=format_,
        )
