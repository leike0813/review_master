Manuscript Number: TUST-D-25-02850  

MuckSeg: A deep learning-based algorithm for automated in-situ TBM muck morphology analysis

Dear Prof. Zhou,

Thank you for submitting your manuscript to Tunnelling and Underground Space Technology incorporating Trenchless Technology Research.

I have completed my evaluation of your manuscript. The reviewers recommend reconsideration of your manuscript following major revision. I invite you to resubmit your manuscript after addressing the comments below. Please resubmit your revised manuscript by Mar 17, 2026.

When revising your manuscript, please consider all issues mentioned in the reviewers' comments carefully: please outline every change made in response to their comments and provide suitable rebuttals for any comments not addressed. Please note that your revised submission may need to be re-reviewed. 

To submit your revised manuscript, please log in as an author at https://www.editorialmanager.com/tust/, and navigate to the "Submissions Needing Revision" folder.  

Research Elements (optional)
This journal encourages you to share research objects - including your raw data, methods, protocols, software, hardware and more – which support your original research article in a Research Elements journal. Research Elements are open access, multidisciplinary, peer-reviewed journals which make the objects associated with your research more discoverable, trustworthy and promote replicability and reproducibility. As open access journals, there may be an Article Publishing Charge if your paper is accepted for publication. Find out more about the Research Elements journals at https://www.elsevier.com/authors/tools-and-resources/research-elements-journals?dgcid=ec_em_research_elements_email.


Tunnelling and Underground Space Technology incorporating Trenchless Technology Research values your contribution and I look forward to receiving your revised manuscript.

Kind regards,  
Shucai Li  
Editor-in-Chief  

Tunnelling and Underground Space Technology incorporating Trenchless Technology Research

Editor and Reviewer comments:



Reviewer's Responses to Questions

Note: In order to effectively convey your recommendations for improvement to the author(s), and help editors make well-informed and efficient decisions, we ask you to answer the following specific questions about the manuscript and provide additional suggestions where appropriate.

1. Are the objectives and the rationale of the study clearly stated?

Please provide suggestions to the author(s) on how to improve the clarity of the objectives and rationale of the study. Please number each suggestion so that author(s) can more easily respond.

Reviewer #1: Yes

Reviewer #2: 1.A specialized image acquisition device was used to collect muck images from a conveyor belt, resulting in a dataset containing 70 images with detailed annotations. However, this number of labeled images is insufficient for training a deep learning model. Why were more data not collected using this device?
2.The stem block of MuckSeg employs multiple convolutional kernels operating in parallel, together with max pooling and average pooling, to reduce channel redundancy. However, as shown in Fig. 8, the number of channels in each branch does not decrease. How do the authors justify that this design effectively reduces channel redundancy?
3.Several hyperparameters are involved in MuckSeg. How were these parameters selected, and how did the authors ensure that the model does not suffer from overfitting? For example, learning rates of 5e-4 and 2e-4 are not commonly used in deep learning experiments.
4.The proposed method should be compared with more recent state-of-the-art approaches to better demonstrate its effectiveness.
5.The importance of the two key strategies (the training strategy and the post-processing algorithm) should be validated. For instance, ablation studies could be conducted to quantify their individual contributions.
6.The rock-grade classifier is introduced in Fig. 28 but has not been described earlier in the manuscript. This component should be clearly introduced and explained before it is used.
7.There is a class imbalance issue in the training dataset for the rock-grade predictor. What methods were taken to address this problem?

2. If applicable, is the method/study reported in sufficient detail to allow for its replicability and/or reproducibility?

Please provide suggestions to the author(s) on how to improve the replicability/reproducibility of their study. Please number each suggestion so that the author(s) can more easily respond.

Reviewer #1: Mark as appropriate with an X:
Yes [] No [] N/A []
Provide further comments here: Yes

Reviewer #2: Mark as appropriate with an X:
Yes [] No [] N/A []
Provide further comments here:
1.Several hyperparameters are involved in MuckSeg. How were these parameters selected, and how did the authors ensure that the model does not suffer from overfitting? For example, learning rates of 5e-4 and 2e-4 are not commonly used in deep learning experiments.

3. If applicable, are statistical analyses, controls, sampling mechanism, and statistical reporting (e.g., P-values, CIs, effect sizes) appropriate and well described?

Please clearly indicate if the manuscript requires additional peer review by a statistician. Kindly provide suggestions to the author(s) on how to improve the statistical analyses, controls, sampling mechanism, or statistical reporting. Please number each suggestion so that the author(s) can more easily respond.

