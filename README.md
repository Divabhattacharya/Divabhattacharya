<div align="center">

# Diva Bhattacharya

**GPU compilers · CUDA · ML systems**

Electrical engineering at NSUT Delhi. I build tools that check whether GPU compilers produce correct code,
and ML systems that hold up under real data.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Diva%20Bhattacharya-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/diva-b-829a80192/)
[![Codeforces](https://img.shields.io/badge/Codeforces-mana2014in-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/mana2014in)
![Kaggle](https://img.shields.io/badge/Kaggle-Expert%20%C2%B7%20Silver%20Medal-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)

</div>

---

## ⚙️ GPU compilers & CUDA

| Project | What it does | Results |
|---|---|---|
| **[ptxsim](https://github.com/Divabhattacharya/ptxsim)**<br><sub>C++17 · LLVM · Z3 · Python</sub> | A PTX interpreter with independent thread scheduling. It drives differential fuzzing of LLVM's NVPTX backend, automatic test-case reduction, and Alive2-style SMT translation validation. | 47,392 random kernels × 7 compiler pipelines with 0 mismatches. The fuzzer found 2 interpreter bugs, each reduced to a one-line repro. Proved O0≡O3 for 7 kernels with Z3 |
| **[cuda-compiler-verify](https://github.com/Divabhattacharya/cuda-compiler-verify)**<br><sub>CUDA C++ · PTX · Python</sub> | A CUDA compiler test suite: 6 programs × 10 `nvcc`/`ptxas` configurations. It checks results bit-exactly, against NVIDIA's documented ULP bounds, and against forward error bounds, plus differential and PTX code-generation tests | Hand-written PTX loaded through the CUDA Driver API on an A100, including a negative test that the JIT rejects ill-typed PTX |
| **[cudasmith](https://github.com/Divabhattacharya/cudasmith)** <sub>(WIP)</sub><br><sub>CUDA · Python</sub> | A Csmith-style generator of random CUDA kernels that are free of undefined behaviour, with warp shuffles placed only in converged code, for differential testing of `nvcc` | Generator, campaign runner and reducer written; GPU campaign pending |

## 🧠 ML systems

| Project | What it does | Stack |
|---|---|---|
| **[Pantanal ProtoSSM](https://github.com/Divabhattacharya/birdclef2026-pantanal-protossm)**<br><sub>BirdCLEF+ 2026</sub> | Multi-label bird-call detection over 234 taxa, built on Perch teacher embeddings with a ProtoSSM temporal model, OOF stacking and TTA | TensorFlow · PyTorch · SSM |
| **[NeuroAfrica-3D](https://github.com/Divabhattacharya/neuroafrica-brats-glioma-segmentation)**<br><sub>BraTS-Africa</sub> | 3D MRI glioma segmentation (WT/TC/ET) with Dice, NSD and HD95 tracking and SageMaker-ready fold training | PyTorch · MONAI · nnU-Net |
| **[GossipPPO](https://github.com/Divabhattacharya/gossippop-federated-rl)**<br><sub>Federated RL</sub> | Decentralized multi-agent RL using peer-to-peer gossip averaging, with Byzantine-robust filtering under 30% offline and 15% malicious agents | Ray · PPO · NetworkX |
| **[LiveKit Barge-In Agent](https://github.com/Divabhattacharya/livekit-barge-in-agent)**<br><sub>Voice AI</sub> | Real-time interruption handling for voice agents: filler suppression, command detection and latency metrics | Whisper · LiveKit · WebRTC |

## 🏅 Highlights

- **Kaggle Silver Medal**: CSIRO Image2Biomass, global rank 30 · Kaggle Competitions Expert
- **Research internships**:
  - IIT Delhi (Prof. Brejesh Lall): space-debris streak detection for spacecraft safety
  - IIT Kharagpur (Prof. Budhananda Banerjee): robust applied ML
  - Heriot-Watt University (Prof. Bhaskar SenGupta): electromagnetic noise harvesting and signal recovery
- **Texas Instruments BYTE** mentee: analog front ends, digital logic, and firmware–sensor synchronisation

## 🧰 Toolbox

| | |
|---|---|
| **Languages** | C · C++17 · Python · CUDA C++ · PTX · SQL · MATLAB |
| **GPU & compilers** | nvcc / ptxas · LLVM IR & NVPTX · CUDA Driver API · Z3 (SMT) · cuobjdump |
| **Machine learning** | PyTorch · TensorFlow · MONAI · nnU-Net · scikit-learn · Ray · Whisper |
| **Infrastructure** | AWS SageMaker · S3 · ECR · CloudWatch · Docker · Git · Linux |
