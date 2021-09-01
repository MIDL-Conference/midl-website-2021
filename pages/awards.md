---
title: "Awards"
---

{% from "_macros.html" import paper, button, youtube %}

# Awards

{{ youtube('JF_jOA2JqiM') }}

## Best Paper Award

The **MIDL 2021 best paper award** recognizes the highest quality full-length paper presented at the conference. The focus lies on novel methodological concepts with great potential of medical impact. All long papers that are presented as long papers at MIDL 2021 were eligible. The award was decided by an independent committee that had no conflicts of interest.

### Best Paper Award - Winner
[% .papers %]

{{ paper('Beyond pixel-wise supervision: semantic segmentation with higher-order shape descriptors',
        'Hoel Kervadec, Houda Bahig, Laurent Letourneau-Guillon, Jose Dolz, Ismail Ben Ayed',
        openreview='https://openreview.net/forum?id=nqe6e0oJ_fL',
        pdf='/proceedings/kervadec21.pdf',
        id='A3',
        paper='papers/A3.html',
        proceedings='https://proceedings.mlr.press/v143/kervadec21a.html',
        video='https://www.youtube.com/watch?v=ApKsoowlEGQ',
        abstract="Standard losses for training deep segmentation networks could be seen as individual classifications of pixels, instead of supervising the global shape of the predicted segmentations. While effective, they require exact knowledge of the label of each pixel in an image. This study investigates how effective global geometric shape descriptors could be, when used on their own as segmentation losses for training deep networks. Not only interesting theoretically, there exist deeper motivations to posing segmentation problems as a reconstruction of shape descriptors: First, annotations to obtain approximations of low-order shape moments could be much less cumbersome than their full-mask counterparts, and anatomical priors could be readily encoded into invariant shape descriptions, which might alleviate the annotation burden. Also, some shape descriptors could be readily used to encode\\'\\' biomarkers, leading to better interpretability. Finally, and most importantly, we hypothesize that, given a task, certain shape descriptions might be invariant across image acquisition protocols/modalities and subject populations, which might open interesting research avenues for generalization in medical image segmentation.We introduce and formulate a few shape descriptors in the context of deep segmentation, and evaluate their potential as stand-alone losses on two different, challenging tasks. Inspired by recent works in constrained optimization for deep networks, we propose a way to use those descriptors to supervise segmentation, without any pixel-level label. Very surprisingly, as little as 4 descriptors values per class can approach the performance of a segmentation mask with 65k individual discrete labels. We also found that shape descriptors can be a valid way to encode anatomical priors about the task, enabling to leverage expert knowledge without requiring additional annotations. Our implementation is publicly available and can be easily extended.")
}}
[% / %]

### Best Paper Award - Runner-up
[% .papers %]

{{ paper('Semantic similarity metrics for learned image registration',
        'Steffen Czolbe, Oswin Krause, Aasa Feragen',
        openreview='https://openreview.net/forum?id=9M5cH--UdcC',
        pdf='/proceedings/czolbe21.pdf',
        id='D2',
        paper='papers/D2.html',
        proceedings='https://proceedings.mlr.press/v143/czolbe21a.html',
        video='https://www.youtube.com/watch?v=qHADp8I2iR4',
        abstract='We propose a semantic similarity metric for image registration. Existing metrics like euclidean distance or normalized cross-correlation focus on aligning intensity values, giving difficulties with low intensity contrast or noise. Our approach learns dataset-specific features that drive the optimization of a learning-based registration model. We train both an unsupervised approach using an auto-encoder, and a semi-supervised approach using supplemental segmentation data to extract semantic features for image registration. Comparing to existing methods across multiple image modalities and applications, we achieve consistently high registration accuracy. A learned invariance to noise gives smoother transformations on low-quality images.')
}}
[% / %]

### Best Paper Award - Other finalists
[% .papers %]

{{ paper('Embedding-based Instance Segmentation in Microscopy',
        'Manan Lalit, Pavel Tomancak, Florian Jug',
        openreview='https://openreview.net/forum?id=JM6GuFGayL5',
        pdf='/proceedings/lalit21.pdf',
        id='A2',
        paper='papers/A2.html',
        proceedings='https://proceedings.mlr.press/v143/lalit21a.html',
        video='https://www.youtube.com/watch?v=trETG5zf3PI',
        abstract='Automatic detection and segmentation of objects in 2D and 3D microscopy data is important for countless biomedical applications.In the natural image domain, spatial embedding-based instance segmentation methods are known to yield high-quality results, but their utility for segmenting microscopy data is currently little researched. Here we introduce EmbedSeg, an embedding-based instance segmentation method which outperforms existing state-of-the-art baselines on 2D as well as 3D microscopy datasets.Additionally, we show that EmbedSeg has a GPU memory footprint small enough to train even on laptop GPUs, making it accessible to virtually everyone. Finally, we introduce four new 3D microscopy datasets, which we make publicly available alongside ground truth training labels. Our open-source implementation is available at https://github.com/juglab/EmbedSeg.')
}}

