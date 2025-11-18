# src/config.py

"""
Configuration settings for the hyperspectral analysis pipeline.
"""

CONFIG = {
    # --- Paths ---
    "file_path": "Data/Indian_pines_corrected.mat",
    "data_key": "indian_pines_corrected",
    "gt_file_path": "Data/Indian_pines_gt.mat",
    "gt_data_key": "indian_pines_gt",
    "output_dir": "results",
    
    # --- Analysis Parameters ---
    "correlation_threshold": 0.95,

    # --- Classification Parameters ---
    "knn_neighbors": 5,
    "test_size": 0.2,
    "random_state": 42  # for reproducibility
}