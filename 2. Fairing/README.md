# Kubeflow Fairing
쿠브플로우 페어링에 대한 설명입니다.  
블로그 링크: [https://seokii.tistory.com/206](https://seokii.tistory.com/206)

## Faring Documentation
쿠브플로우 페어링 공식 문서 사이트입니다.  
Docs: https://www.kubeflow.org/docs/external-add-ons/fairing/  
공식 문서를 통해 다음 내용을 확인할 수 있습니디.
- Overview of Kubeflow Fairing
- Install Kubeflow Fairing
- Configure Kubeflow Fairing
- Fairing on Azure
- Fairing on GCP
- Tutorials
- Reference

## Fairing 설치
자세한 내용은 블로그 글을 참고바랍니다.  
&nbsp;<br>
fairing 설치
```
pip install kubeflow-fairing
```
fairing 확인 
```
pip show kubeflow-fairing
```

## Faring 개념이해
**페어링(Fairing)** 은 쿠브플로우가 설치된 환경에서 **ML 모델의 학습과 배포를 도와주는** 파이썬 패키지입니다.  
공식 문서에서는 페어링에 대해 다음과 같이 설명합니다.
> 쿠브플로 페어링은 쿠브플로에서 ML 모델을 쉽게 교육하고 배포할 수 있는 파이썬 패키지입니다.  
쿠브플로 페어링은 다른 플랫폼에서 훈련하거나 배포할 수 있도록 확장될 수도 있습니다.  
현재 쿠브플로 페어링은 구글 AI 플랫폼에서 훈련할 수 있도록 확장되었습니다.

&nbsp;<br>
또한, 쿠브플로 페어링 프로젝트의 목표는 다음과 같습니다.
- **쉬운 ML 모델 훈련 작업 패키지화** : 작성한 모델 학습 코드를 도커 이미지화
- **하이브리드 클라우드 환경에서의 쉬운 학습** : 고급 API를 제공해 기본 인프라에 대한 지식이 필요 없음
- **쉬운 배포** : 학습된 모델을 배치하는 과정 간소화

&nbsp;<br>
쿠브플로우 페어링에는 다음과 같은 중요한 3가지의 개념이 있습니다.
- Preprocessor(전처리기)
- Builder(빌더)
- Deployer(배포)

### Preprocessor
전처리기는 도커 이미지로 패키지화할 대상을 지정합니다.  
즉, 컨테이너 이미지를 만들 때, 이미지 생성에 필요한 정보들을 정의합니다.  
전처리기를 통해 컨테이너 이미지에 들어갈 입력파일을 선택, 변환, 제외할 수 있습니다.  
제공하는 전처리기의 종류는 4가지 입니다.  
- python : 입력 파이썬 파일을 그대로 컨테이너 이미지에 직접 복사해 패키징합니다.
- notebook : 주피터 노트북 파일을 파이썬 파일로 변환 후 코드에 대한 패키징을 진행합니다.
- full_notebook : 노트북 파일의 전체 코드를 실행하고,결과를 다시 노트북 파일로 생성합니다.
- function : 단일함수를 전처리 및 패키징합니다.

### Builder
빌더는 컨테이너 이미지를 빌드하는 방법 및 컨테이너 레지스트리의 위치를 정의합니다.  
전처리기가 생성한 패키지를 도커 이미지화시키는 역할을 합니다.  
제공하는 빌더의 종류는 3가지 입니다.  
- append : 도커 클라이언트를 사용하지 않고, 파이썬 라이브러리인 containerregistry를 사용해 기존 컨테이너 이미지를 바탕으로 코드를 새 레이어로 추가합니다.
도커를 사용하지 않는 환경에서 사용하기 좋습니다. 또한, 추가된 부분만 컨테이너 이미지 레지스트리에 푸시하기 때문에 상대적으로 시간이 더 적게 소모됩니다. 
- docker : 로컬 도커 클라이언트로 도커 이미지를 생성합니다.
- cluster : 쿠버네티스 클러스터에서 사용할 컨테이너 이미지를 생성합니다. 구글 컨테이너 툴인 Kaniko를 사용합니다.

### Deployer
컨테이너 이미지 생성이 완료되면 해당 이미지의 배포를 진행합니다.  
Deployer를 통해서 이미지를 배포하고, 실행할 위치를 정의합니다.  
제공하는 Deployer의 종류는 매우 다양합니다.  
- job : 쿠버네티스 job 리소스를 사용해 학습을 시작합니다.
- tfjob : 쿠브플로우의 TFJob 컴포넌트를 사용헤 텐서플로우 학습 작업을 시작합니다.
- pytorchjob : 쿠브플로우의 PyTorchJob 컴포넌트를 사용해 파이토치 학습 작업을 시작합니다.
- gcpjob : GCP에 학습 작업을 보냅니다.
- serving : 쿠브플로우의 디플로이먼트와 서비스를 이용한 예측모델을 서빙합니다.
- kfserving : 쿠브플로우의 KFServing을 사용해 예측모델을 서빙합니다.
- gcpserving : 학습된 모델을 GCP 서빙 모델로 배포합니다.