{{ paper('Unsupervised Brain Anomaly Detection and Segmentation with Transformers',
        'Walter Hugo Lopez Pinaya, Petru-Daniel Tudosiu, Robert Gray, Geraint Rees, Parashkev Nachev, Sébastien Ourselin, M. Jorge Cardoso',
        openreview='https://openreview.net/forum?id=Z1tlNqbCpp_',
        pdf='/proceedings/pinaya21.pdf',
        id='E3',
        paper='papers/E3.html',
        proceedings='https://proceedings.mlr.press/v143/pinaya21a.html',
        video='https://www.youtube.com/watch?v=cSGtcb8nu9w',
        abstract='Pathological brain appearances may be so heterogeneous as to be intelligible only as anomalies, defined by their deviation from normality rather than any specific pathological characteristic. Amongst the hardest tasks in medical imaging, detecting such anomalies requires models of the normal brain that combine compactness with the expressivity of the complex, long-range interactions that characterise its structural organisation. These are requirements transformers have arguably greater potential to satisfy than other current candidate architectures, but their application has been inhibited by their demands on data and computational resource. Here we combine the latent representation of vector quantised variational autoencoders with an ensemble of autoregressive transformers to enable unsupervised anomaly detection and segmentation defined by deviation from healthy brain imaging data, achievable at low computational cost, within relative modest data regimes. We compare our method to current state-of-the-art approaches across a series of experiments involving synthetic and real pathological lesions. On real lesions, we train our models on 15,000 radiologically normal participants from UK Biobank, and evaluate performance on four different brain MR datasets with small vessel disease, demyelinating lesions, and tumours. We demonstrate superior anomaly detection performance both image-wise and pixel-wise, achievable without post-processing. These results draw attention to the potential of transformers in this most challenging of imaging tasks.')
}}

{{ paper('Gifsplanation via Latent Shift: A Simple Autoencoder Approach to Counterfactual Generation for Chest X-rays',
        'Joseph Paul Cohen, Rupert Brooks, Sovann En, Evan Zucker, Anuj Pareek, Matthew P. Lungren, Akshay Chaudhari',
        openreview='https://openreview.net/forum?id=rnunjvgxAMt',
        pdf='/proceedings/cohen21.pdf',
        id='I2',
        paper='papers/I2.html',
        proceedings='https://proceedings.mlr.press/v143/cohen21a.html',
        video='https://www.youtube.com/watch?v=s0L5f7ibiLI',
        abstract='Motivation: Traditional image attribution methods struggle to satisfactorily explain predictions of neural networks. Prediction explanation is important, especially in medical imaging, for avoiding the unintended consequences of deploying AI systems when false positive predictions can impact patient care. Thus, there is a pressing need to develop improved models for model explainability and introspection. Specific problem: A new approach is to transform input images to increase or decrease features which cause the prediction. However, current approaches are difficult to implement as they are monolithic or rely on GANs. These hurdles prevent wide adoption.Our approach: Given an arbitrary classifier, we propose a simple autoencoder and gradient update (Latent Shift) that can transform the latent representation of a specific input image to exaggerate or curtail the features used for prediction. We use this method to study chest X-ray classifiers and evaluate their performance. We conduct a reader study with two radiologists assessing 240 chest X-ray predictions to identify which ones are false positives (half are) using traditional attribution maps or our proposed method.Results: We found low overlap with ground truth pathology masks for models with reasonably high accuracy. However, the results from our reader study indicate that these models are generally looking at the correct features.We also found that the Latent Shift explanation allows a user to have more confidence in true positive predictions compared to traditional approaches (0.15±0.95 in a 5 point scale with p=0.01) with only a small increase in false positive predictions (0.04±1.06 with p=0.57).Accompanying webpage: https://mlmed.org/gifsplanation/Source code: https://github.com/mlmed/gifsplanation')
}}
[% / %]

---

## Reviewers Awards

Selection of reviewer awards were based on Area Chairs who scored the quality of reviews.

