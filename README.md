<img src="https://capsule-render.vercel.app/api?type=waving&color=0:76B900,50:1F8ACB,100:0A66C2&height=170&section=header&text=Diva%20Bhattacharya&fontSize=44&fontColor=ffffff&fontAlignY=36&desc=GPU%20compilers%20%C2%B7%20CUDA%20%C2%B7%20ML%20systems&descAlignY=58&descSize=17" width="100%" alt="Diva Bhattacharya"/>

<div align="center">

<img src="assets/diva.png" width="170" alt="Diva Bhattacharya"/>

<a href="https://github.com/Divabhattacharya"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1200&color=76B900&center=true&vCenter=true&width=720&lines=Kaggle+Silver+%E2%80%94+CSIRO+Image2Biomass%2C+Global+Rank+30;Fuzzing+%2B+Z3+verification+of+LLVM's+NVPTX+backend;PTX+interpreter+in+C%2B%2B%2C+no+GPU+required;CUDA+compiler+testing+on+an+NVIDIA+A100" alt="Typing SVG"/></a>

<a href="https://www.linkedin.com/in/diva-bhattacharya-829a80192/"><img src="https://img.shields.io/badge/LinkedIn-Diva%20Bhattacharya-0A66C2?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHJlY3Qgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiByeD0iNCIgZmlsbD0iI2ZmZmZmZiIvPjx0ZXh0IHg9IjEyIiB5PSIxOCIgZm9udC1mYW1pbHk9IkFyaWFsLEhlbHZldGljYSxzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iYm9sZCIgZm9udC1zaXplPSIxNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzBBNjZDMiI%2BaW48L3RleHQ%2BPC9zdmc%2B" alt="LinkedIn"/></a>
<a href="https://www.kaggle.com/competitions/csiro-biomass/writeups/30th-place-solution"><img src="https://img.shields.io/badge/Kaggle-Silver%20%C2%B7%20Rank%2030-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle Silver"/></a>
<a href="https://codeforces.com/profile/mana2014in"><img src="https://img.shields.io/badge/Codeforces-mana2014in-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white" alt="Codeforces"/></a>

**Electrical Engineering @ NSUT Delhi** · I build tools that check whether GPU compilers produce correct code,<br/>
and ML systems that hold up on real data.

</div>

---

## 🏆 Kaggle Silver Medal: CSIRO Image2Biomass, Global Rank 30

<table>
<tr>
<td width="100%">

### Dual-Stream DINOv3 + Gated Depthwise Convolutions + Auxiliary Metadata

<img src="https://img.shields.io/badge/medal-silver-C0C0C0?style=flat-square"/> <img src="https://img.shields.io/badge/global%20rank-30-20BEFF?style=flat-square"/> <img src="https://img.shields.io/badge/private%20LB-0.63-76B900?style=flat-square"/> <img src="https://img.shields.io/badge/public%20LB-0.75-76B900?style=flat-square"/> <img src="https://img.shields.io/badge/PyTorch-AMP-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"/>

Predicting pasture biomass (green, dead, clover and total dry matter) from field photos:

- **Dual-stream vision:** the left and right fields of view of each image are modelled as two streams on a DINOv3 backbone and fused with gated depthwise convolutions.
- **Auxiliary metadata prediction:** extra training signal for a small dataset of about 357 images.
- **Metric-aligned, weighted regression heads** for each biomass component, trained with mixed precision and cosine annealing.

