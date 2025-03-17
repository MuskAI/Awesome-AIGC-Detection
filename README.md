# Awesome-AIGC-Detection [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  
![](asset.jpg)

This repo is created based on [This](https://github.com/RFAI2025/Awesome-AIGC-Image-Detection/tree/main)

Photographs are a means for people to document their daily experiences and are often seen as reliable sources of information. However, there is increasing concern that advancements in artificial intelligence (AI) technology could lead to the creation of fake images, potentially causing confusion and eroding trust in the authenticity of photos. The rapid advancement of AI-Generated Content (AIGC) has greatly impacted our daily lives, making the detection of such content a critical challenge for AI safety today. This is a collection list of research on AIGC image detection, intended to support progress in related areas.  

## Contents
- [Datasets](#Datasets)
- [Papers](#Papers)
- [Tools](#Tools)
- [Others](#Others)

## Datasets
|  Year   | Dataset  |  Number of Real  |  Number of Fake  |  Source of Real Image  |  Generation Method of Fake Image  |
|  ----  | ----  |  ----  | ----  |  ----  | ----  |
| 2020  | [CNNSpot](https://peterwang512.github.io/CNNDetection/) | 362,000  |  362,000 | LSUN, ImageNet, CelebA, COCO... | ProGAN, StyleGAN, BigGAN, CRN, SITD... |
| 2023  | [GenImage](https://genimage-dataset.github.io/) | 1,331,167  |  1,350,000 | ImagNet | SDMs, Midjourney, BigGAN |
| 2023  | [Fake2M](https://github.com/Inf-imagine/Sentry) | -  |  2,300,000 | CC3M | SD-V1.5, IF, StyleGAN3 |
| 2023  | [DMimage](https://github.com/grip-unina/DMimageDetection) | 200,000  |  200,000 | COOC, LSUN | LDM |
| 2023  | [DiffusionDB](https://github.com/poloclub/diffusiondb) | 3,300,000  |  16,000,000 | DiscordChatExporter | SD |
| 2024  | WildFake | 2,557,278  | 1,013,446 | ImagNet, Laion, Wukong, COO...  | BigGAN, StyleGAN, StarGAN, Midjourney, DALLE... |

## Papers
<details open>
  <summary>2025</summary>

  - [**KDD '25**] Improving Synthetic Image Detection Towards Generalization: An Image Transformation Perspective [[Paper](https://arxiv.org/pdf/2408.06741)][[Code](https://github.com/Ouxiang-Li/SAFE)]
  - [**arxiv**] TextureCrop: Enhancing Synthetic Image Detection through Texture-based Cropping [[Paper](https://arxiv.org/pdf/2407.15500)]
</details>

<details open>
  <summary>2024</summary>
  
  - [**CVPR '24**] FakeInversion: Learning to Detect Images from Unseen Text-to-Image Models by Inverting Stable Diffusion [[Paper](https://arxiv.org/pdf/2406.08603)][[Code](https://fake-inversion.github.io/)]
  - [**CVPR '24**] Forgery-aware Adaptive Transformer for Generalizable Synthetic [[Paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Forgery-aware_Adaptive_Transformer_for_Generalizable_Synthetic_Image_Detection_CVPR_2024_paper.pdf)][[Code](https://github.com/Michel-liu/FatFormer?tab=readme-ov-file)]
  - [**CVPR '24**] Rethinking the Up-Sampling Operations in CNN-based Generative Network for Generalizable Deepfake Detection [[Paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Tan_Rethinking_the_Up-Sampling_Operations_in_CNN-based_Generative_Network_for_Generalizable_CVPR_2024_paper.pdf)][[Code](https://github.com/chuangchuangtan/NPR-DeepfakeDetection)]
  - [**CVPR '24**] LaRE<sup>2</sup>: Latent Reconstruction Error Based Method for Diffusion-Generated Image Detection [[Paper](https://arxiv.org/pdf/2403.17465)][[Code](https://github.com/luo3300612/LaRE)]
  - [**CVPR '24**] AEROBLADE: Training-Free Detection of Latent Diffusion Images Using Autoencoder Reconstruction Error [[Paper](https://arxiv.org/pdf/2401.17879)][[Code](https://github.com/jonasricker/aeroblade)]
  - [**ECCV '24**] Zero-Shot Detection of AI-Generated Images [[Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02665.pdf)][[Code](https://github.com/grip-unina/ZED/)]
  - [**ECCV '24**] Leveraging Representations from Intermediate Encoder-blocks for Synthetic Image Detection [[Paper](https://arxiv.org/pdf/2402.19091)][[Code](https://github.com/mever-team/rine/tree/main?tab=readme-ov-file)]
  - [**ECCV '24**] Contrasting Deepfakes Diffusion via Contrastive Learning and Global-Local Similarities [[Paper](https://arxiv.org/pdf/2407.20337)][[Code](https://github.com/aimagelab/CoDE)]
  - [**ICML '24**] DRCT: Diffusion Reconstruction Contrastive Training towards Universal Detection of Diffusion Generated Images [[Paper](https://openreview.net/pdf?id=oRLwyayrh1)][[Code](https://github.com/beibuwandeluori/DRCT)]
  - [**ICML '24**] Exposing the Fake: Effective Diffusion-Generated Images Detection [[Paper](https://arxiv.org/pdf/2307.06272)]
  - [**ICML '24**] How to Trace Latent Generative Model Generated Images without Artificial Watermark? [[Paper](https://arxiv.org/pdf/2405.13360)][[Code](https://github.com/ZhentingWang/LatentTracer)]
  - [**ICMR '24**] CLIPping the Deception: Adapting Vision-Language Models for Universal Deepfake Detection [[Paper](https://dl.acm.org/doi/pdf/10.1145/3652583.3658035?__cf_chl_tk=52uMrPHjHFZ_5l.v3gqWEAAZLY7rDpWSndFDcA4MsQ8-1739784272-1.0.1.1-9QaZoAk9FhSYgOCA67OOS7E44PzqmrDa0Bdu6dzlPFY)][[Code](https://github.com/sfimediafutures/CLIPping-the-Deception)]
  - [**CVPRW '24**] Raising the Bar of AI-generated Image Detection with CLIP [[Paper](https://openaccess.thecvf.com/content/CVPR2024W/WMF/papers/Cozzolino_Raising_the_Bar_of_AI-generated_Image_Detection_with_CLIP_CVPRW_2024_paper.pdf)][[Code](https://github.com/grip-unina/ClipBased-SyntheticImageDetection/)]
  - [**CVPRW '24**] Faster Than Lies: Real-time Deepfake Detection using Binary Neural Networks [[Paper](https://openaccess.thecvf.com/content/CVPR2024W/DFAD/papers/Lanzino_Faster_Than_Lies_Real-time_Deepfake_Detection_using_Binary_Neural_Networks_CVPRW_2024_paper.pdf)]
  - [**arxiv**] Mixture of Low-rank Experts for Transferable AI-Generated Image Detection [[Paper](https://arxiv.org/pdf/2404.04883)][[Code](https://github.com/zhliuworks/CLIPMoLE)]
  - [**arxiv**] Guided and Fused: Efficient Frozen CLIP-ViT with Feature Guidance and Multi-Stage Feature Fusion for Generalizable Deepfake Detection [[Paper](https://arxiv.org/pdf/2408.13697)]
  - [**arxiv**] A Single Simple Patch is All You Need for AI-generated Image Detection [[Paper](https://arxiv.org/pdf/2402.01123)][[Code](https://github.com/bcmi/SSP-AI-Generated-Image-Detection)]
  - [**arxiv**] RIGID: A Training-Free and Model-Agnostic Framework for Robust AI-Generated Image Detection [[Paper](https://arxiv.org/pdf/2405.20112)]
  - [**arxiv**] Improving Interpretability and Robustness for the Detection of AI-Generated Images [[Paper](https://arxiv.org/pdf/2406.15035)]
  - [**arxiv**] Continuous fake media detection: adapting deepfake detectors to new generative techniques [[Paper](https://arxiv.org/pdf/2406.08171)]
  - [**arxiv**] Organic or Diffused: Can We Distinguish Human Art from AI-generated Images? [[Paper](https://arxiv.org/pdf/2402.03214)]
  - [**arxiv**] Let Real Images be as a Judger, Spotting Fake Images Synthesized with Generative Models [[Paper](https://arxiv.org/pdf/2403.16513)]
  - [**arxiv**] D<sup>3</sup> Scaling Up Deepfake Detection by Learning [[Paper](https://arxiv.org/pdf/2404.04584)]
  - [**arxiv**] Bi-LORA: A Vision-Language Approach for Synthetic Image Detection from Discrepancy [[Paper](https://arxiv.org/pdf/2404.01959)]
  - [**arxiv**] Detecting Image Attribution for Text-to-Image Diffusion Models in RGB and Beyond [[Paper](https://arxiv.org/pdf/2403.19653)][[Code](https://github.com/k8xu/ImageAttribution)]
</details>

<details open>
  <summary>2023</summary>

  - [**CVPR '23**] Towards Universal Fake Image Detectors that Generalize Across Generative Models [[Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Ojha_Towards_Universal_Fake_Image_Detectors_That_Generalize_Across_Generative_Models_CVPR_2023_paper.pdf)][[Code](https://github.com/WisconsinAIVision/UniversalFakeDetect)] 
  - [**CVPR '23**] Learning on Gradients: Generalized Artifacts Representation for GAN-Generated Images Detection [[Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Tan_Learning_on_Gradients_Generalized_Artifacts_Representation_for_GAN-Generated_Images_Detection_CVPR_2023_paper.pdf)][[Code](https://github.com/chuangchuangtan/LGrad)]
  - [**ICCV '23**] DIRE for Diffusion-Generated Image Detection [[Paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_DIRE_for_Diffusion-Generated_Image_Detection_ICCV_2023_paper.pdf)][[Code](https://github.com/ZhendongWang6/DIRE)]
  - [**NeurIPS' 23**] Seeing is not always believing: Benchmarking Human and Model Perception of AI-Generated Images [[Paper](https://arxiv.org/pdf/2304.13023)][[Code](https://github.com/Inf-imagine/Sentry)]
  - [**ICASSP '23**] On The Detection of Synthetic Images Generated by Diffusion Models [[Paper](https://arxiv.org/pdf/2211.00680)][[Code](https://github.com/grip-unina/DMimageDetection)]
  - [**CCS '23**] DE-FAKE: Detection and Attribution of Fake Images Generated by Text-to-Image Generation Models [[Paper](https://arxiv.org/pdf/2210.06998)]
  - [**OJSP '23**] Synthbuster: Towards Detection of Diffusion Model Generated Images [[Paper](https://ieeexplore.ieee.org/document/10334046)]
  - [**ICCVW '23**] Online Detection of AI-Generated Images [[Paper](https://openaccess.thecvf.com/content/ICCV2023W/DFAD/papers/Epstein_Online_Detection_of_AI-Generated_Images__ICCVW_2023_paper.pdf)]
  - [**ICCVW '23**] Detecting Images Generated by Deep Diffusion Models using their Local Intrinsic Dimensionality [[Paper](https://openaccess.thecvf.com/content/ICCV2023W/DFAD/papers/Lorenz_Detecting_Images_Generated_by_Deep_Diffusion_Models_Using_Their_Local_ICCVW_2023_paper.pdf)]
  - [**arxiv**] PatchCraft: Exploring Texture Patch for Efficient AI-generated Image Detection [[Paper](https://arxiv.org/pdf/2311.12397v3)]
  - [**arxiv**] Generalizable Synthetic Image Detection via Language-guided Contrastive Learning [[Paper](https://arxiv.org/pdf/2305.13800)][[Code](https://github.com/HighwayWu/LASTED)]
  - [**arxiv**] Raising the Bar of AI-generated Image Detection with CLIP [[Paper](https://arxiv.org/pdf/2312.00195)][[Code](https://github.com/grip-unina/ClipBased-SyntheticImageDetection/)]
  - [**arxiv**] GenDet: Towards Good Generalizations for AI-Generated Image Detection [[Paper](https://arxiv.org/pdf/2312.08880)]
  - [**arxiv**] AntifakePrompt: Prompt-Tuned Vision-Language Models are Fake Image Detectors [[Paper](https://arxiv.org/pdf/2310.17419)]
  - [**arxiv**] Generalizable Synthetic Image Detection via Language-guided Contrastive Learning [[Paper](https://arxiv.org/pdf/2305.13800)][[Code](https://github.com/HighwayWu/LASTED)]
</details>

<details open>
  <summary>2022</summary>

  - [**ECCV '22**] Detecting Generated Images by Real Images [[Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136740089.pdf)][[Code](https://github.com/Tangsenghenshou/Detecting-Generated-Images-by-Real-Images)]
  - [**ECCV '22**] FingerprintNet: Synthesized Fingerprints for Generated Image Detection [[Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136740071.pdf)]
</details>

<details open>
  <summary>2021</summary>

  - [**ICME '21**] Are GAN generated images easy to detect? A critical analysis of the state-of-the-art [[Paper](https://arxiv.org/pdf/2104.02617)]
</details>

<details open>
  <summary>2020</summary>

  - [**CVPR '20**] CNN-generated images are surprisingly easy to spot... for now [[Paper](https://arxiv.org/pdf/1912.11035)][[Code](https://github.com/peterwang512/CNNDetection)]
  - [**ECCV '20**] What makes fake images detectable? Understanding properties that generalize [[Paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123710103.pdf)][[Code](https://github.com/chail/patch-forensics)]
</details>

## Tools

## Others
Last updated on 2025.2.20
