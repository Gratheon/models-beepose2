## Gratheon/beepose2

A fork of DeepLabCut with bee pose model

https://github.com/user-attachments/assets/e8b0958a-8d1e-4a3e-a843-34505a558832




## Quick start

Developers Stable Release: very quick start (Python 3.10+ required) to install 

```bash
pip install --pre  "deeplabcut[gui]"
```

Edit `config.yaml` and set new project path

## Keypoints
After evaluation, we trained a model using **DeepLabCut**. We defined 13-keypoint skeleton where `thorax` connected most of the nodes:
```
multianimalbodyparts:
- head
- thorax
- abdomen
- antenna-left
- antenna-right
- fore-leg-left
- fore-leg-right
- mid-leg-left
- mid-leg-right
- hind-leg-left
- hind-leg-right
- wing-left
- wing-right
```

## mAP
The following are the results from our model training on OSX:

```
Training for epoch 200 done, starting evaluation
Epoch 200/200 (lr=1e-05), train loss 0.00241, valid loss 0.00294
Model performance:
  metrics/test.rmse:          62.60
  metrics/test.rmse_pcutoff:  56.85
  metrics/test.mAP:           69.38
  metrics/test.mAR:           76.67
```
## Performance
3 FPS on Mac M3