# Hyperspectral Image Classification with KNN and Dimensionality Reduction

## Overview

This project demonstrates a complete pipeline for hyperspectral image classification using the K-Nearest Neighbors (KNN) algorithm. It includes a crucial preprocessing step for dimensionality reduction by selecting spectral bands based on correlation analysis (Pearson and Spearman). The goal is to classify land cover types from the Indian Pines hyperspectral dataset and to compare the classification accuracy when using all bands versus a reduced set of bands.

## Features

- **End-to-End Pipeline**: From data loading to classification and visualization.
- **Dimensionality Reduction**: Implements feature selection by removing highly correlated bands using a configurable threshold.
- **Correlation Analysis**: Utilizes both Pearson and Spearman correlation metrics to analyze band relationships.
- **KNN Classification**: Employs the KNN algorithm for pixel-wise classification.
- **Comparative Analysis**: Compares the classification results of using all bands versus feature-selected bands.
- **Visualization**: Generates and saves classification maps and correlation heatmaps.
- **Modular Code**: Organized into a clear and reusable `HyperspectralAnalyzer` class.

## Pipeline

The project follows these steps:

1.  **Load Data**: The Indian Pines hyperspectral data cube and its corresponding ground truth map are loaded from `.mat` files.
2.  **Data Preparation**: The 3D data cube (Height x Width x Bands) is reshaped into a 2D matrix (Pixels x Bands) for easier processing.
3.  **Correlation Analysis**:
    *   Pearson and Spearman correlation matrices are calculated for all spectral bands.
    *   Heatmaps of these matrices are generated and saved to the `results/` directory.
4.  **Band Selection (Dimensionality Reduction)**:
    *   A subset of bands is selected by removing those with a correlation higher than a specified threshold (e.g., 0.95).
    *   This process is done independently for both Pearson and Spearman correlations.
5.  **KNN Classification**:
    *   The KNN classifier is trained and evaluated on three different sets of features:
        1.  **All Bands**: Using the original, full set of spectral bands.
        2.  **Pearson-Selected Bands**: Using the reduced set of bands from the Pearson correlation analysis.
        3.  **Spearman-Selected Bands**: Using the reduced set of bands from the Spearman correlation analysis.
    *   For each case, the data is split into training and testing sets, and the model's accuracy is evaluated.
6.  **Generate Classification Maps**:
    *   A full classification map of the entire scene is generated for each of the three feature sets.
    *   These maps are saved as PNG images in the `results/` directory.

## Project Structure

```
Project4/
├── Data/
│   ├── Indian_pines_corrected.mat
│   └── Indian_pines_gt.mat
├── results/
│   ├── classification_map_all_bands.png
│   ├── classification_map_pearson.png
│   ├── classification_map_spearman.png
│   ├── pearson_correlation_all.png
│   └── spearman_correlation_all.png
├── Src/
│   ├── analyzer.py
│   ├── config.py
│   └── main.py
└── README.md
```

## Requirements

- Python 3.x
- NumPy
- SciPy
- Pandas
- Matplotlib
- Scikit-learn
- Seaborn

You can install the required packages using pip:
```bash
pip install numpy scipy pandas matplotlib scikit-learn seaborn
```

## How to Run

1.  **Configure Parameters** (Optional):
    You can modify the parameters in `Src/config.py` to change the behavior of the pipeline, such as the KNN neighbors, test set size, or correlation threshold.

    ```python
    # Src/config.py
    CONFIG = {
        # --- Paths ---
        "file_path": "Data/Indian_pines_corrected.mat",
        "gt_file_path": "Data/Indian_pines_gt.mat",
        "output_dir": "results",
        
        # --- Analysis Parameters ---
        "correlation_threshold": 0.95,

        # --- Classification Parameters ---
        "knn_neighbors": 5,
        "test_size": 0.2,
        "random_state": 42
    }
    ```

2.  **Execute the Pipeline**:
    Run the `main.py` script from the root of the project directory:

    ```bash
    python Src/main.py
    ```

    The script will execute the entire pipeline and save the output images in the `results/` directory.

## Results

The script will generate the following files in the `results/` directory:

-   `pearson_correlation_all.png`: A heatmap of the Pearson correlation matrix for all bands.
-   `spearman_correlation_all.png`: A heatmap of the Spearman correlation matrix for all bands.
-   `classification_map_all_bands.png`: The final classification map using all spectral bands.
-   `classification_map_pearson.png`: The final classification map using the bands selected after Pearson correlation analysis.
-   `classification_map_spearman.png`: The final classification map using the bands selected after Spearman correlation analysis.

The console output will display the classification accuracy and a detailed report for each of the three classification runs.

## Dataset

This project uses the **Indian Pines** dataset, a well-known benchmark for hyperspectral image analysis.

-   **Source**: Captured by the Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) sensor over the Indian Pines test site in Northwestern Indiana.
-   **Data**: `Indian_pines_corrected.mat` contains the hyperspectral data cube with dimensions 145x145 pixels and 220 spectral bands.
-   **Ground Truth**: `Indian_pines_gt.mat` provides the ground truth with 16 different land cover classes.