### Outstanding reviewers
* Christian F. Baumgartner
* Christian Desrosiers
* Monika Grewal
* Jannis Hagenah
* Alessa Hering
* Raghav Mehta
* Hans Meine
* Nick Pawlowski
* Antoine Théberge

### Honorable mention
* Vincent Andrearczyk
* Elsa Angelini
* Felix John Bragman
* Francesco Caliva
* Diedre Carmo
* Francesco Ciompi
* Nicha C. Dvornek
* Adrian Galdran
* Melanie Ganz
* Pedro M. Gordaliza
* Hoel Kervadec
* Hugo Kuijf
* Amirreza Mahbod
* Saypraseuth Mounsaveng
* Anirban Mukhopadhyay
* Sriprabha Ramanarayanan
* Mitko Veta

---

## Audience Awards

In addition to the best paper award there were two audience awards for best long oral and best short oral presentation. 

### Audience Award - Best long oral presentation - Winner
[% .papers %]

{{ paper('Understanding and Visualizing Generalization UNets',
        'Abhejit Rajagopal, Vamshi Chowdary Madala, Thomas A Hope, Peder Larson',
        openreview='https://openreview.net/forum?id=V-a5DJCh4Hk',
        pdf='/proceedings/rajagopal21.pdf',
        id='I3',
        paper='papers/I3.html',
        proceedings='https://proceedings.mlr.press/v143/rajagopal21a.html',
        video='https://www.youtube.com/watch?v=jJn0oMAAg0o',
        abstract="Fully-convolutional neural networks, such as the 2D or 3D UNet, are now pervasive in medical imaging for semantic segmentation, classification, image denoising, domain translation, and reconstruction. However, evaluation of UNet performance, as with most CNNs, has mostly been relegated to evaluation of a few performance metrics (e.g. accuracy, IoU, SSIM, etc.) using the network\\'s final predictions, which provides little insight into important issues such as dataset shift that occur in clinical application. In this paper, we propose techniques for understanding and visualizing the generalization performance of UNets in image classification and regression tasks, giving rise to metrics that are indicative of performance on a withheld test-set without the need for groundtruth annotations.")
}}
[% / %]

### Audience Award - Best long oral presentation - Runner-up
[% .papers %]

{{ paper('Whole-Body Soft-Tissue Lesion Tracking and Segmentation in Longitudinal CT Imaging Studies',
        'Alessa Hering, Felix Peisen, Teresa Amaral, Sergios Gatidis, Thomas Eigentler, Ahmed Othman, Jan Hendrik Moltz',
        openreview='https://openreview.net/forum?id=hzbuHGhU02Z',
        pdf='/proceedings/hering21.pdf',
        id='A1',
        paper='papers/A1.html',
        proceedings='https://proceedings.mlr.press/v143/hering21a.html',
        video='https://www.youtube.com/watch?v=7E6UA7B49so',
        abstract='In follow-up CT examinations of cancer patients, therapy success is evaluated by estimating the change in tumor size. This process is time-consuming and error-prone. We present a pipeline that automates the segmentation and measurement of matching lesions, given a point annotation in the baseline lesion. First, a region around the point annotation is extracted, in which a deep-learning-based segmentation of the lesion is performed. Afterward, a registration algorithm finds the corresponding image region in the follow-up scan and the convolutional neural network segments lesions inside this region. In the final step, the corresponding lesion is selected. We evaluate our pipeline on clinical follow-up data comprising 125 soft-tissue lesions from 43 patients with metastatic melanoma. Our pipeline succeeded for 96% of the baseline and 80% of the follow-up lesions, showing that we have laid the foundation for an efficient quantitative follow-up assessment in clinical routine.')
}}
[% / %]

### Audience Award - Best short oral presentations
[% .papers %]

