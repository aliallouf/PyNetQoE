# PyNetQoE: Python Library for Network Quality of Experience (QoE) Analysis

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python: 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)
![Field: Network Intelligence](https://img.shields.io/badge/Field-Network%20Intelligence-orange)

**PyNetQoE** is a modular Python library designed to bridge the gap between raw network telemetry and user-centric experience analysis. Built on research focusing on Video Streaming QoE, this library provides automated tools for data preprocessing, MOS (Mean Opinion Score) prediction, and user behavior clustering.

---

## 🚀 Key Features

- **Automated Preprocessing**: Intelligent handling of network device logs, including One-Hot Encoding for resolutions and automatic grouping of low-frequency OS/API versions.
- **QoE Prediction Pipeline**: Implementation of Random Forest classifiers optimized with SMOTE (Synthetic Minority Over-sampling Technique) to handle class imbalances in user ratings.
- **User Profiling**: Unsupervised learning (K-Means) module to cluster users based on performance profiles (Bitrate, Buffering, and Framerate).
- **Researcher-Friendly**: Designed to work seamlessly with PCAP-derived CSV logs.

---

## 🛠️ Installation

Clone the repository and install it in editable mode:

```bash
git clone [https://github.com/your-username/PyNetQoE.git](https://github.com/your-username/PyNetQoE.git)
cd PyNetQoE
pip install -e .    