Reviewer #1: Mark as appropriate with an X:
Yes [] No [] N/A []
Provide further comments here: No

Reviewer #2: Mark as appropriate with an X:
Yes [] No [] N/A []
Provide further comments here:
1. The statistical analyses and reporting are generally appropriate for the scope of the study
2. No additional statistical peer review is required

5. If applicable, are the interpretation of results and study conclusions supported by the data?

Please provide suggestions (if needed) to the author(s) on how to improve, tone down, or expand the study interpretations/conclusions. Please number each suggestion so that the author(s) can more easily respond.

Reviewer #1: Mark as appropriate with an X:
Yes [] No [] N/A []
Provide further comments here: No

Reviewer #2: Mark as appropriate with an X:
Yes [] No [] N/A []
Provide further comments here:
1. The interpretations and conclusions are generally well supported by the presented data.
2. Minor clarification of key conclusions may improve clarity.

6. Have the authors clearly emphasized the strengths of their study/methods?

Please provide suggestions to the author(s) on how to better emphasize the strengths of their study. Please number each suggestion so that the author(s) can more easily respond.

Reviewer #1: No

Reviewer #2: 1.The proposed method should be compared with more recent state-of-the-art approaches to better demonstrate its effectiveness.
2.The importance of the two key strategies (the training strategy and the post-processing algorithm) should be validated. For instance, ablation studies could be conducted to quantify their individual contributions.

7. Have the authors clearly stated the limitations of their study/methods?

Please list the limitations that the author(s) need to add or emphasize. Please number each limitation so that author(s) can more easily respond.

Reviewer #1: No

Reviewer #2: The limitations discussed in the Discussion section of this manuscript are sufficient.

8. Does the manuscript structure, flow or writing need improving (e.g., the addition of subheadings, shortening of text, reorganization of sections, or moving details from one section to another)?

Please provide suggestions to the author(s) on how to improve the manuscript structure and flow. Please number each suggestion so that author(s) can more easily respond.

Reviewer #1: Yes

Reviewer #2: Overall structure and organization are clear and well designed.

9. Could the manuscript benefit from language editing?

Reviewer #1: Yes

Reviewer #2: Yes

 