{{ paper('Common limitations of performance metrics in biomedical image analysis',
        'Annika Reinke, Matthias Eisenmann, Minu Dietlinde Tizabi, Carole H. Sudre, Tim Rädsch, Michela Antonelli, Tal Arbel, Spyridon Bakas, M. Jorge Cardoso, Veronika Cheplygina, Keyvan Farahani, Ben Glocker, Doreen Heckmann-Nötzel, Fabian Isensee, Pierre Jannin, Charles Kahn, Jens Kleesiek, Tahsin Kurc, Michal Kozubek, Bennett A. Landman, Geert Litjens, Klaus Maier-Hein, Anne Lousise Martel, bjoern menze, Henning Müller, Jens Petersen, Mauricio Reyes, Nicola Rieke, Bram Stieltjes, Ronald M. Summers, Sotirios A. Tsaftaris, Bram van Ginneken, Annette Kopp-Schneider, Paul Jäger, Lena Maier-Hein',
        openreview='https://openreview.net/forum?id=76X9Mthzv4X',
        pdf='https://openreview.net/pdf?id=76X9Mthzv4X',
        id='A4',
        paper='papers/A4.html',
        proceedings='',
        video='https://www.youtube.com/watch?v=toehYwAvu6A',
        abstract="While the importance of automatic biomedical image analysis is increasing at an enormous pace, recent meta-research revealed major flaws with respect to algorithm validation. Performance metrics are key for objective, transparent and comparative performance assessment, but little attention has been given to their pitfalls. Under the umbrella of the Helmholtz Imaging Platform (HIP), three international initiatives - the MICCAI Society\\'s challenge working group, the Biomedical Image Analysis Challenges (BIAS) initiative, as well as the benchmarking working group of the MONAI framework - have now joined forces with the mission to generate best practice recommendations with respect to metrics in medical image analysis. Consensus building is achieved via a Delphi process, a popular tool for integrating opinions in large international consortia. The current document serves as a teaser for the results presentation and focuses on the pitfalls of the most commonly used metric in biomedical image analysis, the Dice Similarity Coefficient (DSC), in the categories of (1) mathematical properties/edge cases, (2) task/metric fit and (3) metric aggregation. Being compiled by a large group of experts from more than 30 institutes worldwide, we believe that our framework could be of general interest to the MIDL community and will improve the quality of biomedical image analysis algorithm validation.")
}}

{{ paper('Rethinking the Design of Learning based Inter-Patient Registration using Deformable Supervoxels ',
        'Mattias P Heinrich',
        openreview='https://openreview.net/forum?id=zZA5TpNdC4Z',
        pdf='https://openreview.net/pdf?id=zZA5TpNdC4Z',
        id='E4',
        paper='papers/E4.html',
        proceedings='',
        video='https://www.youtube.com/watch?v=Uhe3uB9NhBQ',
        abstract='Deep learning has the potential to substantially improve inter-subject alignment for shape and atlas analysis. So far most highly accurate supervised approaches require dense manual annotations and complex multi-level architectures but may still be susceptible to label bias. We present a radically different approach for learning to estimate large deformations without expert supervision. Instead of regressing displacements, we train a 3D DeepLab network to predict automatic supervoxel segmentations. To enable consistent supervoxel labels, we use the warping field of a conventional approach and increase the accuracy by sampling multiple complementary over-segmentations. We experimentally demonstrate that 1) our deformable supervoxels are less sensitive to large initial misalignment and can combine linear and nonlinear registration and 2) using this self-supervised classification loss is more robust to noisy ground truth and leads to better convergence than direct regression as supervision.')
}}

{{ paper('Discrete Pseudohealthy Synthesis: Aortic Root Shape Typification and Type Classification with Pathological Prior',
        'Jannis Hagenah, Floris Ernst',
        openreview='https://openreview.net/forum?id=Fqmbjvawgt',
        pdf='/proceedings/hagenah21.pdf',
        id='J5',
        paper='papers/J5.html',
        proceedings='https://proceedings.mlr.press/v143/hagenah21a.html',
        video='https://www.youtube.com/watch?v=7Rfa6bKQSHo',
        abstract="In personalized prosthesis shaping, the desired shape remains typically unknown and has to be estimated based on the individual pathological shape. This estimation is also called pseudo healthy synthesis. One example application is the personalization of aortic root prostheses during valve-sparing aortic root surgery. Even though several methods for pseudohealthy synthesis were proposed during the last years, it might not always be necessary to taylor a completely individual and unique prosthesis for each and every patient as this introduces high costs and regulatory issues. Another option is to identify a set of prosthesis types that represents all natural healthy shapes in an adequate way. Then, the pseudohealthy synthesis problem becomes a classification problem, aiming on predicting the optimal prosthesis out of the set of candidates given a pathological shape.In this work, we present a fully automized workflow of unsupervised shape typification and type classification based on pathological data for the example of personalizing aortic root prostheses shapes. We provide a proof-of-concept study on an ex-vivo porcine data set, including a thorough evaluation of the model\\'s hyperparameters and the number of identified shape types. Our study lies the groundwork for a new branch of personalized prosthesis shaping with a high potential of translation to clinical application: Discrete Pseudohealthy Synthesis.")
}}
[% / %]


