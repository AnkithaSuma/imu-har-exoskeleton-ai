## Results

### Model Performance and Deployment Suitability

Table 1 compares the classification accuracy, model size, and prediction time of Decision Tree, Random Forest, and XGBoost models.

XGBoost achieved the highest accuracy of 99.12%, while also maintaining a relatively small model size of 960.64 KB and the fastest prediction time of 0.506 ms. Random Forest achieved 98.16% accuracy but required a substantially larger model size of 5049.32 KB and a slower prediction time of 11.41 ms. Decision Tree had the smallest model size but lower accuracy.

These results suggest that XGBoost provides the strongest balance between classification performance and deployment feasibility for real-time smart exoskeleton applications.

### Sensor Ablation Study

The sensor ablation experiment showed that accelerometer-only features achieved 98.98% accuracy, gyroscope-only features achieved 93.07%, and combined features achieved 99.12%.

This indicates that accelerometer-derived features carry most of the discriminative information for activity recognition in the UCI HAR dataset, while gyroscope features provide complementary improvements.

### Feature Importance Analysis

Feature importance analysis showed that accelerometer-derived features dominated the top-ranked predictors. Gravity acceleration and body acceleration features were especially important for separating posture-related activities such as Sitting, Standing, and Laying.

This supports the interpretation that both movement intensity and body orientation are important for wearable activity recognition.

### Model Comparision table


    Model	        Accuracy (%)	Model Size (KB)	  Prediction Time (ms)
0	Decision Tree	93.68	        53.305664	      4.224164
1	Random Forest	98.16	        5049.321289	      11.406338
2	XGBoost	        99.12	        960.641602	      0.505992

### Sensor Ablation table


    Sensor Type	    Accuracy
0	Accelerometer	0.989803
1	Gyroscope	    0.930659
2	Combined	    0.991162



