# RoadDamageDetector
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

## Download Road Damage Dataset
Please pay attention to the disk capacity when downloading.
- [trainedModels (70MB)](https://s3-ap-northeast-1.amazonaws.com/mycityreport/trainedModels.tar.gz)
- [RoadDamageDataset (1.7GB)](https://s3-ap-northeast-1.amazonaws.com/mycityreport/RoadDamageDataset.tar.gz)

## Dataset Tutorial
We also created the tutorial of Road Damage Dataset.
In this tutorial, we will show you:
- How to download Road Crack Dataset
- The structure of the Dataset
- The statistical information of the dataset
- How to evaluate your result

## Privacy matters
eigo no check ga owattara kaku

## License
cc by 4

## Citation
If you use or find out our dataset useful, please cite our paper:


If you have something to ask us about the dataset, please contact :
`maedahi[at]iis.u-tokyo.ac.jp`