Reviewer #1: The manuscript proposes MuckSeg, a ConvNeXt-based U-shaped network for instance segmentation of TBM conveyor muck, combined with non-binary labels, a two-stage training strategy, generalized focal loss, and progressive post-processing. The aim is to automatically extract muck size, flatness, and roundness indices for use in TBM tunnelling analysis and monitoring.
The topic is important, and the paper shows solid engineering background and a fairly complete pipeline from image acquisition to segmentation and metric extraction. However, in its current form the manuscript still has substantial weaknesses in: the clarity of its claimed contributions and novelty, the completeness and fairness of experimental validation and the depth of engineering interpretation of the results. Therefore, I recommend Major Revision, below I list detailed comments and suggestions:
1. Novelty is not clearly quantified.
The manuscript repeatedly mentions several enhancements, ConvNeXt encoder, stem block, semi-coupled decoder with REA, non-binary labels, generalized focal loss, dual-stage training, progressive post-processing. However, most of these are only qualitatively motivated, it is not clear which ones actually contribute to performance and by how much. Highlight what is truly new in this work, rather than listing many architectural choices.
2. Engineering problem and method are not fully "closed-loop".
The engineering motivation (long TBM distance, need for online muck size/shape monitoring, link to geology and excavation efficiency) is well described in the introduction, but in the results and discussion sections the connection back to TBM performance and geotechnical parameters is weak.
It is suggested to illustrate how the extracted PSD (particle size distribution), flatness, and roundness from MuckSeg compare with manual sieving measurements on selected frames. And how these indices correlate with TBM parameters (e.g., penetration rate, thrust, specific energy) or with rock mass classification along a short tunnel stretch. Additionally, please discuss the engineering meaning of the reported errors. For example: A mean absolute error of ~3.8 mm for mean particle size when the typical mean size is ~30 mm corresponds to roughly 12-13% relative error. Is this acceptable for the intended engineering decisions.
3. Comparative baselines are too limited.
Currently the main comparison is with MSD-UNet, which is indeed a relevant baseline, but the claim that MuckSeg is superior would be stronger if other standard architectures were included. Please consider adding results for improved Mask-RCNN, improved U-Net, and ViT. Ensure all methods use the same resolution and data augmentation, and trained with comparable epochs and learning-rate schedules.
4. No systematic ablation for key modules.
Beyond the dual-stage training and pretraining tests, there is little evidence about which parts of MuckSeg are truly critical. Please conduct and report ablation experiments of stem block, semi-coupled decoder+REA, non-binary labels and the progressive 3-step post-processing. For each ablation, report key metrics (region IoU, boundary IoU, 60-HD/95-HD, false positive/false negative rates, and if possible runtime). In the discussion, summarize which modules contribute most and which are mainly trade-offs between accuracy and complexity.
5. Progressive post-processing is complex and needs clearer intuition and boundary conditions.
The three-step (first-/second-/third-rank) segmentation pipeline combining morphological operations, center-point proposals, and watershed is mathematically described but not easy to follow intuitively. It is suggested to add one or two illustrative examples where all three steps are shown. Also, discuss the sensitivity of the algorithm to its key thresholds and iteration limits (e.g., maximum iteration, distance thresholds). What happens if these are set too small or too large. Is there a rationale for their specific numeric values.
6. Error analysis and uncertainty discussion should be deepened.
The paper shows histograms and plots of error metrics, but does not sufficiently analyze how performance varies with particle size, shape, or image conditions. Group results by particle size ranges (e.g., <10 mm, 10-30 mm, 30-60 mm, >60 mm) and report MAE, false negative rate, and mis-segmentation ratios per group. It is mentioned that very fine particles (e.g., 5-10 mm) are harder to detect, quantifying this would be valuable.
For a few representative frames, plot PSD curves derived from MuckSeg vs. from manual sieving/annotation, and compute relative errors in D10, D50, D90. This directly reflects the impact on engineering analysis.
Analyze sources of error and uncertainty: e.g., occlusion, motion blur, muddy coatings, lighting variations, high fragment stacking.
7. Abbreviations in the main text only require their full names to be provided upon first appearance. Subsequent occurrences do not need to be redefined. For example, on line 55: Computer Vision (CV).
8. The citations in the main text are inconsistent, such as on line 43 (Yaghoobi et al., 2019) and line 78 (Chen et al., 2018). Similar issues exist elsewhere in the manuscript. Please review carefully.
9. Punctuation marks should not appear in the formula, such as in Eq. (1), (2), (3), etc.
10. In Figure 12, the "detach" and "initialized" sections overlap the text below, making the text difficult to read.
11. Figure 29 does not require an outer border. Labels (a) and (b) can be placed at the bottom of the image.
12. The format of references should be consistent. Some names within the text are connected by "-", while others are not.
13. Certain images extend too far beyond the right margin of the article. It is recommended to adjust the image size and layout, as shown in Figures 17, 28, etc.
I therefore recommend Major Revision, with the expectation that the authors address the points above through additional analysis, clearer explanations, and careful language polishing.




Reviewer #2: This field is optional. If you have any additional suggestions beyond those relevant to the questions above, please number and list them here.
In this manuscript, the author introduces MuckSeg, a specialized instance segmentation method for analyzing muck images from TBM conveyor belts. MuckSeg employs a U-shaped fully convolutional neural network based on the ConvNeXt architecture, coupled with a suite of post-processing algorithms. The experimental results demonstrate excellent performance on a real-world TBM tunneling project. Overall, the manuscript is well written and presents interesting results. The issues raised below are relatively minor and can be addressed with a minor revision:
1. A specialized image acquisition device was used to collect muck images from a conveyor belt, resulting in a dataset containing 70 images with detailed annotations. However, this number of labeled images is insufficient for training a deep learning model. Why were more data not collected using this device?
2. The stem block of MuckSeg employs multiple convolutional kernels operating in parallel, together with max pooling and average pooling, to reduce channel redundancy. However, as shown in Fig. 8, the number of channels in each branch does not decrease. How do the authors justify that this design effectively reduces channel redundancy?
3. Several hyperparameters are involved in MuckSeg. How were these parameters selected, and how did the authors ensure that the model does not suffer from overfitting? For example, learning rates of 5e-4 and 2e-4 are not commonly used in deep learning experiments.
4. The proposed method should be compared with more recent state-of-the-art approaches to better demonstrate its effectiveness.
5. The importance of the two key strategies (the training strategy and the post-processing algorithm) should be validated. For instance, ablation studies could be conducted to quantify their individual contributions.
6. The rock-grade classifier is introduced in Fig. 28 but has not been described earlier in the manuscript. This component should be clearly introduced and explained before it is used.
7. There is a class imbalance issue in the training dataset for the rock-grade predictor. What methods were taken to address this problem?
