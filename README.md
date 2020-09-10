# RoadDamageDetector

********

# News
[2020-09-10]: Test2 dataset for Global Road Damage Detection Challenge 2020 has been released!

[2020-09-02]: The citation information and the article explaining the latest India-Japan-Czech (InJaCz) Road Damage Dataset, being used for [IEEE BigData Cup Challenge 2020](http://bigdataieee.org/BigData2020/), is now [available](https://arxiv.org/abs/2008.13101).

[2020-4-25]: [Global Road Damage Detection Challenge 2020](https://rdd2020.sekilab.global/) will be held as one of the [IEEE Bigdata Cup](http://bigdataieee.org/BigData2020/). How about joining the data cup now? Exciting prizes await you!

[2019-10-16]: Road Damage Dataset was awarded by the GIS Association of Japan. For more information, please check [here](http://www.gisa-japan.org/awards/recipients.html).

[2018-12-10]: Road damage detection and classification challenge (one of the IEEE Bigdata Cup Challenge) was held in Seattle. 59 teams participated from 14 countries. For more information, please check [here](https://bdc2018.mycityreport.net/)!

********

# Dataset for [Global Road Damage Detection Challenge 2020](https://rdd2020.sekilab.global/) 

- [train.tar.gz](https://mycityreport.s3-ap-northeast-1.amazonaws.com/02_RoadDamageDataset/public_data/IEEE_bigdata_RDD2020/train.tar.gz)
  - `train.tar.gz` contains Japan/India/Czech images and annotations. The format of annotations is the same as pascalVOC.

- [test1.tar.gz](https://mycityreport.s3-ap-northeast-1.amazonaws.com/02_RoadDamageDataset/public_data/IEEE_bigdata_RDD2020/test1.tar.gz)

- [sampleSubmission.txt](https://mycityreport.s3-ap-northeast-1.amazonaws.com/02_RoadDamageDataset/public_data/IEEE_bigdata_RDD2020/sampleSubmission.txt)

- [test2.tar.gz](https://mycityreport.s3-ap-northeast-1.amazonaws.com/02_RoadDamageDataset/public_data/IEEE_bigdata_RDD2020/test2.tar.gz)

## Citation
The data collection methodology, study area and other information for the India-Japan-Czech dataset are provided in our research paper entitled [Transfer Learning-based Road Damage Detection for Multiple Countries](https://arxiv.org/abs/2008.13101). 

If you use or find our dataset and/or article useful, please cite.

@misc{arya2020transfer,
    title={Transfer Learning-based Road Damage Detection for Multiple Countries},
    author={Deeksha Arya and Hiroya Maeda and Sanjay Kumar Ghosh and Durga Toshniwal and Alexander Mraz and Takehiro Kashiyama and Yoshihide Sekimoto},
    year={2020},
    eprint={2008.13101},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}

## Damage Categories to be considered
{D00: Longitudinal Crack, D10: Transverse Crack, D20: Aligator Crack, D40: Pothole}

********

# Road Damage Dataset 2019

## Citation

If you use or find out our dataset useful, please cite [our paper](https://doi.org/10.1111/mice.12561) in the journal of [Computer-Aided Civil and Infrastructure Engineering](https://onlinelibrary.wiley.com/journal/14678667):

Maeda, H., Kashiyama, T., Sekimoto, Y., Seto, T., & Omata, H. Generative adversarial network for road damage detection. Computer‐Aided Civil and Infrastructure Engineering.


@article{maedagenerative,
  title={Generative adversarial network for road damage detection},
  author={Maeda, Hiroya and Kashiyama, Takehiro and Sekimoto, Yoshihide and Seto, Toshikazu and Omata, Hiroshi},
  journal={Computer-Aided Civil and Infrastructure Engineering},
  publisher={Wiley Online Library}
}


## Abstract
Machine learning can produce promising results when sufficient training data are available; however, infrastructure inspections typically do not provide sufficient training data for road damage. Given the differences in the environment, the type of road damage and the degree of its progress can vary from structure to structure. The use of generative models, such as a generative adversarial network (GAN) or a variational autoencoder, makes it possible to generate a pseudoimage that cannot be distinguished from a real one. Combining a progressive growing GAN along with Poisson blending artificially generates road damage images that can be used as new training data to improve the accuracy of road damage detection. The addition of a synthesized road damage image to the training data improves the F‐measure by 5% and 2% when the number of original images is small and relatively large, respectively. All of the results and the new Road Damage Dataset 2019 are publicly available. 


## The structure of Road Damage Dataset 
The structure of the Road Damage Dataset 2019 is the same as the previous one: Pascal VOC.
 
## Download Road Damage Dataset
Please pay attention to the disk capacity when downloading.
- trainedModels
  - [Resnet(128MB)](https://mycityreport.s3-ap-northeast-1.amazonaws.com/02_RoadDamageDataset/public_data/Japan/CACAIE2020/frozen_inference_graph_resnet.pb)
  - [Mobilenet(18MB)](https://mycityreport.s3-ap-northeast-1.amazonaws.com/02_RoadDamageDataset/public_data/Japan/CACAIE2020/frozen_inference_graph_mobilenet.pb)

- [RoadDamageDataset_2019 (2.4GB)](https://mycityreport.s3-ap-northeast-1.amazonaws.com/02_RoadDamageDataset/public_data/Japan/RDD2020_data.tar.gz)

********

# Road Damage Dataset 2018

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

## Download Road Damage Dataset
Please pay attention to the disk capacity when downloading.
- [trainedModels (70MB)](https://mycityreport.s3-ap-northeast-1.amazonaws.com/02_RoadDamageDataset/public_data/Japan/CACAIE2018/trainedModels.tar.gz)

- [RoadDamageDataset_v1 (1.7GB)](https://mycityreport.s3-ap-northeast-1.amazonaws.com/02_RoadDamageDataset/public_data/Japan/CACAIE2018/RoadDamageDataset.tar.gz)

## Dataset Tutorial
We also created the tutorial of Road Damage Dataset.
In this tutorial, we will show you:
- How to download Road Crack Dataset
- The structure of the Dataset
- The statistical information of the dataset
- How to use trained models.

Please check [RoadDamageDatasetTutorial.ipynb](https://github.com/sekilab/RoadDamageDetector/blob/master/RoadDamageDatasetTutorial.ipynb).

********

# Privacy matters
Our dataset is openly accessible by the public. Therefore, considering issues with privacy, based on visual inspection, when a person's face or a car license plate are clearly reflected in the image, they are blurred out.

# License
Images on this dataset are available under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0). The license and link to the legal document can be found next to every image on the service in the image information panel and contains the CC BY-SA 4.0 mark:
<br><a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.en"><img alt="Creative Commons License" style="border-width:0" src="https://licensebuttons.net/l/by-sa/4.0/88x31.png" /></a><br />

