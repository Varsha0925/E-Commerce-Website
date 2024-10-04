# Recommendation Model Website

This project is a recommendation model website built using Flask and TensorFlow. It provides recommendations based on a trained model.

## Getting Started

To get started with the project, follow these steps:

important step 
run the command to get the difined model for recommendations

```shell

python product_recommendation_miniLM.py

```
Dataset Details :https://drive.google.com/file/d/1Et8ekpb16JkX8dti-v2L9wNgH0kMAe1C/view?usp=sharing

the directory will have the pkl files.

1. Create a new conda environment and install TensorFlow:

   ```shell
   conda create -n tf tensorflow
   ```

2. Activate the conda environment:

   ```shell
   conda activate tf
   ```

3. Install the required packages:

   ```shell
   conda install -c anaconda flask
   conda install -c anaconda pandas
   conda install -c conda-forge sentence-transformers
   conda install -c anaconda scikit-learn
   conda install -c conda-forge tensorflow
   conda install -c anaconda pymysql
   conda install -c conda-forge pickle5
   conda install -c anaconda numpy
   conda install -c anaconda pillow
   ```

4. Start the project:

   ```shell
   python app.py
   ```

5. Open your web browser and navigate to `http://localhost:5000` to access the recommendation model website.

## License

This project is licensed under the [MIT License](LICENSE).


