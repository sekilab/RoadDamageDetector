# RoadDamageDetector
This page introduces the road damage dataset we created.
intro wo kaku

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
- How to use trained models.

Please check [RoadDamageDatasetTutorial.ipynb](https://github.com/sekilab/RoadDamageDetector/blob/master/RoadDamageDatasetTutorial.ipynb).

## Privacy matters
eigo no check ga owattara kaku

## License
Images on this dataset are available under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0). The license and link to the legal document can be found next to every image on the service in the image information panel and contains the CC BY-SA 4.0 mark:
<br><a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.en"><img alt="Creative Commons License" style="border-width:0" src="https://licensebuttons.net/l/by-sa/4.0/88x31.png" /></a><br />


## Citation
If you use or find out our dataset useful, please cite our paper:


If you have something to ask us about the dataset, please contact :
`maedahi[at]iis.u-tokyo.ac.jp`
