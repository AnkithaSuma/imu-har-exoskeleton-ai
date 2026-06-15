Why does this paper exist? 
- Existing HAR studies often focus on recognition performance, while practical deployment considerations for smart exoskeleton systems receive less attention.

What questions am i answering? 
- Which machine learning model offers the best trade-off between recognition performance and deployment feasibility for smart exoskeleton applications?

What is my contribution?
- Developed an end-to-end Human Activity Recognition (HAR) pipeline using wearable IMU sensor data.
- Explored and preprocessed the UCI HAR dataset containing 10,299 activity samples.
- Implemented and compared Decision Tree, Random Forest, XGBoost, and LSTM models.
- Performed dimensionality reduction and visualization using PCA and t-SNE.
- Analyzed feature importance to identify key movement-related sensor features.
- Processed and modeled raw accelerometer and gyroscope time-series signals.
- Evaluated model performance using accuracy metrics and confusion matrices.
- Achieved 99.12% validation accuracy using XGBoost.
- Developed a real-time activity prediction simulation for smart exoskeleton applications.
- Created a fully documented, reproducible GitHub repository with architecture diagrams and result visualizations.