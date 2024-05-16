# Parkinson’s Disease Detection

## Introduction
Parkinson's disease (PD) is a progressive neurodegenerative disorder affecting millions worldwide, characterized by symptoms like tremors, rigidity, and impaired motor function. Early detection of PD is crucial for timely intervention and effective management. This project aims to develop a machine learning (ML)-based approach for PD detection using voice recordings and spiral drawings, providing a non-invasive and potentially cost-effective method for early diagnosis.

## Contributors
- Anirudh Dattu 
- Akaash Gupta
- Satya Karthikeya Singidi 
- Aryan Rongali 

## Mentor
- Dr. Hirdesh Kumar Pharasi, Professor

## Abstract
This project proposes a comprehensive ML-based approach for Parkinson’s disease detection, utilizing two distinct types of data: voice recordings and spiral drawings. The project involves feature extraction from both datasets and training ML models to discriminate between PD and healthy individuals based on these features.

## Methodology
The methodology includes the following steps:
1. **Data Preprocessing:** Raw datasets are preprocessed to handle null and missing values, ensuring the quality of the data for model training.
2. **Feature Extraction:** Relevant features are extracted from voice recordings, such as vocal tremor and speech prosody, and from spiral drawings, using techniques like Histogram of Oriented Gradients (HOG) and edge detection.
3. **Model Training:** ML models are trained on the extracted features, including Support Vector Machines (SVM), Logistic Regression, Random Forest, etc.
4. **Evaluation:** The performance of trained models is evaluated using metrics like accuracy, precision, recall, and F1-score.
5. **Optimization:** Hyperparameter tuning techniques like grid search are employed to optimize model performance.

## Dataset
Two datasets are utilized:
1. **Voice Recordings Dataset:** Collected from individuals with and without PD, containing features like sustained phonation of vowel "/a/" repeated three times.
2. **Spiral Drawings Dataset:** Digital spiral drawings categorized as PD or control, containing features like shape deviations and line quality.

## Results
- **Voice Recordings Analysis:** The Random Forest Classifier achieved the highest accuracy of 86.8% on the validation dataset.
- **Spiral Drawings Analysis:** The Random Forest Classifier achieved the highest accuracy of 80.2% on the test dataset after optimization using grid search.

## Conclusion
The results demonstrate the effectiveness of ML-based approaches in accurately detecting early signs of Parkinson’s disease using non-invasive data sources. This approach has the potential to revolutionize PD diagnosis by enabling earlier intervention and improved patient outcomes.

## License
This project is licensed under the MIT License.
