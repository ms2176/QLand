# QLand | QArdh

<center>
<img src="https://github.com/ms2176/QLand/blob/main/images/banner.png">
</center>

### Table of Contents
<ul>
   <li><a href="#Project-Outline">Project Outline</a></li>
   <li><a href="#Objective">Objective</a></li>
   <li><a href="#Case-Study">Case Study</a></li>
   <li><a href="#Research-Foundation">Research Foundation</a></li>
   <li><a href="#Conclusion">Conclusion</a></li>
   <li><a href="#Project-Structure">Project Structure</a></li>
   <li><a href="#Getting-Started-With-The-App">Getting Started With The App</a></li>
   <li><a href="#Credits">Credits</a></li>
   <li><a href="#Citations">Citations</a></li>
</ul>

## Project Outline

**QLand | QArdh** is a pioneering project developed during the NYU Quantum Computing Hackathon. The initiative leverages quantum computing technologies to enhance the monitoring and prediction of desertification, a critical environmental issue where fertile lands progressively turn into deserts. Desertification affects two-thirds of the Earth’s land surface and is driven by various factors including human activities and climate change.

![Figure1. Distribution of Desertification around the world](https://github.com/ms2176/QLand/blob/main/images/fig%20one.jpg)


## Objective
The project aims to optimize the process of analyzing and predicting key factors contributing to desertification by using both classical machine learning and quantum computing techniques. This dual approach seeks to improve accuracy and efficiency in predicting future desertification patterns.

## Case Study

### Data Collection
**Datasets**: We utilized datasets based on desertification analysis in Iraq, incorporating insights from previous studies such as the one outlined by Omdena on using machine learning and satellite data for desertification detection. (Source: [Omdena Blog](https://www.omdena.com/blog/desertification-detection-with-machine-learning-and-satellite-data)).

<img alt="Figure2. Iraq, case study region" src="https://github.com/ms2176/QLand/blob/main/images/Fig2%20Study%20case%20Region-of-interest-for-land-cover-classification-approach.jpg" width="700">
<br>
<img alt="Figure3. Iraq case study" src="https://github.com/ms2176/QLand/blob/main/images/study%20case%202.jpg" width="700">


### Classical Machine Learning Models
**Machine Learning Implementation**: We employed classical machine learning models such as Random Forest (RF) and Support Vector Machines (SVM). These models were tested with two of the four main indicators of desertification:
   - Normalized Difference Vegetation Index (NDVI)
   - Land Surface Temperature (LST)

In the following diagram, we measure the estimated scaling of the SVM algorithm as the size of the dataset increases, we can confirm a time complexity of O($n^2$) where n is the number of samples.

We use this time complexity for our job scheduling to determine the resource estimate, which we define as a time slot on a given a machine.

![Figure4.Using NDVI on SVM ](https://github.com/ms2176/QLand/blob/main/images/Using%20SVM%20with%20NDVI.png)


### Quantum Computing Application
**Quantum Job Scheduling Problem**:
   - **Definition**: In quantum computing, the job scheduling problem involves the optimal allocation of quantum computation tasks to available quantum resources (qubits, quantum gates) over time. Efficient scheduling is crucial for maximizing the utilization of quantum hardware, which is still a limited resource.
   - **Application**: For this project, we applied the Quantum Approximate Optimization Algorithm (QAOA) to solve quantum job scheduling problems. This approach aims to streamline our computational processes, thereby speeding up the analysis of desertification indicators.
   - **Implementation**: For our Job Shop Scheduling Problem (JSSP), we use several different constraints that allow us to schedule classical statistical models and AI/ML modes in situations which involve supercomputers and GPUs.
      - Execute as many jobs as possible in the nearest time over all available machines, ensuring maximum utilization.
      -  Every job should be executed exactly once over the entire system.
      -  No intersection of job execution on the same machine and time.

   <img src="https://github.com/ms2176/QLand/blob/main/images/ingest.png" width="500">

## Results
The implementation of a quantum scheduler within distributed machine learning (ML) systems has demonstrated notable efficacy in optimizing task allocation across multiple machines while minimizing execution time. Through the utilization of quantum algorithms such as the Quantum Approximate Optimization Algorithm (QAOA), the scheduler explores expansive solution spaces, seeking optimal task assignments that mitigates resource conflicts to enhance overall system performance.

Moreover, the quantum scheduler exhibits adaptability and responsiveness to dynamic changes in job demands and resource availability, affording the system the capacity to adjust task allocations. This optimization enables the scheduler to maintain efficient resource utilization and throughput, thereby augmenting the efficiency of ML model training and inference processes.

We provide an example result below with 3 machines, 2 time slots and 3 jobs, where all the machines are sucessfully ran at `t=0` .

```
fval=3.0, machine1job1time1=1.0, machine1job1time2=0.0, machine1job2time1=0.0, machine1job2time2=1.0, machine1job3time1=0.0, machine1job3time2=0.0, machine2job1time1=0.0, machine2job1time2=0.0, machine2job2time1=0.0, machine2job2time2=0.0, machine2job3time1=1.0, machine2job3time2=0.0, status=SUCCESS
```

## Research Foundation
- **Background**: In examining anthropogenic factors of desertification, our project references research that identifies four critical indicators: NDVI, LST, DGSI (Dryness Greenness Soil Index), and Albedo. However, existing research (e.g., Feng et al., 2022) points out significant challenges in accurate forecasting and prediction using these indicators. (Source: Feng, K., et al., "Monitoring Desertification Using Machine-Learning Techniques with Multiple Indicators Derived from MODIS Images in Mu Us Sandy Land, China", Remote Sensing, 2022, 14(11):2663. [DOI](https://doi.org/10.3390/rs14112663)).

## Conclusion
The QLand||QArdh project is at the forefront of integrating quantum computing with machine learning to tackle the pressing issue of desertification. By refining data analysis and prediction models, this initiative not only contributes to environmental science but also enhances our capability to manage and potentially mitigate one of the most severe ecological challenges of our time.

## Project Structure

    ├── app             <- The directly executable code of the scheduler.
    ├── images          <- Holds README images.
    ├── classical algorithms             <- Classical Algorithms used for desertification prediction.
    |   ├── LST_RF          <- Jupyter notebook illustrating the use of RF model over LST index.
    |   ├── LST_SVM         <- Jupyter notebook illustrating the use of SVM model over LST index.
    |   ├── NDVI_RF         <- Jupyter notebook illustrating the use of RF model over NVDI index.
    |   └── NDVI_SVM        <- Jupyter notebook illustrating the use of SVM model over NVDI index.
    └────
--------


## Getting Started With The App

### Requirements
1. **Python 3** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/index.html).
2. **PIP Dependencies** - install dependencies by running the following command in the project directory:
   ```bash
   $ pip install -r requirements.txt
   ```
   This will install all of the required packages within the requirements.txt file.

### Running The App

To run and test the app you need to run `main.py` file by executing the following command:

```bash
$ python3 app/main.py
```

then proceed by inputting the requested data (e.g. the NDVI csv file)

**Alternatively**, you can run the `test.py` file by executing the following command:
```bash
$ python3 app/test.py
```

## Credits
This project was developed to be presented for the Quantum Computing Hackathon at NUYAD for the year 2024.

#### Participants:
   - [Sarah Dweik](https://www.linkedin.com/in/sarahdweik), Birzeit University
   - [Mufliha Shake Dawood](https://www.linkedin.com/in/muflihadawood), Heriot-Watt University
   - [Megane Demgne](https://www.linkedin.com/in/megane-demgne), African Leadership College
   - [Loise Kinuthia](https://www.linkedin.com/in/loise-kinuthia-7964601a8), African Leadership University
   - [Yamen Ghozlan](https://linkedin.com/in/yamen-ghozlan), Philadelphia University
   - Jovan Kašćelan, NYUAD
   - [Jeanne Mukakalisa](https://www.linkedin.com/in/jeanne-mukakalisa-b191a4206), African Leadership University

#### Mentors:
   - [Ricky Young](https://www.linkedin.com/in/ricky-y-1545b3a9), Qbraid
   - [David Morcuende Cantador](https://www.linkedin.com/in/david-morcuende-cantador/), QuIC
   - [Muhammad Kashif](https://www.linkedin.com/in/muhammad-kashif-29191571), NYUAD

## Citations
<ul>
   <li><a href="https://www.omdena.com/blog/desertification-detection-with-machine-learning-and-satellite-data">Desertification Detection using Machine Learning and Satellite Data, Omdena</a></li>
   <li><a href="https://doi.org/10.3390/rs14112663">Monitoring Desertification Using Machine-Learning Techniques with Multiple Indicators Derived from MODIS Images in Mu Us Sandy Land, China, by Kun Feng, Tao Wang, Shulin Liu, Wenping Kang, Xiang Chen, Zichen Guo and Ying Zhi.</a></li>
   <li><a href="https://github.com/mareksubocz/QuantumJSP/blob/master/job_shop_scheduler.py">Quantum Shop Scheduler repository by Marek Subocz on GitHub</a></li>
   <li><a href="https://github.com/OmdenaAI/iraq-chapter-desertification-detection/tree/main">Iraq Chapter Desertification Detection, Omdena Inc on Github.</a></li>
   <li><a href="https://arxiv.org/abs/1506.08479">Quantum Annealing Implementation of Job-Shop Scheduling, by Davide Venturelli, Dominic J.J. Marchand and Galo Rojo. Cornell University</a></li>
</ul>