**[📖 Read the 30th-place solution write-up →](https://www.kaggle.com/competitions/csiro-biomass/writeups/30th-place-solution)**

</td>
</tr>
</table>

## ⚡ GPU compilers & CUDA

<table>
<tr>
<td width="50%" valign="top">

### [ptxsim](https://github.com/Divabhattacharya/ptxsim)
<sub>C++17 · LLVM · Z3 · Python</sub>

A PTX interpreter with Volta-style independent thread scheduling. It drives three checks on LLVM's NVPTX backend: **differential fuzzing**, **automatic test-case reduction**, and **Alive2-style SMT translation validation**.

- **47,392** random kernels × 7 compiler pipelines with **0 mismatches**
- The fuzzer found **2 interpreter bugs**, each auto-reduced to a one-line repro
- **O0 ≡ O3 proved** with Z3, and a planted miscompile caught with a concrete counterexample

</td>
<td width="50%" valign="top">

### [cuda-compiler-verify](https://github.com/Divabhattacharya/cuda-compiler-verify)
<sub>CUDA C++ · PTX · Python · A100</sub>

A test suite for the `nvcc` → PTX → `ptxas` → SASS toolchain.

- 6 CUDA programs × **10 compiler configurations** (`-G`, `-Xptxas -O0`, register spills, `--fmad=false`, PTX JIT, fast-math, …)
- Bit-exact checks, NVIDIA's documented **ULP bounds**, and forward error bounds
- FileCheck-style **PTX codegen tests**, plus hand-written PTX via the CUDA Driver API

</td>
</tr>
<tr>
<td colspan="2">

**[cudasmith](https://github.com/Divabhattacharya/cudasmith)** <sub>(work in progress)</sub>: a Csmith-style generator of random CUDA kernels free of undefined behaviour, with convergence-aware warp shuffles, for differential testing of `nvcc` on real GPUs.

</td>
</tr>
</table>

## 🧠 Machine learning systems

<table>
<tr>
<td width="50%" valign="top">

### [Pantanal ProtoSSM](https://github.com/Divabhattacharya/birdclef2026-pantanal-protossm)
<sub>BirdCLEF+ 2026 · TensorFlow · PyTorch</sub>

Multi-label bird-call detection over **234 taxa**: Perch teacher embeddings, a ProtoSSM temporal model with cross-attention and prototypes, OOF stacking and TTA.

</td>
<td width="50%" valign="top">

### [NeuroAfrica-3D](https://github.com/Divabhattacharya/neuroafrica-brats-glioma-segmentation)
<sub>BraTS-Africa · MONAI · nnU-Net</sub>

3D MRI glioma segmentation (WT / TC / ET) with Dice, NSD and HD95 tracking and SageMaker-ready fold training.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [GossipPPO](https://github.com/Divabhattacharya/gossippop-federated-rl)
<sub>Federated RL · Ray · PPO</sub>

Decentralized multi-agent RL using peer-to-peer gossip averaging. It stays robust under **30% offline and 15% Byzantine** agents, with median/MAD filtering rejecting 214 bad updates.

</td>
<td width="50%" valign="top">

### [LiveKit Barge-In Agent](https://github.com/Divabhattacharya/livekit-barge-in-agent)
<sub>Voice AI · Whisper · WebRTC</sub>

Real-time interruption handling for voice agents: filler suppression, command detection and latency metrics.

</td>
</tr>
</table>

## 🔬 Research & experience

| | |
|---|---|
| **IIT Delhi**, EE (Prof. Brejesh Lall) | AI-based space-debris streak detection for spacecraft safety |
| **IIT Kharagpur** (Prof. Budhananda Banerjee) | Robust applied-ML systems: reproducible training, uncertainty and error analysis |
| **Heriot-Watt University, UK** (Prof. Bhaskar SenGupta) | Electromagnetic noise harvesting and signal recovery |
| **Texas Instruments BYTE** | Analog front ends, digital logic, firmware–sensor synchronisation |

## 🧰 Toolbox

<p>
<img src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black"/>
<img src="https://img.shields.io/badge/C++17-00599C?style=for-the-badge&logo=cplusplus&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white"/>
<img src="https://img.shields.io/badge/PTX-76B900?style=for-the-badge&logo=nvidia&logoColor=white"/>
<img src="https://img.shields.io/badge/LLVM-262D3A?style=for-the-badge&logo=llvm&logoColor=white"/>
<img src="https://img.shields.io/badge/Z3%20SMT-4B4B4B?style=for-the-badge"/>
</p>
<p>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
<img src="https://img.shields.io/badge/MONAI-00A3E0?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Ray-028CF0?style=for-the-badge&logo=ray&logoColor=white"/>
<img src="https://img.shields.io/badge/AWS%20SageMaker-232F3E?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"/>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0A66C2,50:1F8ACB,100:76B900&height=110&section=footer" width="100%" alt=""/>
