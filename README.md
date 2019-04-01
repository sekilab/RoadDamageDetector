# RoadDamageDetector

## News
[2018-12-10]: Road damage detection and classification challenge (one of the IEEE Bigdata Cup Challenge) was held in Seattle. 59 teams participated from 14 countries. For more information, please check [here](https://bdc2018.mycityreport.net/)!

[2018-12-??]: RoadDamageDataset_v2 (1.7GB) is available now! We re-labeled all the RoadDamageDataset_v1 (1.7GB) in order to improve the accuracy of annotation. 

## Citation

If you use or find out our dataset useful, please cite [our paper](https://doi.org/10.1111/mice.12387) in the journal of [Computer-Aided Civil and Infrastructure Engineering](https://onlinelibrary.wiley.com/journal/14678667):

Maeda, H., Sekimoto, Y., Seto, T., Kashiyama, T., & Omata, H. 
Road Damage Detection and Classification Using Deep Neural Networks with Smartphone Images. 
Computer‐Aided Civil and Infrastructure Engineering.

@article{maedaroad, title={Road Damage Detection and Classification Using Deep Neural Networks with Smartphone Images}, 
author={Maeda, Hiroya and Sekimoto, Yoshihide and Seto, Toshikazu and Kashiyama, Takehiro and Omata, Hiroshi}, 
journal={Computer-Aided Civil and Infrastructure Engineering}, publisher={Wiley Online Library} }


arXiv version is [here](https://arxiv.org/abs/1801.09454).


## Abstract

Research on damage detection of road surfaces using image processing techniques has been actively conducted achieving considerably high detection accuracies.
However, many studies only focus on the detection of the presence or absence of damage. However, in a real-world scenario, when the road managers from a governing body needs to repair such damage, they need to know the type of damage clearly to take effective action. In addition, in many of these previous studies, the researchers acquire their own data using different methods. Hence, there is no uniform road damage dataset available openly, leading to the absence of a benchmark for road damage detection.
This study makes three contributions to address these issues.
First, to the best of our knowledge, for the first time, a large-scale road damage dataset is prepared. This dataset is composed of 9,053 road damage images captured with a smartphone installed on a car, with 15,435 instances of road surface damage included in these road images. These images are captured in a wide variety of weather and illuminance conditions. In each image, the bounding box representing the location of the damage and the type of damage are annotated.
Next, we use the state-of-the-art object detection method using convolutional neural networks to train the damage detection model with our dataset, and compare the accuracy and runtime speed on both, a GPU server and a smartphone. Finally, we show that the type of damage can be classified into eight types with high accuracy by applying the proposed object detection method.
The road damage dataset, our experimental results, and the developed smartphone application used in this study are made publicly available.
This page introduces the road damage dataset we created.


# Road Damage Dataset
## The structure of Road Damage Dataset
Road Damage Dataset contains trained models and Annotated images.
Annotated images are presented as the same format to [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/).
- trainedModels
    - SSD Inception V2
    - SSD MobileNet
- RoadDamageDataset (dataset structure is the same format as PASCAL VOC)
    - Adachi
        - JPEGImages : contains images
        - Annotations : contains xml files of annotation
        - ImageSets : contains text files that show training or evaluation image list
    - Chiba
    - Muroran
    - Ichihara
    - Sumida
    - Nagakute
    - Numazu


## Download Road Damage Dataset Ver. 1
Please pay attention to the disk capacity when downloading.
- [trainedModels (70MB)](https://s3-ap-northeast-1.amazonaws.com/mycityreport/trainedModels.tar.gz)

- [RoadDamageDataset_v1 (1.7GB)](https://s3-ap-northeast-1.amazonaws.com/mycityreport/RoadDamageDataset.tar.gz)

## Download Road Damage Dataset Ver. 2

- [RoadDamageDataset_v2 (1.7GB)](https://s3-ap-northeast-1.amazonaws.com/mycityreport/RoadDamageDataset_v2.tar.gz)

### What's new in RoadDamageDataset_v2?
The definition of the label was changed.
- D01 was merged into D00.
- D01 and D11 were abolished.
- D50(Manhole and Handhole) was added.

## Dataset Tutorial
We also created the tutorial of Road Damage Dataset.
In this tutorial, we will show you:
- How to download Road Crack Dataset
- The structure of the Dataset
- The statistical information of the dataset
- How to use trained models.

Please check [RoadDamageDatasetTutorial.ipynb](https://github.com/sekilab/RoadDamageDetector/blob/master/RoadDamageDatasetTutorial.ipynb).

## Smartphone Apps
We also make our smartphone apps publicly available.
Please check [here](https://github.com/sekilab/RoadDamageDetector/blob/master/smartphoneAPPS.md).

## Privacy matters
Our dataset is openly accessible by the public. Therefore, considering issues with privacy, based on visual inspection, when a person's face or a car license plate are clearly reflected in the image, they are blurred out.


## License
Images on this dataset are available under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0). The license and link to the legal document can be found next to every image on the service in the image information panel and contains the CC BY-SA 4.0 mark:
<br><a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.en"><img alt="Creative Commons License" style="border-width:0" src="https://licensebuttons.net/l/by-sa/4.0/88x31.png" /></a><br />


If you have something to ask us about the dataset, please contact :
`maedahi[at]iis.u-tokyo.ac.jp`
