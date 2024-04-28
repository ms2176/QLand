from main import main

if __name__ == "__main__":
    args = [
        "Iraq",
        "NVDI_RF/modis_ndvi_series.csv",
        "LST_RF/modis_ndvi_series_LST.csv",
        ["CNN"],
    ]

    main(args)